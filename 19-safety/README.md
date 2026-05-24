# 19-safety — LLM/Agent 安全 · 红队 · 防护

| 仓库 | 星 | 体量 | 抄什么 |
|---|---|---|---|
| 🥇 **[garak](./garak/)** | 6k★ | 14M / 331 py | NVIDIA 出品；**44 类 probe**（dan/jailbreak/leak/atkgen/promptinject 等）；红队事实标准；AGENTS.md |
| 🥈 **[NeMo-Guardrails](./NeMo-Guardrails/)** | 5k★ | 33M / 736 py | NVIDIA 对话防护轨；Colang DSL；运行时拦截 |
| **[presidio](./presidio/)** | 5k★ | 207M / 460 py | Microsoft PII 检测/脱敏（25+ 实体类型） |
| **[promptbench](./promptbench/)** | 3k★ | 4M / 58 py | Microsoft prompt 鲁棒性评测 |
| **[llm-attacks](./llm-attacks/)** | 4k★ | 0.8M / 21 py | Zico Kolter（CMU）GCG 攻击参考实现 |

## 抄作业重点
- **garak/probes/** 44 个类目 = 上线前红队回归套件骨架
- **NeMo-Guardrails/nemoguardrails/colang/** 对话防护 DSL 设计
- **presidio/presidio-analyzer/** PII 检测规则库
