# UI Product Design

一个中文 UI/UX 设计 Skill，适用于 Web、移动 App 和微信小程序。连接着陆页与真实任务，兼顾视觉表达、完整交互和平台验证。

## 开始使用

将整个 `ui-product-design` 文件夹放入当前工具的 Skills 目录，保留其内部结构。在已安装环境调用：

```text
使用 $ui-product-design，为当前项目设计并实现着陆页和后续任务页面，验证主 CTA、任务完成及失败恢复。
```

想实际测试效果，可复制 [网页测试提示词](examples/web-test-prompt.md)，在独立的 Web 项目中运行。它提供产品内容和可验证任务，把配色、字体、构图与图形判断留给 Skill。

## 工作方式

- 先明确用户成果、主要任务、入口和恢复路径，再决定页面与视觉。
- 自由创作可用 shell 随机串启发，明确品牌和参考仍优先；种子不进入用户界面。
- 区分新设计、改版、仅设计与轻量修改，保护已有行为与共享组件影响面。
- 分别处理 Web、原生/跨端 App 和微信小程序的导航、单位与辅助功能。
- 用真实渲染和交互证据验证；需要评审时使用新上下文、固定提示和同版本证据。
- 普通任务按范围与具体缺陷完成；高分精修只在明确要求时启用，避免无限追分。

像素艺术、特色插画和动态场景是可选表达，成熟工作台可以通过内容层级与效率完成设计，不强制加装饰。

## 目录

| 路径 | 用途 |
|---|---|
| [ui-product-design/SKILL.md](ui-product-design/SKILL.md) | Skill 入口 |
| [references](ui-product-design/references/) | 按需读取的任务、视觉、平台、动效及评审规则 |
| [随机种子脚本](ui-product-design/scripts/new-design-seed.ps1) | 长度可配置的字母数字串 |
| [research.md](research.md) | 文献研究、来源版本、采用与修正的理由 |
| [网页测试提示词](examples/web-test-prompt.md) | 完整网页试用场景 |
| [验证摘要](validation/summary.md) | 已验证内容与证据范围 |
| [check_package.py](validation/check_package.py) | 编码、链接、配置及脚本契约检查 |

本仓库保留源码与可复用记录；本地截图、内部随机串、临时浏览器目录和重复生成的ZIP不纳入版本控制。

## 验证

包校验需要 Python、PyYAML 和已有的 PowerShell 7 或 Windows PowerShell。运行：

```powershell
python -X utf8 -m pip install -r requirements-dev.txt
python -X utf8 validation/check_package.py
```

校验生成的 `validation/package-check.json` 是本机报告，不提交。校验通过证明文件结构与脚本契约，不证明实际页面审美、真实服务、真机或完整可访问性验收。

方法由公开文章、oil 系列仓库、一手规范与研究综合整理；来源和访问范围见 [sources.md](ui-product-design/references/sources.md)。没有复制上游组件、字体或付费内容。
