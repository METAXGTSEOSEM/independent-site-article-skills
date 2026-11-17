# 独立站文章生产与审核 Skill

一个主技能，协调研究、写作、事实核查、SEO／AI 搜索审核、指定 Humanizer 和独立终审。

适用于英文／中文独立站文章、B2B 采购指南、产品知识和已有文章优化。支持 WordPress、Shopify 等站点的文章交付，不自动接通或发布网站。

## Magpie 安装

1. 进入「技能 → 查找技能」。
2. 输入本仓库 GitHub 地址。
3. 只选择 `independent-site-article`。
4. 保留完整技能文件夹，包括 `references/`、`assets/`、`agents/`。
5. 选择实际使用的 Agent。

本仓库只有一个 `SKILL.md`。七个职责写在参考文件中，运行时由主助手委派，不需要再导入七份角色到全局指令。

仓库结构遵循标准技能目录。发布后会检查远程内容和隔离安装；未在你的 Magpie 界面完成实际导入操作。

## 必须准备的语言编辑技能

- 英文：安装 [blader/humanizer](https://github.com/blader/humanizer)，技能名 `humanizer`。
- 中文：安装 [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)，技能名 `humanizer-zh`。

本仓库不复制第三方技能正文。只写英文时需要英文技能，只写中文时需要中文技能。缺少对应技能会报告待处理，不能声称已完成指定审核。

可选：已有 `seo-content`、`seo-geo`、`seo-content-brief`、真实搜索或数据工具时按需调用。未接入付费服务也能基于公开资料工作，但不能编造搜索量和排名。

## 使用

每篇文章一个主对话，在可以读写项目文件的目录执行：

```text
使用 independent-site-article，完成本篇文章。
网站：
主题或固定标题：
语言和地区写法：
目标国家、读者：
B2B／B2C：
文章目的：
已有产品资料或原文：

先研究再撰稿，按指定 Humanizer 编辑，并由独立子代理终审。
保存来源、稿件版本和报告。
本次只交付文章，不上传或发布。
```

支持 `$independent-site-article` 的工具可直接点名；其他工具用技能名和自然语言请求即可，实际调用以宿主支持为准。

可委派时，主助手把 `references/roles.md` 中对应职责传给通用子代理。不能委派时交付草稿和自审报告，完整状态为“待独立终审”，不会假装独立审核已完成。

## 交付与边界

- 文章正文。
- H1、SEO title、摘要、slug、图片与内链建议。
- 事实来源、主张台账和固定版本审核。
- 网站未实测项与可选后续复盘计划。

政策基线核对日为 2026-11-17。每篇须重新核实相关官方资料，不能把基线视为永久最新。

不承诺排名、收录、AI 引用、涨粉或 AI 检测通过。安装技能不自动获得网站或账号权限。

## 文件

```text
skills/independent-site-article/
  SKILL.md
  agents/openai.yaml
  references/workflow.md
  references/roles.md
  references/policy-sources.md
  assets/brief.md
  assets/sources.csv
  assets/claims.csv
  assets/review-and-delivery.md
```

本仓库原创工作流采用 MIT 许可；第三方技能与官方资料的许可和权利归各自项目，见 [来源说明](THIRD_PARTY.md)。
