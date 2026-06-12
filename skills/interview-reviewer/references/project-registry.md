# 项目文档注册表

用户新增项目时更新此文件。Skill 每次执行时读取本文件获取项目列表和文档路径。每次复盘还应读取 `user-profile.md` 作为个人画像。

---

## shared — 共享参考（每次面试复盘都读取）

- 用户画像: /Users/chenbuyan/.agents/skills/interview-reviewer/references/user-profile.md
- 简历: /Users/chenbuyan/Documents/陈纪富_AI产品经理简历_优化版_1.docx
- 本地复盘输出目录: /Users/chenbuyan/Documents/面试

---

## 爆款文案 — 图书短视频爆款文案 LLM 生成系统

面向图书内容电商编导团队的 LLM + RAG 文案生成系统。核心叙事是：把图书卖点、人群痛点、脚本结构和投放反馈沉淀成可复用的 AI 内容生产系统。

当前已知材料：

- /Users/chenbuyan/Documents/陈纪富_AI产品经理简历_优化版_1.docx
- /Users/chenbuyan/.agents/skills/interview-reviewer/references/user-profile.md

待补材料：

- PRD / 需求文档
- RAG 知识库结构说明
- Prompt / Agent 编排说明
- 评测 SOP / bad case 归因表
- 典型文案案例：通用模型 bad case、优化后 good case、人工修改版本、最终投放版本
- 数据口径说明：15→30/40、7%/8%、GMV+30%、年节省50万+ 分别如何统计

匹配关键词：爆款文案、文案生成、RAG、编导、童书、图书、Coze、Dify、卖点、转化率、GMV、DeepSeek、Prompt

---

## 主图详情页 — 电商货架主图与详情页多 Agent 智能生成系统

面向内容电商货架场景的多 Agent 主图/详情页生成系统。核心叙事是：把文案生成、图片生成、布局生成、合规审核和质量评估整合成可控生产链路。

- /Users/chenbuyan/Documents/项目梳理/prd-电商AI主图生成系统/v1.0-PRD-电商AI主图生成系统.md
- /Users/chenbuyan/Documents/项目梳理/prd-电商AI主图生成系统/changelog.md
- /Users/chenbuyan/Documents/项目梳理/prd-电商AI主图生成系统/wiki-index.md
- /Users/chenbuyan/Documents/项目梳理/business-flow-diagrams/ecommerce-ai-business-flow.mmd
- /Users/chenbuyan/Documents/项目梳理/agent-flow-diagrams/six-agent-orchestration-flow.mmd
- /Users/chenbuyan/Documents/项目梳理/architecture-diagrams/ecommerce-ai-image-architecture.mmd
- /Users/chenbuyan/Documents/项目梳理/architecture-diagrams/ecommerce-ai-image-architecture.png

匹配关键词：主图、详情页、货架、电商AI主图、AIGC图片、多Agent、商品保真、合规审核、质量评分、BadCase、SDXL、FLUX、ControlNet

---

## 视频号起盘 — 视频号教辅电商 0-1 起盘项目

从 0 到 1 搭建教辅图书视频号内容电商团队和投放链路。核心叙事是：内容策略、选品、投放、团队 SOP、AI 工具赋能共同验证商业模式。

当前已知材料：

- /Users/chenbuyan/Documents/陈纪富_AI产品经理简历_优化版_1.docx
- /Users/chenbuyan/.agents/skills/interview-reviewer/references/user-profile.md

待补材料：

- 账号定位 / 内容策略文档
- 选品逻辑文档
- 运营 SOP
- 投放复盘 / ROI 数据口径
- AI 工具赋能流程说明

匹配关键词：视频号、教辅、电商起盘、运营负责人、投放、ROI、月消耗、选品、内容策略、团队搭建、SOP

---

## 如何新增项目

在上方添加新的 `## key — 项目名` 段落，列出所有相关文档的绝对路径（每行一个）。

推荐为每个项目准备：

- PRD / 需求文档
- 业务流程 / 用户流程
- 架构设计 / Agent 编排图
- 评测 / 测试方案
- 数据口径说明
- STAR 故事和追问题库
