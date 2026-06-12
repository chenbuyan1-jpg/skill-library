---
name: vibe-pm
description: Vibe Coding 产品方法论的入口与总览。仅当用户明确询问"vibe-pm 是什么"、"vibe coding 方法论"、"我该用哪个 vibe-pm skill"、"新人想了解整套体系"时触发。具体的项目动作（定义完成、写 PRD、文档审查、工程审查、评测）请由对应的 vibe-pm-* 子 skill 处理，不要在这里替代它们工作。
---

# vibe-pm — Vibe Coding 产品方法论入口

这是一套 **给非工程师产品经理使用的、通过自然语言指挥 AI 写代码做产品** 的工作流方法论。

它**不是**：传统 PRD 写作流程、团队协作流程、给开发同事看的文档体系。
它**是**：把"产品想法"变成"AI 能直接执行的指令包"的标准化流水线。

---

## 当用户触发本 skill 时，你的工作是

1. **判断意图**：用户是想了解方法论本身？还是想立刻开始一个项目？
2. 如果是**了解方法论** → 在终端里展示下面的"方法论速览"
3. 如果是**立刻开始项目** → 引导到对应的子 skill（不要自己代劳）

---

## 方法论速览（展示给用户）

### 核心命题
> Vibe Coding ≠ 传统开发。**衡量标准是"AI 能否直接落地"，不是"开发同事能否理解"**。

### 7 条不可妥协的原则

1. **完成定义优先于功能定义**
2. **MVP 砍刀比 PRD 更值钱**
3. **真实世界的样子 > 文档里的描述**
4. **闭环反馈是 AI 产品的命脉**
5. **文档不是越多越好，而是要"可被引用"**
6. **决策的颗粒度和时间感要匹配**
7. **memory（人和项目的偏好）要随手沉淀**

### Skill 链（按使用顺序）

```
   想法
    ↓
[vibe-pm-define-done]  ← 第一道闸门：先锁完成标志
    ↓ 输出：完成定义卡
[vibe-pm-prd]          ← 写 AI 能执行的 PRD
    ↓ 输出：PRD/ 目录（5 模块解耦）
   开发  ← AI/工程师/自己写
    ↓
[vibe-pm-doc-audit]    ← (规划中) 文档完备性审查
[vibe-pm-engineering-review]  ← (规划中) 工程完备性审查
[vibe-pm-ai-eval]      ← (规划中) AI 评测体系
    ↓
   上线 → 迭代闭环
```

---

## 决策树：用户应该用哪个 skill？

| 用户说什么 | 用哪个 |
|---|---|
| "我有个想法 / 想做一个 / 立项" | `vibe-pm-define-done` |
| "完成的标准是什么 / 怎么算做完" | `vibe-pm-define-done` |
| "vibe coding PRD / 让 AI 写一个 / 写 PRD 给 AI 用" | `vibe-pm-prd` |
| "传统 PRD / 给开发同学看" | ❌ 不在 vibe-pm 范围（用 prd-generator 等其他 skill）|
| "想了解 vibe-pm 是什么 / 整套体系" | 本 skill（你正在看的）|
| "已有 PRD 想审查文档是否齐全" | (规划中) `vibe-pm-doc-audit` |
| "审查代码框架是否健全" | (规划中) `vibe-pm-engineering-review` |
| "AI 产品的评测体系" | (规划中) `vibe-pm-ai-eval` |

---

## 当用户不确定该用哪个时

按这个流程提问：

```
1. 你现在在项目的什么阶段？
   - 还没动手 → vibe-pm-define-done
   - 已经定好要做什么，要写规格 → vibe-pm-prd
   - 已经在改代码 → (engineering-review 规划中)

2. 你的目标是什么？
   - 写一份 AI 能直接照着做的文档 → vibe-pm-prd
   - 锁定项目边界，避免做着做着失控 → vibe-pm-define-done
```

---

## 不要在本 skill 里做的事

- ❌ 直接帮用户写 PRD（应该转 `vibe-pm-prd`）
- ❌ 直接帮用户列功能清单（应该转 `vibe-pm-define-done`）
- ❌ 把传统 PRD 流程搬过来（vibe-pm 不是传统 PRD 流程的别名）

---

## 相关材料（同一目录下）

- `README.md` — 给 PM 同事的入口文档（人读的）
- `METHODOLOGY.md` — 完整方法论（含"这套方法论是怎么来的"的反例库）
- `ROADMAP.md` — 已完成 / 规划中的 skill 清单
- `shared/` — 跨 skill 共享的资料（评测样例、案例库等）
