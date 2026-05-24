# Skill Creator 深度研究

来源：`~/.claude/plugins/marketplaces/claude-plugins-official/plugins/skill-creator/`

Anthropic 官方的 skill 创建工具——一个完整的 skill 开发、评估、迭代工作流。

---

## 整体架构

```
skill-creator/
├── SKILL.md                    ← 主 skill（工作流指南）
├── agents/
│   ├── grader.md               ← 评估 agent：对每个 assertion 打分
│   ├── comparator.md           ← 盲测 agent：A/B 比较两个输出
│   └── analyzer.md             ← 分析 agent：解释为什么某版本赢了
├── scripts/
│   ├── run_eval.py             ← 运行单次评估
│   ├── run_loop.py             ← 评估+改进循环（含 train/test 分割）
│   ├── improve_description.py  ← 用 Claude 优化 description 字段
│   ├── aggregate_benchmark.py  ← 聚合统计结果
│   ├── generate_report.py      ← 生成 HTML 报告
│   ├── package_skill.py        ← 打包为 .skill 文件
│   └── quick_validate.py       ← 快速校验 SKILL.md 格式
├── eval-viewer/
│   ├── generate_review.py      ← 启动评审浏览器界面
│   └── viewer.html             ← 评审 UI 模板
├── assets/
│   └── eval_review.html        ← description 优化评审 UI 模板
└── references/
    └── schemas.md              ← 所有 JSON schema 定义
```

---

## 核心工作流

### 阶段一：创建 Skill

```
1. 捕捉意图
   ├── 从对话历史中提取已有工作流（"turn this into a skill"）
   ├── 或通过问答理解：做什么？何时触发？输出格式？需要测试吗？
   └── 调研边界情况、输入输出格式、成功标准

2. 撰写 SKILL.md
   ├── name：技能标识符
   ├── description：触发条件（要"pushy"，防止 undertrigger）
   └── 内容：目标：清晰 > 限制

3. 确定测试用例（2-3个真实 prompt）
   └── 保存到 evals/evals.json
```

### 阶段二：运行评估

**关键规则**：每个测试用例同时派生两个子 Agent：
- `with_skill`：带技能运行
- `without_skill`（新 skill）或 `old_skill`（改进已有 skill）：基线

**不能**先跑 with_skill，再回来跑 baseline——必须同一轮同时启动。

```
工作目录结构：
<skill-name>-workspace/
└── iteration-1/
    ├── eval-0/
    │   ├── with_skill/outputs/    ← 带 skill 的输出
    │   ├── without_skill/outputs/ ← 基线输出
    │   ├── eval_metadata.json
    │   └── timing.json            ← 从任务通知中捕获（不可事后恢复）
    └── benchmark.json
```

### 阶段三：边跑边写 Assertions

子 Agent 运行期间，同时草拟定量 assertions：

```json
{
  "id": 1,
  "prompt": "用户的任务 prompt",
  "expected_output": "预期结果描述",
  "expectations": [
    "输出包含 X",
    "skill 使用了 Y 脚本"
  ]
}
```

好的 assertion 特征：
- 客观可验证（有的放矢，不是"写得好"这种主观描述）
- 描述性命名（在 benchmark viewer 中一眼看懂）
- 有辨别力（正确完成时 PASS，错误时 FAIL）

### 阶段四：评分 + 聚合 + 展示评审

```bash
# 1. 每个 run 用 grader agent 评分 → grading.json
# 2. 聚合统计
python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>
# → 生成 benchmark.json 和 benchmark.md

# 3. 启动评审界面（ALWAYS 先给用户看，不要自己先做改进）
nohup python <skill-creator-path>/eval-viewer/generate_review.py \
  <workspace>/iteration-N \
  --skill-name "my-skill" \
  --benchmark <workspace>/iteration-N/benchmark.json \
  > /dev/null 2>&1 &
```

评审界面有两个 tab：
- **Outputs**：每个测试用例的输入/输出，用户可留反馈
- **Benchmark**：pass_rate / time / tokens 统计对比

### 阶段五：根据反馈改进

```json
// feedback.json 格式
{
  "reviews": [
    {"run_id": "eval-0-with_skill", "feedback": "图表缺少坐标轴标签"},
    {"run_id": "eval-1-with_skill", "feedback": ""},  // 空 = 满意
  ],
  "status": "complete"
}
```

改进原则：
1. **从反馈中泛化**：改 skill 要适用百万次调用，不是过拟合这几个测试
2. **保持 prompt 精简**：删掉没起作用的内容，读 transcript 而非只看输出
3. **解释 Why**：写明为什么要这么做，不要堆 MUST/NEVER
4. **提取重复模式**：3个测试都写了同一个脚本？把它放进 `scripts/`

---

## Description 优化子系统

这是 skill-creator 独有的功能：用机器学习方法优化 description 字段的触发准确率。

### 流程

```bash
# 1. 生成 20 个评估 prompt（should-trigger + should-not-trigger）
# 2. 用户在浏览器中审核（eval_review.html）
# 3. 运行优化循环
python -m scripts.run_loop \
  --eval-set <trigger-eval.json> \
  --skill-path <skill-path> \
  --model claude-sonnet-4-6 \
  --max-iterations 5 \
  --verbose
```

### 训练/测试分割（防止过拟合）

`run_loop.py` 自动将 eval set 按 60/40 分割：
- 60% train：用于优化
- 40% held-out test：用于验证（选最好的 description 按 test 分数，不是 train 分数）

### Trigger Eval Query 设计原则

**Should-trigger（8-10个）**：
- 不同措辞的同一意图
- 不明说技能名但明显需要它
- 罕见用例和竞争场景

**Should-not-trigger（8-10个）**：
- **不能**是无关的简单情况（"写一个 fibonacci 函数"对 PDF skill 来说太容易排除）
- **必须**是真正难以区分的近似情况——共享关键词但实际不需要这个 skill

**好的 query 示例**（具体、真实）：
```
"ok so my boss just sent me this xlsx file (its in my downloads, called something 
like 'Q4 sales final FINAL v2.xlsx') and she wants me to add a column that shows 
the profit margin as a percentage. The revenue is in column C and costs are in D"
```

**差的 query 示例**（太抽象）：
```
"Format this data"
"Extract text from PDF"
```

---

## 三个专业 Agent

### Grader Agent（grader.md）

**职责**：评估每个 assertion 是否通过，并对 eval 本身提出改进建议。

**8步流程**：
1. 读 transcript
2. 检查输出文件
3. 评估每个 assertion（PASS/FAIL + 引用证据）
4. 提取并验证输出中的隐含声明
5. 读 user_notes.md（如存在）
6. 批评 eval 本身（非辨别性 assertion？遗漏重要检查？）
7. 写 grading.json
8. 读取 metrics/timing 数据

**PASS 条件**：有明确证据 AND 证据反映真实完成（不是表面合规）

**FAIL 条件**：无证据 / 证据矛盾 / 证据肤浅（文件名对但内容错）

### Comparator Agent（comparator.md）

**职责**：盲测——不知道哪个是 A、哪个是 B，只看输出质量。

**评分维度**：
- Content：正确性、完整性、准确性（1-5分）
- Structure：组织性、格式、可用性（1-5分）
- 综合得分（1-10分）

**决策优先级**：
1. 主要：综合 rubric 分数
2. 次要：assertion pass rate（如有）
3. 决胜局：真正相等时才判 TIE（应尽量少用）

### Analyzer Agent（analyzer.md）

**职责**：分析为什么某个版本赢了，给 skill 改进建议。

---

## JSON Schema 体系

| 文件 | 位置 | 用途 |
|------|------|------|
| `evals.json` | `evals/evals.json` | 测试用例定义 |
| `grading.json` | `<run-dir>/grading.json` | Grader 输出 |
| `metrics.json` | `<run-dir>/outputs/metrics.json` | Executor 的工具调用统计 |
| `timing.json` | `<run-dir>/timing.json` | 壁钟时间（从任务通知捕获，不可事后恢复） |
| `benchmark.json` | `<workspace>/iteration-N/benchmark.json` | 聚合统计结果 |
| `history.json` | workspace 根目录 | 版本迭代记录 |
| `comparison.json` | `<grading-dir>/comparison-N.json` | Comparator 输出 |
| `analysis.json` | `<grading-dir>/analysis.json` | Analyzer 输出 |

`benchmark.json` 的字段名必须精确匹配 viewer 预期：
- `configuration` 不是 `config`
- `pass_rate` 嵌套在 `result` 下，不是顶层

---

## 不同环境下的适配

| 环境 | 差异 |
|------|------|
| **Claude Code** | 完整功能（子 Agent、浏览器、CLI） |
| **Claude.ai** | 无子 Agent：串行执行；无浏览器：直接展示结果；无 description 优化 |
| **Cowork** | 有子 Agent；无浏览器：用 `--static` 生成静态 HTML |

---

## 关键操作注意事项

1. **timing.json 必须即时保存**：从子 Agent 任务通知中获取 `total_tokens` 和 `duration_ms`，不保存就消失了
2. **先展示给用户，再自己改**：运行完测试必须先启动 eval-viewer 让用户审查，不能自己直接开始改进
3. **directory listing failure**：benchmark.json 字段名必须严格匹配 viewer schema
4. **不用 `/skill-test`**：这一节是一个完整序列，不中断，不用其他测试 skill
