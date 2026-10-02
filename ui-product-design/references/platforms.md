# 平台适配

只读取本次目标平台段落。共用任务逻辑、词汇和语义 tokens；导航、控件、尺寸与验证证据随平台改变。技术栈版本、API、组件支持性和限制以当前项目及官方文档核对，以下不是冻结的兼容性承诺。

## Web / Web App / 移动 H5

- 使用项目现有路由，区分链接与动作。验证 CTA 跳转、深链直接打开、刷新、浏览器后退和必要的滚动/查询恢复。嵌入微信的 H5 仍是 Web，涉及宿主桥接时另行核对能力。
- 用语义 HTML 和可访问的控件实现交互。键盘可以完成任务；弹层管理焦点、关闭方式和返回焦点；状态变化按必要程度通知辅助技术。
- 以内容而非固定设备名确定断点。至少检查一组宽屏与窄屏，并测试最长实际内容；包含 hover 的操作提供触屏和键盘路径。
- Web 文本按 WCAG 2.2 AA 检查普通文本 4.5:1，大文本 3:1；大文本阈值是至少 18pt，或至少 14pt 且加粗，不把 CSS 18px 误当成 18pt。需要识别的非文本控件/状态按适用条款检查 3:1。[文本对比](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)、[非文本对比](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)。
- 触控热区按 WCAG 2.2 的 24×24 CSS px 最小目标或适用例外核对；间距例外需要实际测量。重要移动操作可选择更大的热区，例如 44 CSS px，作为项目设计目标而非 AA 统一要求。[目标尺寸](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)。
- 检查放大和重排；普通横向文本在相当于 320 CSS px 宽的视口不应要求双向滚动，真正需要二维布局的内容有例外。按适用条款检查所有文本的 200% 缩放，包括正文、导航、表单、按钮和错误消息；结合长中文确认功能与内容不丢失。字幕和图像形式的文本按条款例外判断，不用只测正文代替全部文本。[重排](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)、[文本缩放](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html)。
- 首屏资源与布局按实测控制；不将第三方字体或动画加载设为使用任务的前提。更复杂的视觉先验证静态降级。

## 原生与跨端 App

- 识别 iOS、Android、Flutter、React Native 等实际运行环境，复用其成熟导航、表单、滚动与辅助功能语义。品牌表达集中在内容、tokens 和少量特色组件；不能照搬浏览器 DOM/ARIA。
- 根据平台规范设置热区。Apple 当前 HIG 区分默认控件尺寸与最低尺寸，iOS/iPadOS 的 44×44 pt 可作为舒适项目基线，不是所有场景的绝对最低；Android 推荐至少 48×48 dp。pt、dp 与 CSS px 不是可跨端照抄的单位。[Apple 无障碍](https://developer.apple.com/design/human-interface-guidelines/accessibility)、[Apple 官方可读文档数据](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/accessibility.json)、[Android 触控目标](https://support.google.com/accessibility/android/answer/7101858)。
- 测试系统字号、VoiceOver/TalkBack、安全区、横竖屏需求、键盘遮挡、系统返回/手势和平台减少动态效果设置。输入区与底部动作可滚到可见位置。
- 启动、深链、离线、授权拒绝与中断后恢复属于任务设计。权限按任务需要解释和请求，取消仍有合理路径；视觉改版不新增权限或真实副作用。
- 记录模拟器与真机各自的验证结果。开发机上的动画或截图不能证明目标手机的性能、辅助功能或触觉/音频结果。

## 微信小程序

- 读取 app.json、页面配置、实际基础库与目标客户端；核对项目是否使用原生小程序、Taro、uni-app 或其他适配层。遵循本项目实现，不把 HTML/React DOM 或浏览器 CSS 直接复制为小程序代码。
- 读取实际 pages/tabBar 配置。普通栈页面可用 `wx.navigateTo`，替换用 `wx.redirectTo`，这两者不能打开 tabBar 页面；tab 页面用 `wx.switchTab`。`wx.reLaunch` 清理页面栈，应服务于明确任务。分享或扫码直接进入详情时，也要有可用的回首页路径。路由回调成功不等于页面已完成呈现。实施前核对当前 API 限制：[路由](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.navigateTo.html)、[切换 tab](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.switchTab.html)。
- rpx 是随屏宽变化的布局单位，不等于 CSS px、pt 或 dp。不要把可访问目标尺寸机械换成固定 rpx；依据实际可点击范围与真机可用性评估。当前 WXSS 也包含 vw 相关建议，按项目与大屏响应式需要选择，不滥用单一比例单位。[WXSS](https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxss.html)。
- 优先用原生导航、按钮、表单等可用组件；自定义导航需测量状态栏、胶囊区域和安全区，不能硬编码一台手机的位置。窗口 safeArea 有支持性和方向限制并可能缺失，提供合理回退。[胶囊区域](https://developers.weixin.qq.com/miniprogram/dev/api/ui/menu/wx.getMenuButtonBoundingClientRect.html)、[窗口信息](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getWindowInfo.html)。
- 只使用目标基础库和适配层支持的样式、字体、动画、图片与语义能力。小程序支持部分 ARIA，但移动读屏行为及 iOS/Android 存在差异；按当前文档核对，不用浏览器成功结果替代小程序支持性。图形提供文字信息和触控替代。[无障碍组件](https://developers.weixin.qq.com/miniprogram/dev/component/aria-component.html)。
- 弱网、前后台切换、键盘、授权取消、分享回流、返回和重复提交都要走查。减少持续循环动画、频繁跨层数据更新与过大首屏资源；分包/资源限制按当前官方规则核对，不缓存一个永久 MB 数字。
- 开发者工具验证构建、路由和状态；目标 iOS/Android 真机确认字体、可点击区域、胶囊、安全区、键盘与动效。官方页面读取失败时，通过可访问的官方渠道或开发者工具帮助补证；没有拿到证据时注明未核对，不宣称已验证。

跨端设计统一品牌识别和任务词汇，允许导航与控件因平台不同而不同。网页模拟器不能证明原生 App 或微信小程序验收。
