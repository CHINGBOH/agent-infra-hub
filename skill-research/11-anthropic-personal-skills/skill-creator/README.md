# skill-creator（Personal Skills 版）

**Added by:** Anthropic  
**Trigger:** Slash command + auto  
**类型：** A型 SKILL.md Skill（评估循环模式）

---

## Description（触发描述）

**English:**  
Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

**中文：**  
创建新技能、修改和改进现有技能，以及衡量技能性能。当用户想要从头创建技能、编辑或优化现有技能、运行评估测试技能、对技能性能进行基准测试或优化技能描述时使用。

---

## 与 09-skill-creator（插件版）的对比

两者是同一个 skill 的不同版本/来源：

| 维度 | Personal Skills 版（本文件） | 插件版（09-skill-creator） |
|------|-----------------------------|-----------------------------|
| 来源 | claude.ai/customize/skills | ~/.claude/plugins/cache/ |
| 详细程度 | 较简洁，专注核心流程 | 极详细，含完整工具链 |
| 评估工具 | 有（同样的 aggregate_benchmark） | 有（完整 scripts/ + agents/） |
| 描述优化 | 有（但 claude.ai 跳过） | 有（含 run_loop.py） |
| 盲对比 | 有（但 claude.ai 跳过） | 有（comparator.md） |
| 与用户沟通 | 强调避免技术术语 | 未特别强调 |

**核心流程完全一致**，本版本更加精炼，同时增加了 claude.ai 环境的适配说明。

---

## 核心流程（7步）

```
1. 决定技能要做什么以及大致如何实现
2. 编写技能草稿（SKILL.md）
3. 创建 2-3 个测试提示
4. 帮助用户评估结果（定性 + 定量）
5. 根据反馈重写技能
6. 重复直到满意
7. 扩大测试集，更大规模再次尝试
```

---

## SKILL.md 完整内容

### Skill Creator

A skill for creating new skills and iteratively improving them.

**At a high level, the process of creating a skill goes like this:**
1. Decide what you want the skill to do and roughly how it should do it
2. Write a draft of the skill
3. Create a few test prompts and run claude-with-access-to-the-skill on them
4. Help the user evaluate the results both qualitatively and quantitatively
   - While the runs happen in the background, draft some quantitative evals if there aren't any (or modify existing ones). Then explain them to the user.
   - Use the `eval-viewer/generate_review.py` script to show the user the results, and also let them look at the quantitative evals
5. Rewrite the skill based on feedback from the user's evaluation of the results
6. Repeat until satisfied
7. Expand the test set and try again at larger scale

Your job when using this skill is to figure out where the user is in this process and then jump in at the right place.

Of course, always be flexible — if the user says "I don't need to run a bunch of evals", respect that.

After the skill is done, you can also run the skill description optimizer to improve triggering accuracy.

---

### Communicating with the user

The skill creator is liable to be used by people across a wide range of familiarity with coding jargon. Please pay attention to context cues to understand how to phrase your communication.

Default: avoid jargon. It's OK to briefly explain terms if in doubt. Specifically:
- "evaluation" and "benchmark" are borderline, but OK
- For "JSON" and "assertion" you want to see serious cues from the user that they know what those things are

---

### Creating a skill

#### Capture Intent

Start by understanding the user's intent. The current conversation might already contain a workflow to formalize. Questions to ask:
- What should this skill enable Claude to do?
- When should this skill trigger? (what user phrases/contexts)
- What's the expected output format?
- Should we set up test cases to verify the skill works?

#### Interview and Research

Proactively ask questions about edge cases, input/output formats, example files, success criteria, and similar existing skills.

Check available MCPs — if useful for research (searching docs, finding similar skills, looking up best practices), use them proactively.

#### Write the SKILL.md

Based on the user interview, fill in these components:
- **name**: Skill identifier
- **description**: When to trigger, what it does. This is the primary triggering mechanism — include both what the skill does AND when to use it
- **compatibility**: Required tools, dependencies (optional, rarely needed)
- The rest of the skill content

---

### Skill Writing Guide

#### Anatomy of a Skill

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/    - Executable code for deterministic/repetitive tasks
    ├── references/ - Docs loaded into context as needed
    └── assets/     - Files used in output (templates, icons, fonts)
```

#### Progressive Disclosure

Skills use a three-level loading system:
- **Metadata** (name + description): Always in context (~100 words)
- **SKILL.md body**: In context whenever skill triggers (<500 lines ideal)
- **Bundled resources**: As needed (unlimited; scripts can execute without loading)

Key patterns:
- Keep SKILL.md under 500 lines; if approaching the limit, add an additional layer of hierarchy
- Reference files clearly from SKILL.md with guidance on when to read them
- For large reference files (>300 lines), include a table of contents

**Domain organization** — when a skill supports multiple domains/frameworks, organize by variant:

```
cloud-deploy/
├── SKILL.md (workflow + selection)
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```

Claude reads only the relevant reference file.

#### Principle of Lack of Surprise

Skills must not contain malware, exploit code, or any content that could harm users or systems.

#### Writing Patterns

Prefer using the imperative form in instructions.

**Defining output formats:**
```markdown
Report structure
ALWAYS use this exact template:
[Title]
Executive summary
Key findings
Recommendations
```

**Examples pattern:**
```markdown
Commit message format
Example 1:
Input: Added user authentication with JWT tokens
Output: feat(auth): implement JWT-based authentication
```

#### Writing Style

Try to explain to the model WHY things are important in lieu of heavy-handed MUSTs. Use theory of mind — today's LLMs are smart and respond well to reasoning.

---

### Test Cases

After writing the skill draft, come up with 2-3 realistic test prompts. Save to `evals/evals.json`. Don't write assertions yet — just the prompts.

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": "...",
      "prompt": "User's task prompt",
      "expected_output": "Description of expected result",
      "files": []
    }
  ]
}
```

See `references/schemas.md` for the full schema (including the `assertions` field, which you'll add later).

---

### Running and evaluating test cases

This section is one continuous sequence — don't stop partway through. Do NOT use `/skill-test` or any other testing shortcut.

Put results in `<skill-name>-workspace/` as a sibling to the skill directory, organized by iteration:

```
<skill-name>-workspace/
├── iteration-1/
│   ├── eval-0/
│   └── eval-1/
└── iteration-2/
    ├── eval-0/
    └── eval-1/
```

#### Step 1: Spawn all runs (with-skill AND baseline) in the same turn

For each test case, spawn two subagents in the same turn — one with the skill, one without.

**With-skill run:** Execute with the skill path and eval prompt; save to `with_skill/outputs/`

**Baseline run:**
- Creating a new skill: no skill at all, save to `without_skill/outputs/`
- Improving an existing skill: the old version, save to `old_skill/outputs/`

Write an `eval_metadata.json` for each test case:
```json
{
  "eval_id": "...",
  "eval_name": "descriptive-name-here",
  "prompt": "The user's task prompt",
  "assertions": []
}
```

#### Step 2: While runs are in progress, draft assertions

Don't just wait — draft quantitative assertions in `evals/evals.json`. Good assertions are objectively verifiable and have descriptive names.

#### Step 3: As runs complete, capture timing data

When each subagent task completes, save `total_tokens` and `duration_ms` immediately to `timing.json`:
```json
{
  "total_tokens": 84852,
  "duration_ms": 23332,
  "total_duration_seconds": 23.3
}
```

This is the only opportunity to capture this data — it comes through the task notification and isn't accessible afterward.

#### Step 4: Grade, aggregate, and launch the viewer

1. Grade each run with a grader subagent (see `agents/grader.md`)
2. Aggregate: `python -m scripts.aggregate_benchmark workspace/iteration-N --skill-name name`
3. Do an analyst pass (see `agents/analyzer.md`)
4. Launch the viewer:
```bash
nohup python <skill-creator-path>/eval-viewer/generate_review.py \
  workspace/iteration-N \
  --skill-name "my-skill" \
  --benchmark workspace/iteration-N/benchmark.json \
  >/dev/null &
VIEWER_PID=$!
```

#### Step 5: Read the feedback

When the user tells you they're done, read `feedback.json`. Empty feedback means fine.

Kill the viewer server when done: `kill $VIEWER_PID >/dev/null`

---

### Improving the skill

- **Generalize from the feedback.** Don't overfit to specific test cases.
- **Keep the prompt lean.** Remove things that aren't pulling their weight.
- **Explain the why.** Today's LLMs respond well to reasoning.
- **Look for repeated work across test cases.** Factor out into `scripts/`.

Keep iterating until: user is happy / all feedback empty / no meaningful progress.

---

### Advanced: Blind comparison

For more rigorous comparison, use `agents/comparator.md` and `agents/analyzer.md`. Optional.

---

### Description Optimization

The `description` field is the primary mechanism that determines whether Claude triggers a skill.

1. Generate 20 trigger eval queries (should-trigger and should-not-trigger mix)
2. Review with user via `assets/eval_review.html`
3. Run optimization: `python -m scripts.run_loop --eval-set ... --skill-path ... --model ... --max-iterations 10 --verbose`
4. Apply `best_description` from JSON output to SKILL.md frontmatter

---

### Claude.ai Specific Notes

- **Running test cases:** No subagents available — test one at a time, read SKILL.md then execute manually
- **Reviewing results:** If can't open browser, use `--static <output_path>`
- **Benchmarking:** Skip quantitative benchmarking
- **Description optimization:** Skip (requires CLI tool `claude -p`)
- **Blind comparison:** Skip (requires subagents)

---

## 关键文件

| 文件 | 作用 |
|------|------|
| `agents/grader.md` | 如何评估 assertion 与输出 |
| `agents/comparator.md` | 盲 A/B 对比两个输出 |
| `agents/analyzer.md` | 分析某版本为何胜出 |
| `references/schemas.md` | evals.json、grading.json 等的 JSON 结构 |
