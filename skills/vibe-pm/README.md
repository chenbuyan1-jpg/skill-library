# vibe-pm — 给 PM 同事的入口文档

> 这是一套 **给非工程师产品经理** 使用的方法论 ——
> 通过自然语言指挥 AI 写代码做产品的标准化工作流。

---

## 这是什么？

如果你是产品经理，并且想要：

- 用 AI（Claude Code / Cursor / 类似工具）**直接**把想法变成能跑的产品
- **不依赖**研发团队的资源就能验证想法
- 让你的 PRD 真的能被 AI 落地（而不是 AI 看完反问你 100 个问题）

那这套 skill 就是给你写的。

---

## 当前包含的 skill

| Skill | 状态 | 何时使用 |
|---|---|---|
| `vibe-pm`（本 skill） | ✅ 入口 | 想了解整套方法论时 |
| `vibe-pm-define-done` | ✅ 可用 | **任何项目的第一步** ——锁定"完成"标志 |
| `vibe-pm-prd` | ✅ 可用 | 把想法转成"AI 能直接执行"的 PRD |
| `vibe-pm-doc-audit` | 🔲 规划中 | 项目文档完备性审查 |
| `vibe-pm-engineering-review` | 🔲 规划中 | 工程框架审查（钱学森工程控制论） |
| `vibe-pm-ai-eval` | 🔲 规划中 | AI 产品评测体系 |
| `vibe-pm-mvp-scope` | 🔲 规划中 | MVP 砍刀（决定 V1/V2/永不做） |

完整规划见 `ROADMAP.md`。

---

## 第一次使用？跟着做这 3 步

### 第 1 步：理解整套方法论
对 Claude 说：**"vibe-pm 是什么？"**
（会触发 `vibe-pm` skill，给你看方法论速览）

### 第 2 步：开始你的第一个项目
对 Claude 说：**"我有个想法，[一句话描述你的想法]"**
（会触发 `vibe-pm-define-done` skill，5 个问题帮你锁定"完成"是什么）

### 第 3 步：把锁定的想法写成 PRD
对 Claude 说：**"开始写 vibe coding PRD"**
（会触发 `vibe-pm-prd` skill，4 阶段交互式产出 PRD 文件夹）

---

## 给团队同事的 1 分钟介绍

> "你以前写 PRD 是给开发同学看的对吧？vibe-pm 不是。
> 它教你写一种特殊的 PRD —— **写给 AI 看的**。
> 你想做一个 idea，不需要去排研发资源，
> 你直接对 Claude/Cursor 说 '按这份 PRD 实现'，
> AI 就能 1-3 天给你跑出 demo。
>
> 这套 skill 帮你把'随便说说'的想法
> 变成 AI 能照着干活的'指令包'。"

---

## 这套方法论从哪来的？

来自一次真实项目的复盘：一个非工程师产品经理用一晚上做出了一个本地 AI 圆桌讨论工具。
那次过程里踩了 10 个坑（详见 `METHODOLOGY.md` 的"反例库"），
这套 skill 是从那 10 个坑里提炼出来的。

**反例 > 正例。** 每个 skill 里都有"同事最常踩的坑"段落，把别人踩过的坑给你避开。

---

## 持续优化

- 每用一次，记录一条**触发场景 + 是否有效**
- 每月复盘：哪些 skill 没人用？哪些用错了？
- 季度合并/修剪，避免 skill 库膨胀
- 你也欢迎贡献新的 skill —— 用 `skill-creator` 工具

---

## 文件结构

```
~/.claude/skills/
├── vibe-pm/                          ← 你正在看的封装层
│   ├── SKILL.md                      ← Claude 触发时读的方法论入口
│   ├── README.md                     ← 你正在看的（人读的）
│   ├── METHODOLOGY.md                ← 完整方法论 + 反例库
│   ├── ROADMAP.md                    ← skill 规划路线图
│   └── shared/                       ← 跨 skill 共享资料
├── vibe-pm-define-done/              ← 实际可触发的 skill
│   ├── SKILL.md
│   └── references/
└── vibe-pm-prd/                      ← 实际可触发的 skill
    ├── SKILL.md
    └── references/
```

---

## 反馈与共建

每次踩坑都是 skill 优化的最佳时机。把你的踩坑案例直接加到 `METHODOLOGY.md` 的"反例库"段落里，下一个用的人就能避开。
