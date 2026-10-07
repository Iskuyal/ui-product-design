# UI Product Design

[![Validate](https://github.com/Iskuyal/ui-product-design/actions/workflows/validate.yml/badge.svg)](https://github.com/Iskuyal/ui-product-design/actions/workflows/validate.yml) · [MIT License](LICENSE)

一套面向 **Web、移动 App 和微信小程序** 的中文 UI/UX 设计 Skill：从用户任务出发，建立有辨识度的视觉方向，完成页面、状态和实际验证。

适用于 Codex 及能读取 `SKILL.md` 的 Agent Skills 工具。仓库提供设计工作流，不附带成品组件库，也不绑定某个前端框架。

## 快速开始

在支持 `$skill-installer` 的 Codex 环境中，可以使用：

```text
使用 $skill-installer 安装 https://github.com/Iskuyal/ui-product-design/tree/main/skills/ui-product-design
```

也可将 [skills/ui-product-design](skills/ui-product-design/) 整个文件夹复制到工具的 Skills 目录。Codex 手动安装与已有版本更新见 [安装与使用](docs/getting-started.md)。

安装后，在实际项目中输入：

```text
使用 $ui-product-design，为当前项目设计并实现着陆页和后续任务页面，验证主 CTA、任务完成及失败恢复。
```

想先看效果，复制 [完整网页测试提示词](examples/web-test-prompt.md)：它用“巷外”漫游规划场景测试着陆页、探索、详情与个人计划，给出产品任务，把配色、字体、构图和图形判断留给 Skill。

## 什么时候使用

| 场景 | 工作重点 |
|---|---|
| 新界面 / 着陆页 | 内容与任务路径、视觉方向、页面和状态 |
| 已有产品改版 | 保留行为和数据契约，记录基线与共享组件影响面 |
| 仅设计 | 交付可审阅稿件或原型，明确未实现的交互 |
| 局部文字 / 样式调整 | 缩小流程，核对动作含义和必要影响 |

像素艺术、特色插画与动态场景都是可选表达。高频任务页面可以依靠成熟组件与信息效率完成设计；准确设计稿还原和纯后端工作无需启动完整创作流程。

## 设计原则

- **任务先于页面**：连接入口、用户动作、可见成果与失败恢复。
- **创意有语境**：可用随机串发散，品牌、内容和用户约束决定最终选择。
- **跨端分别适配**：共用品牌与任务词汇，分别处理导航、单位、辅助功能和设备证据。
- **验证来自实际结果**：截图、交互、模拟器、真机与用户研究分别报告。
- **评审推动改进**：固定提示、独立上下文、同版本证据；普通任务不为追分无限迭代。

需要更精炼或可分步的指令时，使用 [通用设计提示词](skills/ui-product-design/references/prompt-recipes.md)：将视觉层级、分组、构图节奏、渐进呈现和错误恢复对应到实际决定与检查。大小模型均可使用，短契约为可选工具，不宣称关键词能激活特定 MoE 专家。

## 项目结构

```text
skills/ui-product-design/   可独立安装的 Skill
  SKILL.md                 入口与分流
  agents/                  展示与调用配置
  references/              按需读取的设计、平台与评审规则
  scripts/                 运行时辅助脚本
  LICENSE                  安装包随附许可
docs/                      安装、研究、来源与验证说明
examples/                  可复制的试用提示词
scripts/                   仓库开发校验
.github/workflows/         Windows / Linux 自动校验
```

本地演示应用、内部随机串、截图、临时浏览器数据和生成报告不纳入版本控制。

## 开发与验证

开发校验需要 Python 3.10+、PyYAML 和已有的 PowerShell 7 或 Windows PowerShell；使用 Skill 本身不需要安装 Python。

```sh
python -X utf8 -m pip install -r requirements-dev.txt
python -X utf8 scripts/validate.py
```

校验覆盖 Skill 配置、仓库文档链接、许可一致性和随机脚本契约，报告生成于 `build/validation.json`。自动校验使用 Windows 与 Linux；CI 不等于实际产品的审美、真机或可访问性验收。详见 [验证范围](docs/validation.md)。

## 文档与贡献

- [安装、调用与更新](docs/getting-started.md)
- [方法研究与取舍](docs/research.md)
- [UI/UX 与通用提示词的新研究](docs/research-ui-prompting-2026-10-07.md)
- [可复制的通用提示词](examples/general-design-prompt.md)
- [来源与授权说明](docs/attribution.md)
- [贡献指南](CONTRIBUTING.md)

原创代码和文档采用 [MIT](LICENSE)。链接到的文章、研究、字体或第三方素材仍按各自权利与许可处理。
