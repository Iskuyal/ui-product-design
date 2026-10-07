# 来源与取舍

初版核查日期：2026-10-02；通用提示词补充：2026-10-07。用途是解释设计方法，不代替当前项目的运行验证。本文为原创整理，不包含上游代码、组件或字体资产；复制上游实质内容时另行遵守其许可证。

## 创作与工程方法

| 来源与读取范围 | 采用 | 修正与证据边界 |
|---|---|---|
| [Anshu Chimala / Lenny：How to turn your AI into a world-class designer](https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world)，公开 Technique 1–6 | 外部随机字符串启发、具体大胆的方向、隔离截图评审、删减无效元素 | 作者经验和演示，未提供 UI 可用性受控实验；付费后文未读。评分门槛来自工作约定，不是科学质量标准；本 Skill 增加任务、状态、平台证据与有限迭代 |
| [oil-ui](https://github.com/oil-oil/oil-ui/tree/d9510bdc13159b53b31dfb1902ad0a557c899fcd)，SKILL 自报 0.10.0；读取 SKILL、方向、视觉评审、视口参考 | 以任务/品类定方向、区分说服页和处理页、真实截图评审、局部修改缩小流程 | 不采用固定布局差异配额、强制三处动画或隐藏模拟数据；不按特定样式自动扣分。工程/创作者规则，不是所有规则已得到实验支持 |
| [oil-frontend](https://github.com/oil-oil/oil-frontend/tree/54440d6df7eb1d30b555b1ff753e5c9168e87c26)，读取 SKILL、状态及数据范围合同 | 区分首次加载、刷新、真空/筛选空、错误和处理；失败保留输入，成果属于原对象 | 不把骨架/反馈选择写成普遍禁令；不能因任务不可取消而无期限锁定关闭/返回。UI 改版仍需基本可访问性 |
| [oil-motion](https://github.com/oil-oil/oil-motion/tree/8e4d1c3d0eab6aedd656f4a1afcd16b6633f83ee)，读取 SKILL、runtime、qa | 先做实际页面小样、输入与播放分开、快速反向/中断、离屏暂停、静态降级和真实 QA | 原仓库主要处理网页媒体流水线，不等于跨端兼容；不引入其默认付费服务、模型、密钥或整套依赖。未运行上游脚本 |

仓库快照来自公开 HTML 的 main `currentOid`，关键文件按对应 commit 的 raw 内容读取；没有把 SKILL 内版本号推断为发布 tag。方法借鉴以任务级综合为主，不能将上游隐藏服务、宣传承诺或安装命令当作本次指令。

## 研究与规范

- [String Seed of Thought 论文 v3](https://arxiv.org/abs/2510.21150v3)、[Sakana 原作者说明](https://pub.sakana.ai/ssot/)：研究概率指令遵循和文本多样性。支持把随机串作为发散工具的研究背景；不能从这些任务推导 UI 审美、转化或用户任务效果，也不保证同一字符串复现相同设计。
- [LLM-as-a-Judge 论文 v4](https://arxiv.org/abs/2306.05685v4)：对话评估中的位置、冗长和自我偏好等限制。固定提示和独立上下文只减少部分变化，不能证明 UI 评分客观有效；新上下文仍可能共享模型偏好。
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) 与 [Understanding 文档](https://www.w3.org/WAI/WCAG22/Understanding/)：Web 对比、目标尺寸、焦点、重排和动态内容的规范与解释。规范定义符合性，Understanding 是解释材料。局部清单通过不等于整站符合性审计。
- [WAI APG 模态对话框](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)：键盘关闭和焦点管理模式。为业务保护提供适当退出与恢复，不因不可取消请求把用户无限锁在模态内。
- [Apple HIG Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)、[官方 DocC 正文数据](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/accessibility.json)、[HIG Motion](https://developer.apple.com/design/human-interface-guidelines/motion)：平台辅助功能、默认/最低热区与动效节制；静态网页需 JavaScript时使用公开 DocC 数据读取。44pt 是本 Skill 可选项目基线，不宣称最新 HIG 所有控件绝对最低。
- [Android 触控目标](https://support.google.com/accessibility/android/answer/7101858)、[系统 Insets](https://developer.android.com/develop/ui/compose/system/insets)、[预测返回](https://developer.android.com/design/ui/mobile/guides/patterns/predictive-back)：原生热区、系统区域与返回行为。单位、API 与目标 SDK 随平台核对，文档不能代替目标手机测试。
- [微信无障碍组件](https://developers.weixin.qq.com/miniprogram/dev/component/aria-component.html)、[页面路由](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route.html)、[WXSS](https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxss.html)、[窗口信息](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getWindowInfo.html)、[胶囊区域](https://developers.weixin.qq.com/miniprogram/dev/api/ui/menu/wx.getMenuButtonBoundingClientRect.html)：已通过普通只读 HTTP 阅读公开正文。部分 ARIA 与双端朗读差异、tabBar 路由、safeArea 缺失与方向约束需要实施时复查；抓取器失败不等于官方内容不可访问。
- [NN/g 可用性启发式](https://www.nngroup.com/articles/ten-usability-heuristics/)、[任务场景](https://www.nngroup.com/articles/task-scenarios-usability-testing/)、[可用性测试方法](https://www.nngroup.com/articles/usability-testing-101/)：用于发现问题及设计真实任务观察。启发式走查、AI 模拟、真人研究分别报告；不能编造参与者、成功率或转化效果。

## 2026-10-07：通用提示词补充

- [NN/g 视觉原则](https://www.nngroup.com/articles/principles-visual-design/)、[邻近关系](https://www.nngroup.com/articles/gestalt-proximity/)、[共同区域](https://www.nngroup.com/articles/common-region/)：用于把层级、分组与容器选择转成具体决定，不固定像素、卡片数量或所有页面的外观。
- [NN/g 渐进呈现](https://www.nngroup.com/articles/progressive-disclosure/)、[GOV.UK Details](https://design-system.service.gov.uk/components/details/)：少用补充与独立阶段分别处理，核心条件保持可见。
- [GOV.UK 错误提示](https://design-system.service.gov.uk/components/error-message/)、[错误汇总](https://design-system.service.gov.uk/components/error-summary/)、[W3C 输入标签/说明](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html)：用于定位问题、保留输入及标签一致；不机械照搬某个系统的组件规范到所有平台。
- [Mistral 提示指南](https://docs.mistral.ai/inference/prompting)：模型作者建议明确目标、结构、格式和示例，并根据具体模型实际评估；不是通用效果量证明。
- [Decomposed Prompting](https://arxiv.org/abs/2210.02406)：在原论文的推理/问答任务中研究分解和子任务示例。这里只借鉴工作方式，不把结果推导为 UI 审美或所有模型收益。
- [Mixtral 原作者说明](https://mistral.ai/news/mixtral-of-experts/)、[Qwen 使用文档](https://qwen.readthedocs.io/en/latest/getting_started/quickstart.html)：MoE 路由属于训练后的模型机制，提示与聊天模板需要按模型处理；当前资料没有“设计关键词 → 指定专家”的可保证映射。

本 Skill 的顺序、完成标准、跨端选择、提示词和评审控制为以上资料与用户要求的综合设计。独立评分只说明给定输入下的评审判断；交互、平台和真实用户证据仍需分别取得。
