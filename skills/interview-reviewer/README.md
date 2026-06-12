# Interview Reviewer Skill - 面试录音复盘

一个 Claude Code Skill，从面试录音转录文本出发，产出结构化复盘文档，帮助你真正提升面试能力（不是背答案）。

## 它能做什么

说 `面试复盘` 就会触发。你提供面试录音的转录文本，它会自动生成一份完整的复盘文档：

| Part | 内容 | 解决什么问题 |
|------|------|------------|
| Part 1 | QA问答对 | 清洗口语、切分问答、标注严重度 |
| Part 2 | 正确答案教学 | 对答得最差的3-5题做深度知识教学 + senior级示例 |
| Part 3 | 思维路径 | 训练听到问题后的条件反射（Step 1→2→3→4） |
| Part 4 | 追问防御链 | 预测面试官追问 + 思路关键词 |
| Part 5 | 差距分析 | 项目深挖 + 知识盲区 + JD匹配 + 训练任务 + 自查清单 |

核心特点：
- **教学优于话术** — 教你理解知识本质，不是给一段话让你背
- **结合个人经历复盘** — 每条建议都要回到你的简历、真实项目、STAR故事、项目数据和目标岗位
- **项目文档是ground truth** — 所有答案来自你自己的项目文档，不编造
- **Senior级对标** — 每个弱题给出高级别回答示例 + 你当前level评级
- **所有训练任务都配参考答案** — 不是只列任务不给答案
- **三重审核** — 发布前检查可用性、真实性、知识库一致性

## 安装步骤

### Step 1：复制文件

```bash
# 把整个目录复制到你的 Claude Code skills 目录
cp -r interview-reviewer ~/.claude/skills/
```

### Step 2：配置个人信息

打开 `~/.claude/skills/interview-reviewer/SKILL.md`，搜索所有 `{{...}}` 占位符并替换为你的真实路径：

| 占位符 | 说明 | 示例 |
|--------|------|------|
| `{{OBSIDIAN_VAULT}}` | 你的 Obsidian vault 根目录 | `/Users/你/Documents/obsidian-vault` |
| `{{RESUME_PATH}}` | 你的简历文件路径（PDF/MD） | `/Users/你/Documents/简历.pdf` |
| `{{STAR_STORIES_PATH}}` | 你的STAR故事集路径（可选） | `/Users/你/Documents/STAR故事.md` |
| `{{TARGET_SALARY}}` | 你的目标年薪（万） | `40` / `55` / `70` |
| `{{TARGET_LEVEL}}` | 你的目标职级 | `P7` / `P6` / `senior` |
| `{{TARGET_ROLE}}` | 你的目标岗位类型 | `AI产品经理` / `后端工程师` / `数据分析师` |
| `{{LOCAL_FALLBACK_DIR}}` | 飞书不可用时的本地保存目录 | `/Users/你/Documents/面试复盘/` |

### Step 3：配置飞书发布（可选）

如果你用飞书，编辑 `references/feishu-publishing.md`，填入你的 lark-cli 配置。

如果不用飞书，skill会降级为保存本地 Markdown 文件。

### Step 4：注册你的项目

编辑 `references/project-registry.md`，按格式添加你的项目和文档路径。

### Step 5：配置知识库索引（可选）

如果你有 Obsidian 知识库，编辑 `references/knowledge-vault-index.md`，按格式添加你的知识域和文件路径。

没有 Obsidian 知识库也能用，skill 会用 WebSearch 补充知识。

## 依赖

- **Claude Code**（必须）
- **lark-cli**（可选，用于发布到飞书）— 没有的话会保存为本地文件
- **lark-shared skill**（可选，如果用飞书发布）— 处理飞书认证

## 文件结构

```
interview-reviewer/
├── SKILL.md                    ← 主文件（工作流定义）
└── references/
    ├── project-registry.md     ← 你的项目 → 文档路径映射
    ├── output-template.md      ← 飞书输出模板（色彩/结构）
    ├── feishu-publishing.md    ← 飞书发布配置
    └── knowledge-vault-index.md ← Obsidian知识库索引
```

## 使用方法

在 Claude Code 中直接说：

```
面试复盘
```

然后按提示依次提供：
1. 公司名
2. 讨论了哪些项目
3. 面试官角色（HR/直属leader/技术伙伴/高管）
4. 目标JD（推荐）
5. 面试日期
6. 转录文本（粘贴/文件路径/飞书链接）

## 适用岗位

虽然最初为 AI 产品经理面试设计，但核心工作流（QA切分 → 弱题教学 → 思维路径 → 追问防御 → 差距分析）适用于任何岗位。你只需要在 SKILL.md 中调整 `{{TARGET_ROLE}}` 和知识库索引即可。
