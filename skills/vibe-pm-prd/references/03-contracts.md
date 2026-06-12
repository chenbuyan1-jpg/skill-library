# M4 数据与契约 · 模板

> 输出文件：`PRD/03-contracts.md`
> 用途：把数据模型 + 接口契约 + (AI 产品) prompt 契约 用 AI 能解析的结构化方式定义

---

## 模板

```markdown
# 数据与契约

## 4.1 数据实体

| 实体 | 字段 | 类型 | 必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| {{Entity}} | {{field}} | {{string/int/datetime/bool/json}} | {{✓/✗}} | {{default}} | {{note}} |

## 4.2 实体关系

{{ER 描述或文字关系链。例如：}}
- User 1—N Discussion
- Discussion N—M Agent (通过 DiscussionAgent 关联表)
- Discussion 1—N Message

## 4.3 接口契约

### 4.3.1 API / Route 列表

| 接口 | 方法 | 输入 | 输出 | 错误码 |
|---|---|---|---|---|
| {{/api/xxx}} | {{POST}} | {{input schema}} | {{output schema}} | {{401, 413, 500}} |

### 4.3.2 屏幕路由（前端）

| 路由 | 用途 | 关键 state |
|---|---|---|
| {{/}} | {{首页}} | {{...}} |

## 4.4 [AI 产品独有] Prompt 契约

### Agent / Prompt N: {{名称}}

- **System prompt**:
  \`\`\`
  {{完整可复制的文本}}
  \`\`\`
- **输入变量**: {{var1: string, var2: number, ...}}
- **输出格式**: {{JSON schema 或自然语言格式定义}}
- **温度**: {{0-2，常用 0.3-0.8}}
- **token 预算**: input ≤ {{N}}, output ≤ {{N}}
- **失败行为**: {{超时/超长/拒答/错误时怎么办}}
- **特殊规则**: {{如：禁止使用 [skip] / 当用户 @ 时强制响应 / 等}}
```

---

## 写作规则

### 数据表必含 5 列
**类型 / 必填 / 默认值** 是最常见的"忘了写"。每个字段都要齐全。

类型用通用名（不要绑定具体数据库）：
- 推荐：string / int / datetime / bool / json / text / float
- 避免：VARCHAR(255) / TIMESTAMPTZ / 等具体方言

### 接口契约要写错误码
- ❌ 只写 happy path
- ✅ 至少列 1-3 个最常见的错误码（401 / 413 / 500 / 400）

### Prompt 写完整可复制版本
**这是 AI 产品和传统产品最大的区别。**

- ❌ "系统会有一段提示词来引导模型..."
- ✅ ```System prompt: 你是 X 的数字分身... [完整 400 字提示词] ```

### Prompt 必含 5 项硬指标
- 温度
- token 预算
- 失败行为（超时怎么办）
- 输出格式（JSON or 自然语言）
- 特殊规则（如有）

---

## 写作范例（节选）

```markdown
## 4.1 数据实体

| 实体 | 字段 | 类型 | 必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| Meeting | id | string | ✓ | uuid() | 主键 |
| Meeting | title | string | ✓ | - | 用户填写 |
| Meeting | created_at | datetime | ✓ | now() | |
| Meeting | transcript | text | ✗ | null | 转写后填入 |

## 4.4 Prompt 契约

### Agent: 纪要生成器
- **System prompt**:
  \`\`\`
  你是会议纪要专家。请将下面的会议转写文本整理为四段式纪要：
  1. 议题：列出 3-7 个，每条含发言人
  2. 决议：明确的"X 决定 Y"格式
  3. 行动项：每条 markdown checkbox，含 [负责人] [deadline]
  4. 待跟进：未明确结论的开放问题

  输出 JSON: {topics: [...], decisions: [...], actions: [...], follow_ups: [...]}
  不允许编造原文没有的内容。
  \`\`\`
- **温度**: 0.3
- **token 预算**: input ≤ 16k, output ≤ 2k
- **失败行为**: 返回 {error: "..."}, 不输出半成品
```

---

## 自查（M4 部分 4 项）

- [ ] 字段表有：类型 / 必填 / 默认值
- [ ] 接口契约写了错误码（不只 happy path）
- [ ] 若 AI 产品：prompt 是完整可复制版本，不是描述
- [ ] 若 AI 产品：温度 / token / 失败行为齐全
