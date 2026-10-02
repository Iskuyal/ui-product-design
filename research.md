# 中文 UI/UX 设计 Skill：一手来源研究与执行决策

核查日期：**2026-10-02（Asia/Shanghai）**。范围：Web、iOS/iPadOS、Android、微信小程序。以下是公开原文、官方规范和上游仓库的核查笔记，不是产品实测报告。没有安装上游 Skill、执行其脚本、调用付费模型或修改全局配置。

证据分为四类：**规范要求**（例如 WCAG）、**平台建议/API 合同**、**研究结果**（限论文任务与实验条件）、**创作者方法**（经验与演示，不等于实验结论）。文中的“建议 Skill”是本研究的综合决策，不冒充来源原话。

## 1. 应进入 Skill 的决策

| 触发条件 | 建议执行 | 成功证据与边界 |
| --- | --- | --- |
| 新页面或改版 | 先明确用户、业务对象、首要任务、入口与完成结果，再定视觉方向 | 能写出“从何处进入 → 对哪个对象做什么 → 看见什么结果”；漂亮首屏不能代替完成链。依据 S01–S04、S18 |
| 设计方向反复撞模板 | 从产品内容、品牌与场景提出不同关系；必要时使用可记录的随机字符串启发 | 比较结构、信息优先级、字体/色彩与素材作用；随机性只扩大候选，不保证审美、可用性或复现。依据 S01、S03、S05 |
| “不要 AI 味” | 指出具体不适配：层级混乱、无信息作用的装饰、重复容器、误导文案、内容不真实 | 不按渐变、圆角卡片、紫色、左右分栏等样式自动扣分；能说明为何不适合当前任务才改。依据 S03、S17 |
| 同时有营销页和任务页 | 共享品牌与组件语法，分别安排说服内容和操作内容 | CTA 到真实任务入口；任务页优先当前对象、输入和结果，检查往返上下文；不重复营销 Hero。依据 S03、S04、S17–S18 |
| 数据请求/提交/长任务 | 为受影响范围列状态与恢复路径，分开首次加载、刷新、真空、筛选无结果与失败 | 异步失败保留输入；旧响应不覆盖新选择；重新读取确认保存；进度可观察且不伪造。依据 S04、S08、S17 |
| 需要视觉精修 | 同版本、真实内容、代表性视口取截图；较大改动可交给隔离看图评审者 | 固定评审任务与参考，输出位置、观察、影响和调整；截图不证明交互、语义、读屏或性能。依据 S01、S03、S06 |
| 设置评审停止条件 | 默认一轮评审、一轮修正；必要时追加有明确问题的一轮 | 分数是审美意见，不能替代功能与平台验收；本次用户要求的独立评分门槛可保留，并配合预算、证据与未完成报告，避免无限追分。依据 S01、S03、S06 |
| 跨平台实现 | 保持任务、术语、品牌关系一致，分别采用平台原生语义、导航、单位与安全区 | Web 键盘/读屏、原生系统辅助功能、小程序两端读屏和返回分别验证；同一张截图不证明跨平台成功。依据 S07–S16 |
| 计划加入动效 | 先说明它解释什么变化/反馈；优先项目已有或原生动效，再决定是否需要素材生成 | 不强制三处动画；可中断、可反向、可降级；资源失败和减少动态模式仍能完成任务。依据 S02、S09、S12、S14 |

## 2. 用户指定来源

### S01 · Lenny’s Newsletter / Anshu Chimala

- 原文：[How to turn your AI into a world-class designer](https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world)，标注发布日期 2026-09-01；核查 2026-10-02。
- 实际可读：Discover、Define、Deliver 与 Technique 1–6；Technique 7 标题后出现付费订阅门槛。**未读取付费后文，也未通过缓存、镜像或其他方式绕过。**
- 具体主张：先发散后收敛；外部脚本随机字符串用于设计联想；在新上下文用截图进行批评，固定提示，并以 10 分评分；文章示例用 9 分作为停止要求；最后删除无贡献的元素。
- 建议采用：将创意方向具体化；把批评者与制作论证隔离；使用参照画面；保留实际截图；减去冗余。
- 建议修正：外部随机字符串不是 API 解码 seed，不保证每次独特或更好；“模型只能选最可能 token、无法随机”过度简化，SSoT 原作者明确讨论随机解码。9 分不是文献验证的通用质量门槛；本次用户可将其约定为独立审美评审的完成条件，但不能替代功能/平台验收；大模型/高价格更懂设计、特定搭配更便宜等只是该作者示例。生成图片、视频与外部服务应由任务价值、现有能力、授权和预算决定。
- 证据范围：作者经验与演示。没有在公开内容中看到 UI 任务成功率、转化率或人类偏好的受控比较，不能宣传“科学证明成为世界级设计师”。

### 上游版本快照

GitHub 未认证 REST API 返回限流；`git ls-remote` 连接失败。随后从正常公开仓库 HTML 的 `currentOid` 获得以下 main HEAD，并读取对应固定 commit 的公开 raw 文件；没有克隆或安装仓库。tag 未取得，不推断存在发布 tag。

| 来源 | 仓库与核查 commit | 实际读取的关键文件 | 定位 |
| --- | --- | --- | --- |
| S02 | [oil-motion](https://github.com/oil-oil/oil-motion)，`8e4d1c3d0eab6aedd656f4a1afcd16b6633f83ee` | [SKILL.md](https://github.com/oil-oil/oil-motion/blob/8e4d1c3d0eab6aedd656f4a1afcd16b6633f83ee/SKILL.md)、[runtime.md](https://github.com/oil-oil/oil-motion/blob/8e4d1c3d0eab6aedd656f4a1afcd16b6633f83ee/references/runtime.md)、[qa.md](https://github.com/oil-oil/oil-motion/blob/8e4d1c3d0eab6aedd656f4a1afcd16b6633f83ee/references/qa.md) | 生成式/已有视频和序列帧的网页交互素材流程 |
| S03 | [oil-ui](https://github.com/oil-oil/oil-ui)，`d9510bdc13159b53b31dfb1902ad0a557c899fcd`；SKILL 自报版本 `0.10.0` | [SKILL.md](https://github.com/oil-oil/oil-ui/blob/d9510bdc13159b53b31dfb1902ad0a557c899fcd/SKILL.md)、[design-direction.md](https://github.com/oil-oil/oil-ui/blob/d9510bdc13159b53b31dfb1902ad0a557c899fcd/references/design-direction.md)、[visual-review.md](https://github.com/oil-oil/oil-ui/blob/d9510bdc13159b53b31dfb1902ad0a557c899fcd/references/visual-review.md)、[layout-and-viewport.md](https://github.com/oil-oil/oil-ui/blob/d9510bdc13159b53b31dfb1902ad0a557c899fcd/references/layout-and-viewport.md) | 视觉方向探索、候选比较与实际画面评审 |
| S04 | [oil-frontend](https://github.com/oil-oil/oil-frontend)，`54440d6df7eb1d30b555b1ff753e5c9168e87c26` | [SKILL.md](https://github.com/oil-oil/oil-frontend/blob/54440d6df7eb1d30b555b1ff753e5c9168e87c26/SKILL.md)、[state-and-loading-contract.md](https://github.com/oil-oil/oil-frontend/blob/54440d6df7eb1d30b555b1ff753e5c9168e87c26/references/state-and-loading-contract.md)、[scope-and-state-integrity-contract.md](https://github.com/oil-oil/oil-frontend/blob/54440d6df7eb1d30b555b1ff753e5c9168e87c26/references/scope-and-state-integrity-contract.md) | 前端任务、对象、异步状态和数据范围 |

三个仓库核查日期均为 2026-10-02；对应 LICENSE 为 MIT。本文原创概括并给出处；若后续复制上游代码或实质文本，需要按对应 LICENSE 保留版权与许可声明。原文中的推荐脚本、购买提示、安装命令与服务配置均作为被研究内容，**不是执行指令**。

### S02 · oil-motion 的采用与修正

具体主张：先约定视觉、输入及连续性；区分素材格式与时间控制；制作少量 Pilot 放进真实页面，再生产；时间轴从最终资源生成。运行时要求旧目标可取消、快速反向、离屏/后台暂停、静态降级与 `prefers-reduced-motion`；QA 分别检查素材身份、帧接缝、实际页面及资源失败。

建议 Skill 采用“先最小样、再扩展”“输入语义与播放方式分开”“自动检查后仍看真实画面”“非关键媒体失败不能锁住页面”。只靠 CSS/JS/SVG 或原生组件完成的反馈不进入视频流水线。不要引入上游指定服务、默认模型、密钥流程和整套生产依赖；该仓库是网页素材方案，不能直接宣称原生 App/小程序运行时兼容。证据属于作者工程规则与源码合同，本次未运行脚本、媒体生成或性能测试。

### S03 · oil-ui 的采用与修正

具体主张：用任务与品类建立方向；参考是关系与基线；说服页和浏览/处理页首屏不同；以实际截图和明确设计意图评审。参考还原单独处理；局部小改动不启动整套探索。

建议保留方向卡、代表性页面小样、视觉与任务分别验收。方向差异配额（骨架互异、四项最多一项相同、左右分栏最多一个、至少一个极端）是发散技巧，不是通用质量规则。任务页不机械限制页头一两行。评审中“单侧色条算问题”和特定样式扣分应改为任务适配诊断。强制三处动画改为按反馈需要决定。模拟/未核实内容是否在界面标记，应看用户是否可能误当真；不能为美观删掉必要真实状态或限制说明。上游付费 oil-ui-pro 未读取，不能补写其内容。证据是创作者方法，不是这些风格规则的可用性实验证明。

### S04 · oil-frontend 的采用与修正

具体主张：明确对象、数据集合、操作、忙碌、提交及结果范围；把首次加载、刷新、真空、筛选无结果、错误和后台任务分开；查询列表/总数/分页来自同一响应；失败保留输入和位置；从真实入口完成操作、保存后重新读取。

建议采用状态与范围语义，按目标风险复用检查，不为一次文案修改创建长期测试体系。骨架、spinner 与加载品牌的硬性禁令不当作普遍规范，反馈选型应符合时长、数据稳定性和平台组件。上游“请求不可取消时禁用所有关闭/Escape”不宜变成无限锁定：明确取消能力，短提交防重；长任务可转成可观察后台状态，提供离开/恢复路径；Web 模态默认遵守 APG 的退出和焦点协议。全新 UI/UX Skill 应有基本可访问性验收，不能仅保留已有行为。证据是上游工程规则；未用本项目任务验证其有效性。

## 3. 必要补充一手来源

下表各来源均于 **2026-10-02** 核查。规范与平台建议来自发布者自身；NN/g 是作者/机构的研究方法与启发式，不能当成每条都有独立实验效应。

| 编号与来源 URL | 具体主张/版本 | 建议 Skill 采用或修正；证据范围 |
| --- | --- | --- |
| S05 [SSoT 论文 v3](https://arxiv.org/abs/2510.21150v3)、[Sakana 原作者说明](https://pub.sakana.ai/ssot/) | arXiv v3：2026-02-05；论文研究概率指令遵循，并报告 NoveltyBench 多样性结果。原方法可让模型生成字符串，不要求外部 PRNG；实验含随机解码 | 把随机字符串作为可选创意工具；外部脚本 seed 是设计流程改写。不能由概率分布/文本多样性推导 UI 可用性、审美、品牌效果；说明文示意的 51%/49% 不是测量值 |
| S06 [Judging LLM-as-a-Judge v4](https://arxiv.org/abs/2306.05685v4) | v4：2023-12-24；报告位置、冗长、自我偏好及推理限制，研究对象为对话回答评估 | 固定提示有助流程比较，但不消除偏差；必要比较可交换候选顺序，记录模型/提示版本。不能把其文本任务结果直接当 UI 看图评分的准确率 |
| S07 [WCAG 2.2](https://www.w3.org/TR/WCAG22/)、[目标尺寸最低说明](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum) | W3C Recommendation 2024-12-12；2.5.8 AA 是 24×24 CSS px，含间距/等价/行内/用户代理/必要例外；2.5.5 AAA 是 44×44 CSS px | 明确 AA 门槛与触屏舒适基线的区别。文本通常 4.5:1、大字 3:1；200% 文字放大；320 CSS px 重排需保留内容/功能，二维必需内容有例外。不是所有界面都可简单禁止横向滚动 |
| S08 [状态消息说明](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)、[焦点不被遮挡说明](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html) | SC 4.1.3 AA 与 2.4.11 AA 的官方解释；状态变化在不夺焦点时仍应被辅助技术感知；焦点项不可被作者内容完全遮住 | 对保存、错误、搜索结果数量等恰当使用语义/通知，不把整页塞进 live region；检查固定底栏、浮层和键盘遮挡。Understanding 属解释文档，规范要求以 WCAG 为准 |
| S09 [Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)、[Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html)、[Media Queries 5](https://www.w3.org/TR/mediaqueries-5/#prefers-reduced-motion) | 自动开始且并行呈现、持续超过 5 秒的移动/闪烁/滚动信息通常需暂停/停止/隐藏，必要活动有例外；拖动功能需非拖动单指针替代，必要拖动除外。MQ5 为 2026-02-19 Working Draft，定义 reduce/no-preference | 非必要动效可关、能到同一结果；不能把“所有动画最长5秒”冒充 WCAG；不要把草案全部新 API 当所有浏览器已支持。`prefers-reduced-motion` 是否可用按宿主验证 |
| S10 [WAI APG 模态模式](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) | 焦点进入模态，Tab 在内循环，Escape 关闭，关闭后返回触发器或合理下一位置；语义模态须真的阻止外部交互 | 为 Web 弹窗写焦点/退出验收，优先成熟组件；不把加 `aria-modal` 当完整实现。APG 是模式指导，不能仅以符合示例宣称 WCAG 全面通过 |
| S11 [Apple HIG Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)、[公开 DocC JSON](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/accessibility.json)、[Apple UI tips](https://developer.apple.com/design/tips/) | 当前 HIG 表格：iOS/iPadOS 默认控制尺寸 44×44 pt、最低 28×28 pt；建议字体可放大、Dynamic Type、VoiceOver、信息不只靠颜色。静态 UI tips 仍称 44pt minimum，两页措辞不一致 | 将 44pt 设为本 Skill 常规触摸基线可行，但不称最新 HIG 的绝对最低。小尺寸需理由、间距与真实测试。避免将 pt 当图像像素；原生读屏/系统字体设置必须单独核验 |
| S12 [Apple HIG Layout](https://developer.apple.com/design/human-interface-guidelines/layout)、[Layout JSON](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/layout.json)、[HIG Motion](https://developer.apple.com/design/human-interface-guidelines/motion)、[Motion JSON](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/motion.json) | Layout 变更日志 2026-09-09；依据可用窗口空间布局，尊重 safe area。Motion：动效有目的、可选、短而准、可取消，避免高频操作重复装饰 | 不用设备型号代替可用空间；安全区保护内容和控制。减少动态仍显示状态；不为添加而添加三段动画。HIG 是平台设计建议，不证明某时长能提升业务指标 |
| S13 [Android Compose Accessibility API defaults](https://developer.android.com/develop/ui/compose/accessibility/api-defaults) | 推荐交互目标至少 48dp；可扩展命中区，但过小布局可能造成相邻命中区重叠；组件默认提供部分语义 | 基于真实命中区域验收，不能只量图标；检查 TalkBack 名称/角色/选中状态；复用原生组件。dp 与 CSS px/pt/物理像素分别记录 |
| S14 [Android Insets](https://developer.android.com/develop/ui/compose/system/insets)、[Insets setup](https://developer.android.com/develop/ui/compose/system/insets-ui)、[Predictive back](https://developer.android.com/design/ui/mobile/guides/patterns/predictive-back)、[ValueAnimator](https://developer.android.com/reference/android/animation/ValueAnimator#areAnimatorsEnabled()) | Android 15+、target SDK 35 起 edge-to-edge 强制；safeDrawing、safeGestures 和 IME 有不同用途。预测返回未提交时恢复原状态；API 26 起可查询 animator 是否全局启用 | 检查系统栏、切口、键盘和返回取消；不要复制统一底部常量。系统禁用动画不等于 JS/video 自动停；自定义媒体需独立降级。文档 API 合同不代替具体设备测试 |
| S15 [微信 aria-component](https://developers.weixin.qq.com/miniprogram/dev/component/aria-component.html)、[微信体验评分](https://developers.weixin.qq.com/miniprogram/dev/framework/audits/accessibility.html) | 基础库 2.7.1 起支持部分 ARIA；官方提醒两端朗读不同、部分 role 在移动端可能无效。体验评分的目标条件是宽高≥20px，并提供色彩对比/安全区检查 | 20px 是该评分项条件，不能当舒适推荐或 WCAG 门槛。为自定义组件添加正确语义并两端读屏实测；不将 Web ARIA 可用性完全类推到小程序 |
| S16 [微信 getWindowInfo](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getWindowInfo.html)、[胶囊布局 API](https://developers.weixin.qq.com/miniprogram/dev/api/ui/menu/wx.getMenuButtonBoundingClientRect.html)、[页面路由](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route.html)、[WXSS](https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxss.html) | safeArea 为竖屏正方向且部分设备不返回；胶囊坐标基于屏幕原点。navigateTo/redirectTo 仅非 tabBar，switchTab 仅 tabBar；success 不代表页面已渲染完成，reLaunch 不重启 AppService。rpx=窗口宽度/750，并可能取整；当前文档推荐可考虑 vw 且不滥用比例单位 | 容错缺失字段并核对坐标系/窗口变化；保护胶囊和底部操作；验收真实返回、分享入口与重复进入。不能将 88rpx 写成所有设备恒等44px；查询/对象上下文跨页保留需由设计与状态实现保证 |
| S17 [NN/g 十项启发式](https://www.nngroup.com/articles/ten-usability-heuristics/) | 作者说明这是通用经验规则；页面回顾启发式从 249 个可用性问题因子分析发展；涵盖状态可见、用户控制、标准一致、识别、错误恢复与必要内容 | 用于找问题和形成假设；减法不等于扁平/极简风格，不删任务必需的信息或恢复路径；品牌新意不能破坏熟悉的任务操作 |
| S18 [NN/g 任务场景](https://www.nngroup.com/articles/task-scenarios-usability-testing/)、[Usability Testing 101](https://www.nngroup.com/articles/usability-testing-101/) | 用真实目标用户执行现实任务，观察行为；任务不泄露按钮或操作路径。方法介绍与机构实践 | 手动走通、AI 走查、真人测试分别报告。预先定义完成结果，记录阻碍、错误与恢复；小样发现问题不等于转化提升或统计验证，不伪造参与者和成功率 |

Apple 普通网页依赖 JavaScript，本次使用官方公开 DocC JSON 阅读正文，不是绕过限制。微信页面在 web 抓取器中失败，但通过普通 HTTP 读取公开正文成功；最初猜测的 `/framework/ability/aria.html` 返回 404，改用文档自身链接找到 S15 的真实地址，没有把失效地址当证据。

## 4. 可直接采用的任务流程

以下流程是依据来源综合出的 Skill 操作方案，不是任何文章已证明有效的实验处理。

1. **明确设计范围。** 新设计、局部精修、截图还原、现状评审走不同路径；确认平台、真实内容、主任务与可观察结果。可逆细节可带假设推进；涉及对象、提交范围或核心目的的缺项不能暗猜。
2. **先画任务，再开方向。** 用“入口 → 选择/输入 → 反馈 → 完成/恢复”列最短链；确定每页主对象、动作和返回位置。营销页可以大胆表达，任务页先保证对象可识别和操作稳定。
3. **最小小样暴露风险。** 含表单的产品小样要含表单与错误；数据产品含真实列表与空结果；多平台至少选主平台关键页加另一平台的差异风险，不能仅做封面。
4. **建立视觉关系。** 用少量方向说明字体层级、色彩职责、密度、组件语法、素材与动效目的；沿用有效 token 和原生能力。方向探索才引入随机字符串，保存字符串与联想后的决定，选定后停止随机改变系统。
5. **检查流程与状态。** 从用户真正入口操作；覆盖本次风险相关状态；检查提交失败、取消、再次进入和返回；保存后重新读取，确认结果属于原对象。
6. **检查实际画面。** 保留版本、页面、状态、逻辑视口、缩放、平台环境；看中文长标题/错误文案/大字号/窄屏和整体节奏。代表性状态之外不假称覆盖。
7. **评审与集中修正。** 大改动可隔离评审；局部小改由主 Agent 看相邻影响。先修任务阻断和信息误导，再修阅读层级，最后优化风格细节。必要功能仍未完成时不能用“审美收益不清楚”结束整项任务。

### 从着陆页到任务页

示例验收链：营销 CTA → 对应任务入口 → 需要时才登录/授权 → 先前意图仍在 → 用户处理真实对象 → 显示成功/失败 → 返回列表仍在原位置且对象状态更新。

这不是要求每个产品都有注册、多步流程或营销页面。已有用户从分享、通知、搜索或深链直接进入任务页时，应能认识对象、理解当前状态并开始操作。原型未接入动作应在交付与必要用户界面中明确，不能用成功 toast 伪装持久化完成。（S04、S16、S18）

### 状态与恢复的最小矩阵

| 条件 | 应说明/允许 | 重点验证 |
| --- | --- | --- |
| 首次请求 | 表明正加载哪个范围；占位符合最终结构，是否骨架按需要决定 | 加载中不闪空状态；无重复反馈、无明显跳位 |
| 旧数据刷新 | 保留可用内容，说明当前正在更新；完整查询快照一起切换 | 快速改条件时旧响应不覆盖新结果 |
| 集合为空 | 尚未有对象的原因；适合的创建/导入/发现入口 | 没有错误冒充空集合 |
| 搜索/筛选无结果 | 当前条件没有匹配；修改或清除条件 | 不误告知用户整个集合为空 |
| 加载/提交失败 | 具体可理解原因、可行恢复；输入和对象位置保留 | 重试范围正确，不偷偷重复创建/扣费 |
| 局部提交中 | 动作已受理、防重复、稳定命中区与状态 | 一项操作不锁全部列表；不可取消不要叫“取消” |
| 排队/长任务 | 可观察状态、实际可获取的进度、返回/恢复入口 | 离开再进入仍能找回任务；不编造百分比/步骤 |
| 成功 | 原对象的新状态/真实产物与合理下一步 | 重新读取后结果仍在；不是只看回调或 toast |

## 5. 跨平台最小验收

| 平台 | 尺寸与单位 | 必查行为 |
| --- | --- | --- |
| Web | AA 目标最低 24×24 CSS px 及其例外；本 Skill 可把常规触屏控件 44×44 CSS px 定为项目基线，须标注为项目选择 | 键盘完成任务、可見焦点、名称/角色/值、状态通知；200%文字放大/320 CSS px重排；固定区域不遮挡焦点；原生链接/按钮和弹窗焦点/退出 |
| iOS/iPadOS | pt；44×44 pt 默认目标作为常规基线；当前 HIG 同时列28×28 pt最低，不把小图标尺寸等同命中区 | Dynamic Type、VoiceOver、系统导航/返回、safe area、键盘与窗口变化；减少动态时保留状态与结果 |
| Android | dp；常规交互命中区至少48dp，文字遵从系统缩放 | TalkBack 语义、系统/预测返回与取消、IME/systemBars/gesture insets；系统禁用动画与自定义媒体分别验证 |
| 微信小程序 | px 与 rpx/vw分别解释；常规触屏目标44逻辑px可作本 Skill 的项目基线，**不是微信官方强制44px**；按实际窗口核对转换 | iOS/Android 微信读屏差异、原生组件/自定义ARIA、胶囊与安全区、键盘、tabBar/非tabBar路由、分享进入/返回、窗口变化；记录基础库/渲染引擎与真机验证范围 |

减少动态不等于把 duration 改为 0 后等待动画结束回调推进业务。设计应能直接进入同一有效状态；关闭视差、持续 scrub、大范围位移或循环媒体后仍保留反馈和必要信息。小程序未核实存在跨渲染引擎通用的系统“减少动态”接口，不宣称复制 Web media query 即可；需要时提供可关闭装饰动态的产品入口并在目标环境确认能力。（S09、S12、S14–S16；回调与入口策略为工程综合建议）

## 6. 截图评审的原创协议

固定提示应固定判断维度和任务约束，不能固定想获得的答案。交接当前画面、用户任务、目标平台、选定方向、不能改的约束、必要参照和状态；不交接制作论证、工时、旧评分或“必须给9分”。每轮仍须给足任务背景，不是只给图让评审者猜产品。（S01、S03）

可用的短提示：

> 依据提供的任务、平台、方向与约束评审当前画面。先判断用户是否能识别当前对象、信息优先级与主操作，再检查中文阅读、对齐、空间、颜色、控件和跨状态一致性。最多指出三处最高影响的问题，每处写出位置、可观察事实、用户影响及具体调整。分别标记功能/可读性缺陷与风格偏好。不要因某种颜色、布局或组件常见就判失败；不要模仿参考的品牌或内容。说明截图无法判断的内容。可给各维度的主观评分，但分数不能替代缺陷与证据。只评审，不改文件。

可选评分维度：任务表达、内容层级/可读性、视觉关系/一致性、状态说明、品牌适配。缺少状态证据的维度写“未评估”，不凑分；已有项目可直接按项目规范列偏差，不打分。模型、提示、参照、视口或内容变化后，分数不能当同口径趋势。即使全部高分，也必须单独走交互、语义、缩放、辅助技术与目标环境验收。（S03、S06–S16）

## 7. 未验证与不应写成承诺的内容

- Lenny 付费后文、oil-ui-pro 付费规则未读取；本文没有归纳这些不可见内容。
- 未运行上游脚本、生成服务、demo 或候选 UI；上游提到的服务/模型能力、价格、产物质量与成本占比未做独立复现。
- 未进行真人可用性研究；没有任务成功率、转化提升、审美评分一致性或真实设备性能数据。
- LLM 评审研究针对对话任务，不提供本 Skill 的 UI 评分效度；随机 seed 论文不提供 UI 创造性/UX 因果结论。
- 平台文档是能力与建议，不能代替项目当前 SDK/基础库/渲染引擎、真实屏幕与辅助技术验证；本研究未做这些运行验证。
- 可访问性清单是设计工作最低检查集合，不等于完整 WCAG 合规审计；通过静态构建、截图、模拟器或单一设备时，应准确报告各自证据范围。
