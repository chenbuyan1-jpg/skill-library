# 飞书发布配置

面试复盘文档通过 lark-cli 发布到用户的个人知识库。

> **如果你不用飞书**，skill 会自动降级为保存本地 Markdown 文件到 `/Users/chenbuyan/Documents/面试`。以下配置可以跳过。

---

## lark-cli 配置

> 首次使用前，按你的飞书应用配置填写以下信息。

- appId: `{{YOUR_LARK_APP_ID}}`
- 用户身份: `{{YOUR_LARK_USER_ID}}`
- 始终使用 `--as user` 确保文档归属用户

### 如何获取这些信息

1. 安装 lark-cli：参考 https://github.com/nicepkg/lark-cli
2. appId：在飞书开放平台创建应用后获得
3. 用户身份：运行 `lark-cli auth login` 后获取 user_id

## 发布目标

- 目标空间：`my_library`（用户个人知识库）
- 文档标题格式：`面试复盘 - {公司名} - {YYYY-MM-DD}`

## 发布流程

### Step 1：创建文档（首段内容）

```bash
lark-cli docs +create \
  --title "面试复盘 - {公司名} - {YYYY-MM-DD}" \
  --wiki-space my_library \
  --markdown "{第一段内容：复盘概览+JD}" \
  --as user
```

返回值中提取 `doc_id` 用于后续追加。

### Step 2：分段追加

```bash
lark-cli docs +update \
  --doc "{doc_id}" \
  --mode append \
  --markdown "{后续段落内容}" \
  --as user
```

重复执行直到所有段落追加完毕。

### Step 3：验证

```bash
lark-cli docs +fetch --doc "{doc_id}" --as user
```

检查内容完整性和格式渲染。

## Lark Markdown 限制

在编写内容时必须遵守以下限制，否则API会报错：

### callout 内支持的元素

- 文本（段落、加粗、斜体、链接）
- 列表（有序、无序）
- 代码块

### callout 内不支持的元素（会导致API报错）

- 表格 → 移到callout外面
- 分割线（---）→ 删除或移到callout外面
- 标题（#/##/###）→ 移到callout外面
- 嵌套callout → 不支持

### 其他注意事项

- `---` 不能出现在markdown内容的最开头（会被CLI解析为flag）
- 代码块用 ` ```plaintext {wrap} ``` ` 格式可以自动换行
- 表格列对齐用 `|---|` 即可，不需要精确对齐

## 错误处理

| 错误 | 处理方式 |
|------|---------|
| 认证过期 | 运行 `lark-cli auth login --scope "wiki:node:read docx:document:write"` |
| callout内不支持的元素 | 将表格/分割线移到callout外面后重试 |
| 内容过长导致超时 | 拆分为更小的段落分别追加 |
| lark-cli完全不可用 | 降级：保存为本地文件 `/Users/chenbuyan/Documents/面试/面试复盘_{公司}_{日期}.md` |
