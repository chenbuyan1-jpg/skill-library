# vibe-pm Roadmap

> 已完成 / 规划中 / 不会做 的 skill 全表

---

## 已完成 ✅

| Skill | 状态 | 用途 |
|---|---|---|
| `vibe-pm` | ✅ v1.0 | 方法论入口与索引 |
| `vibe-pm-define-done` | ✅ v1.0 | 完成定义器（项目第一步） |
| `vibe-pm-prd` | ✅ v2.0 | AI 可执行的 vibe coding PRD |

---

## 规划中 🔲（按优先级）

| 优先级 | Skill | 用途 | 预计工作量 |
|---|---|---|---|
| 🥇 高 | `vibe-pm-doc-audit` | 项目文档完备性审查（按规模 × 类型决定文档清单） | 3 小时 |
| 🥈 高 | `vibe-pm-ai-eval` | AI 产品评测体系（评测集 / 评测维度 / bad case 闭环） | 4 小时 |
| 🥉 中 | `vibe-pm-engineering-review` | 工程框架审查（钱学森工程控制论 6 维度） | 4 小时 |
| 中 | `vibe-pm-mvp-scope` | MVP 砍刀（决定 V1 / V2 / 永不做） | 2 小时 |

### 各 skill 的设计要点（待开发时参考）

**`vibe-pm-doc-audit`**
- 输入：项目描述 + 当前阶段
- 输出：必须的文档清单（按优先级）+ 缺失项 + 建议跳过的文档
- 核心：决策矩阵（项目规模 × 文档类型）
- 关键洞见：AI 产品有 3 类文档比传统重要（评测集/bad case 集/Agent 设计），有 1 类不那么重要（详细 UI 原型）

**`vibe-pm-ai-eval`**
- 输入：AI 产品类型（生成 / 决策 / 信息聚合 / Agent）
- 输出：评测集（30-100 条）+ 评测维度 + bad case 收集机制 + 迭代闭环 SOP
- 核心：覆盖 4 类样本（正向 / 边缘 / 失败 / 对抗）
- 反例：本次圆桌项目"卡帕西过度跳过"——一开始就该有 5 条@强制响应评测样本

**`vibe-pm-engineering-review`**
- 输入：项目代码 / 设计文档
- 输出：6 维度审查报告（闭环反馈 / 可观测 / 可控 / 稳定 / 解耦 / 熵增）
- 核心：钱学森工程控制论 → 软件项目映射

**`vibe-pm-mvp-scope`**
- 输入：完整功能清单
- 输出：3 列（绿 V1 必做 / 黄 V1 可选 / 红 V1 禁止）+ 决策依据
- 可与 `vibe-pm-prd` 的 M3 模块复用

---

## 不会做的 ❌

- ❌ `vibe-pm-traditional-prd` —— vibe-pm 不替代传统 PRD 流程，传统 PRD 用 `prd-generator` 等其他 skill
- ❌ `vibe-pm-coding-tutor` —— vibe-pm 不教 PM 写代码，只教 PM 让 AI 写代码
- ❌ `vibe-pm-handoff-to-engineer` —— vibe coding 的 PM 不交接给工程师，交接给 AI
- ❌ `vibe-pm-budget-planning` —— 预算和资源规划不在 vibe-pm 范围

---

## 何时启动新 skill 开发？

**触发条件**（满足任一即启动）：
1. 同一类问题踩坑 ≥ 3 次（说明缺乏方法论）
2. 团队多个 PM 反馈"这一步我不知道怎么做"
3. 现有 skill 在某场景下无能为力，且场景重复出现 ≥ 5 次

**写新 skill 的最佳时机**：你刚踩完坑的那一刻——记忆最鲜活，反例最具体。

---

## 版本历史

| 日期 | 版本 | 变更 |
|---|---|---|
| 2026-05-04 | v1.0 | 首次发布：vibe-pm + vibe-pm-define-done + vibe-pm-prd |

> 后续每次大改在这里记录。
