# Third-Party Notices

本仓库是基于以下两个开源项目的技术思路与机制进行的二次开发。
两个上游项目均采用 MIT License；本仓库未打包其源码文件，
复用的是其生成管线的输出结构与调研方法论。MIT License 要求在任何
实质部分中包含上游版权声明与许可声明，本文件即履行该义务。

## Distilly

- 上游仓库：<https://github.com/titanwings/distilly>
- 许可证：MIT License — Copyright (c) 2026 titanwings
- 前身：原「Colleague Skill / 同事 Skill」项目的后续项目
- 本项目中的复用：
  - `persona.md` / `work.md` 的分层文档结构（Layer 0-7、Agentic Protocol、能力层）
    由 Distilly 的 celebrity prompt 管线（`distilly.celebrity.v1` 预设）生成；
  - `manifest.json` / `meta.json` / `.build/meta.json` 的 schema、字段与产物清单
    机制来自 Distilly 的 `skill_writer`；
  - 调研汇总与结构自检调用了 Distilly 的 `merge_research.py` 与
    `quality_check.py`（--profile budget-friendly，13/13 PASS）；
  - `scripts/finalize_distilly_artifacts.py` 与
    `scripts/normalize_research_bullets.py` 是为适配 Distilly 产物而编写的本项目原创脚本。

## 女娲 · nuwa-skill

- 上游仓库：<https://github.com/alchaincyf/nuwa-skill>
- 许可证：MIT License — Copyright (c) 2026 Huashu（花叔）
- 本项目中的复用：
  - 六维度调研方法论：`references/research/` 下 01-writings / 02-conversations /
    03-expression-dna / 04-external-views / 05-decisions / 06-timeline
    的维度划分与笔记规范；
  - 人物 Skill 自检使用了其 `scripts/quality_check.py`（6/6 通过）；
  - 「本地语料优先、拒绝内容农场」的采集纪律。

## 原始素材（不在本仓库许可证覆盖范围内）

- 罗翔相关调研笔记的素材来自用户本地整理的 B 站「罗翔说刑法」公开视频字幕物料
  （132 份 markdown）。视频与字幕的原始版权归视频平台及权利人所有；
  本仓库发布的是基于公开内容的研究性提炼笔记，不主张对罗翔姓名、形象与
  言论的任何权利，本项目亦未获得罗翔本人授权或认可。
