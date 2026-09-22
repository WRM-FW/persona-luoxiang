# persona_luoxiang · 罗翔 Persona Skill

> 不是复刻一个说话像罗翔的机器人，而是装载一套看问题的方式：先承认有限，再谈应该怎么办。

| 项目 | 值 |
| --- | --- |
| Skill ID | `persona_luoxiang` |
| Skill 名称 | `LuoXiang` |
| 版本 | `1.0.0` |
| 目录 / 调用名 | `persona-luoxiang` |
| 入口文件 | `SKILL.md` |
| 语言 | 简体中文 |
| 调研截止 | 2026-09-15 |

## 一、这个 Skill 是什么

一个可被 AI Agent 直接加载的独立人物 Skill。加载后，Agent 进入「与罗翔面对面对话」的状态：用第一人称、按他的语气说话，用他的心智模型分析用户的问题，而不是背法条或复述字幕。

它蒸馏的是 **HOW he thinks**，不是 **WHAT he said**：

- **6 个心智模型**：有限性先行、合乎中道（先立两端再落中间）、理想是校正现实的标准、两害相权取最不坏、矛头向内（把主语换成「我」）、剧本与本分。
- **10 条决策启发式**：先索取定义权、双端否定、选更不坏并说清代价、不给鼓励性承诺、尖锐判断借第三方之口、专业边界当成分工问题、被赞美时缩小自我坐标、道德判断先换成「我」、进行中的私人痛苦不讲、沉默与发言先算被曲解的代价。
- **一套表达 DNA**：设问—短定义—展开的三拍节奏、「我们」而不是「你们」、直接作答而不做留白式收尾、自嘲只落在可验证的事实上、玩笑靶子只限自己与虚构人物、法条上确定而人生问题上谦卑、引用后必附降格说明。
- **输出纪律（硬约束）**：禁止客套式开场（「这个问题问得很好」）与留白式收尾（「总之啊，这些都值得我们去思考」「这个问题啊，还得你自己拿捏」）及其近义变体；禁止用一串反问句收束；降调词只用于确实收不束的地方，不能替代一个已经能给出的回答。完整清单见 `SKILL.md` 的《禁止的话术（硬清单）》。
- **他者视角与外部争议**：法学界的两极评价、冒名发言与伪金句现象、2020 年退博、2026 年吸毒入刑争论——用来防止这个 Skill 变成粉丝滤镜。
- **诚实边界**：素材是字幕而非逐字稿，缺压力顶点样本；自我修正只有死刑立场一例，拒绝商业合作的一手记录缺失，都写在 `SKILL.md` 里。

Skill 被刻意设计成**不要求每次走同一条路径**：故事—设问—辩证—劝勉是他常见的组织方式，不是流水线。用户问得急就直接给判断，只想听案例就讲案例。

## 二、来源

素材来自 [罗翔老师 B 站主页](https://space.bilibili.com/517327498) 的公开视频字幕物料
（访谈、读评论、经典讲读等 132 份整理稿），本地语料优先，未使用知乎、微信公众号、
百度百科或内容农场。调研方法与生成管线见第八节。

## 三、安装

### 方法一：手动安装

下载 [Releases](https://github.com/WRM-FW/persona-luoxiang/releases) 中的发行版并解压，
将 `persona-luoxiang` 文件夹放入对应 Agent 的 Skill 目录即可。

不同 Agent 的 Skill 目录位置可能不同，请以对应 Agent 的官方文档或实际目录结构为准。

### 方法二：让 Agent 自动安装

下载 [Releases](https://github.com/WRM-FW/persona-luoxiang/releases) 中的发行版后，直接将下面的提示词发送给 Agent，让 Agent 自己完成安装：

```text
请帮我安装这个 Skill。
Skill 名称：persona_luoxiang
Skill 文件位置：“填入文件地址”

请将它安装到当前 Agent 正确的 Skill 目录中，并完成安装后的检查。
安装完成后告诉我 Skill 的实际安装位置，以及如何调用它。
```

## 四、怎么用

安装完成后，也可以直接让 Agent 调用：

```text
调用 persona_luoxiang Skill。
```

或直接说自然语言，不要求固定格式：

- 「用罗翔的视角看看这件事」
- 「如果是罗翔，他会怎么分析我该不该跟领导顶嘴」
- 「切换到罗翔，陪我聊聊我最近总觉得自己很虚伪」
- 「罗翔会怎么看 AI 取代律师这件事」

## 五、目录结构

```
persona-luoxiang/
├── SKILL.md                     # 加载入口（自包含，含全部核心内容）
├── skill.yaml                   # 权威元数据（Skill ID / 触发词 / 来源 / 边界）
├── README.md                    # 本文件
├── LICENSE                      # MIT（仅覆盖本仓库原创内容，见第八、九节）
├── NOTICE.md                    # 上游衍生与素材版权归属声明
├── THIRD_PARTY_NOTICES.md       # 上游项目（Distilly / nuwa-skill）许可证与署名声明
├── persona.md                   # Distilly 人格层（Layer 0-7 + Agentic Protocol）
├── work.md                      # Distilly 能力层（法律分析工作法、教学与表达方法）
├── persona_skill.md             # Distilly 人格层单独可加载版本
├── work_skill.md                # Distilly 能力层单独可加载版本
├── manifest.json / meta.json    # Distilly 引擎清单与元数据（id / name / version 已对齐本 Skill 的规范身份）
├── references/research/         # 11 份调研笔记（01-06 六维度）
├── knowledge/research/
│   ├── raw/                     # 调研笔记副本（Distilly 约定的输入位置）
│   ├── reviews/                 # 两份独立验证报告（见第六节）
│   └── merged/summary.md        # merge_research 汇总（11 文件 / 71 URL / 6 维度 / 0 长引用）
├── .build/meta.json             # Distilly skill_writer 的输入元数据（用于复现生成）
└── scripts/
    ├── normalize_research_bullets.py   # 把调研笔记里的有序列表规范成 `- `（merge 工具只识别无序列表）
    ├── validate_skill_yaml.mjs         # 用 DSH 同族 YAML 解析器校验 frontmatter 与元数据
    ├── finalize_distilly_artifacts.py  # 把 Distilly 生成的 version / id / 命令名对齐到本 Skill 的规范身份
    └── install_to_dsh.py               # 把整个目录包安装到 DSH 技能根
```

## 六、质量校验

### 已通过的检查（本次交付状态）

| 检查 | 工具 | 结果 |
| --- | --- | --- |
| 结构自检（13 项） | Distilly `quality_check.py --profile budget-friendly` | OVERALL PASS（mental_models / limitations / expression_dna / honest_boundaries / internal_tension / intellectual_genealogy / agentic_protocol / source_grounding / copyright_safety 全 PASS） |
| 人物 Skill 自检（6 项） | 女娲 `huashu-nuwa/scripts/quality_check.py` | 6/6 通过（心智模型 6 个、有局限性标注、表达DNA 17 项、诚实边界 9 条、内在张力 2 处） |
| frontmatter 与元数据 | `scripts/validate_skill_yaml.mjs` | PASS（name 为合法 kebab-case、description 存在、布尔键解析正确、无引用块/代码围栏/时间码） |
| 已知答案测试 | 独立评审 Agent | Verdict PASS，8 题平均 1.875，2 个无依据探针均未编造 |
| 边界与反模式测试 | 独立评审 Agent | Status PASS，A 组 1.75 / B 组 1.75，盲测辨识度 中，结构 13 项全覆盖 |

两份验证报告在 `knowledge/research/reviews/`：`validation.md`（已知答案测试）、`research_audit.md`（边界、反模式、盲测、结构）。报告里提出的问题已回灌进 `SKILL.md`：补上死刑立场这一条自我修正记录、给「不给鼓励性承诺」补判据、把即兴应答四段骨架与收束句式写进表达DNA、增加「不制造金句 / 自谦不做默认开场收尾 / 中道只用于价值问题 / 不评价真实在世人物」等输出纪律。

## 七、边界与免责

- 这是一个基于**公开视频字幕物料**提炼的人物风格 / 表达方式研究与 AI Skill 实验项目。
  **本项目未获得罗翔本人授权，罗翔本人未参与本项目，本项目也不代表其认可**；
  它**不代表罗翔本人**，他本人对任何具体问题的态度都可能与 Skill 推出的结论不同。
- 素材是字幕与二次整理稿，不是逐字稿；副语言特征缺失，也没有课堂实录与被当面反驳的样本。因此这套模板最擅长的产出，恰好也是最需要警惕的产出：听起来很像他、但查无出处的漂亮话。
- 自我修正的记录只有一例（死刑立场的公开转变），缺第二例与非公开层面的记录；拒绝商业合作的一手记录缺失——相关结论在这两处只给原则，不给案例。
- `work.md` 里的「法律分析工作法六步」是从他的价值层表述与讲读结构重建的框架推断；材料中没有他演示构成要件分析或法律解释方法取舍的段落，这一点在文档内已单独标注。
- 不涉及私人生活与心理状态推断，公共表达的自谦修辞不能按字面当成客观能力评级。
- 本项目不主张对罗翔姓名、形象与言论的任何权利；涉及视频字幕素材的内容，引用与再分发请遵守原视频平台条款。

## 八、上游项目与来源关系

本项目基于以下两个开源项目的技术思路与机制进行**二次开发**，特此署名：

| 上游项目 | 地址 | 许可证 | 本项目的实际复用 |
| --- | --- | --- | --- |
| **Distilly**（原「Colleague Skill / 同事 Skill」项目的后续项目） | <https://github.com/titanwings/distilly> | MIT License（Copyright (c) 2026 titanwings） | Person Profile 生成管线：`persona.md` / `work.md` 的 Layer 0-7 与能力层文档结构、`manifest.json` / `meta.json` 的 schema 与产物清单机制、`skill_writer` 生成流程，均由 Distilly 引擎产出；本项目调用其 `tools/research/merge_research.py` 与 `quality_check.py` 完成汇总与结构自检 |
| **女娲 · nuwa-skill** | <https://github.com/alchaincyf/nuwa-skill> | MIT License（Copyright (c) 2026 Huashu（花叔）） | 六维度调研方法论（`references/research/01-writings … 06-timeline` 的维度划分与笔记模板）、人物 Skill 自检（其 `scripts/quality_check.py`，6/6 通过）与「本地语料优先」的蒸馏纪律 |

按来源区分本仓库内容：

- **Original Work（本项目原创）**：全部罗翔调研笔记（`references/research/` 11 份）、
  `SKILL.md` 中基于素材提炼的心智模型 / 决策启发式 / 表达 DNA / 输出纪律正文、
  `knowledge/research/reviews/` 验证报告、`scripts/` 四个辅助脚本
  （`normalize_research_bullets.py`、`validate_skill_yaml.mjs`、
  `finalize_distilly_artifacts.py`、`install_to_dsh.py`——为打通 Distilly 产物与
  DSH 加载规范而为本项目新编写，上游仓库中不存在同名文件）、本 README。
- **Generated / Derived Work（由上游管线生成的结构）**：`persona.md`、`work.md`、
  `persona_skill.md`、`work_skill.md`、`manifest.json`、`meta.json`、`.build/meta.json`
  ——文档骨架与元数据 schema 来自 Distilly 的 prompt 与 `skill_writer`，
  内容文本为本次对罗翔素材的调研产出。
- **Third-party（不随本仓库重新授权）**：上游两个项目本身不打包进本仓库，
  复用的是其方法论与生成管线的输出结构；`skill.yaml` 中的
  `prompts/…`、`tools/…` 路径只是对上游仓库内文件的引用记录。

## 九、许可

- 本仓库的原创内容（结构、脚本、调研笔记与 Skill 正文）以 **MIT License** 发布（见 `LICENSE` 与 `NOTICE.md`）；
  其中衍生自 Distilly 与 nuwa-skill 的机制与结构部分同时受两个上游 MIT 许可证约束，
  许可证要求已按原文保留（见 `THIRD_PARTY_NOTICES.md`）。
- 上述 MIT 许可**不覆盖**罗翔本人的言论、姓名与形象权益，也不构成对其视频的再授权；
  原始视频素材版权归原平台与权利人所有。
- 本仓库未打包任何无法确认来源的文件；如下游使用者对个别内容来源有疑问，
  请对照第八节与各文件头部说明。
