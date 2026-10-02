# 安装与使用

## 安装哪个目录

安装 [skills/ui-product-design](../skills/ui-product-design/) 整个文件夹，保留 `SKILL.md`、`references`、`scripts`、`agents` 与 `LICENSE`。仓库的研究文档和开发校验无需复制到运行时。

在支持安装器的 Codex 环境中，可请求：

```text
使用 $skill-installer 安装 https://github.com/Iskuyal/ui-product-design/tree/main/skills/ui-product-design
```

若已通过其他路径安装且能够识别，不要重复创建同名副本；先比较现有修改再更新。

## 手动安装到 Codex

当前官方文档列出的个人目录为 `~/.agents/skills`，项目目录为 `<项目>/.agents/skills`；本页以个人安装为例。如果环境已有其它有效目录，按该环境配置处理。[官方 Skill 文档](https://learn.chatgpt.com/docs/build-skills)

先克隆仓库：

```sh
git clone https://github.com/Iskuyal/ui-product-design.git
cd ui-product-design
```

Windows PowerShell：

```powershell
$skillRoot = Join-Path $env:USERPROFILE '.agents\skills'
$skillTarget = Join-Path $skillRoot 'ui-product-design'
if (Test-Path -LiteralPath $skillTarget) {
    throw '已存在同名 Skill，请先比较本地修改，再决定更新。'
}
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
Copy-Item -LiteralPath '.\skills\ui-product-design' -Destination $skillTarget -Recurse
```

macOS / Linux：

```sh
skill_root="$HOME/.agents/skills"
skill_target="$skill_root/ui-product-design"
if [ -e "$skill_target" ]; then
  echo '已存在同名 Skill，请先比较本地修改，再决定更新。'
else
  mkdir -p "$skill_root"
  cp -R ./skills/ui-product-design "$skill_target"
fi
```

项目安装则将目标换为该项目的 `.agents/skills/ui-product-design`。这些示例保留已有目录，不自动覆盖。若新安装未出现，可重启 Codex 后检查。[官方本地发现说明](https://learn.chatgpt.com/docs/build-skills)

其它 Agent Skills 工具按其实际 Skills 路径复制同一个文件夹；没有测试过的工具兼容性不能由目录格式推断。

## 调用与选择范围

```text
使用 $ui-product-design，为当前项目设计并实现着陆页和后续任务页，验证核心动作与失败恢复。
```

只需要方案时，明确“仅设计，不开发或接入后端”。已有产品改版时，提供要改善的问题、现有约束与不能改变的行为。像素艺术、插画或动效可以提出为偏好；已有品牌和准确参考优先。

不必写长提示词：补足产品用途、目标用户、主要任务、平台和交付范围即可。[网页试用场景](../examples/web-test-prompt.md)提供了一份完整样例。

## 依赖与更新

Skill 的主要内容是 Markdown；随机启发辅助脚本可在已有 PowerShell 中执行。环境没有它时，流程允许使用已有 shell 的随机源，无需为了设计安装 Python 或前端框架。仓库校验另有 Python 开发依赖。

更新时先拉取仓库，比较已安装目录中的本地改动，再同步文件。不要把新目录嵌套复制到旧目录中；保持唯一的有效同名版本。保留许可证及来源说明。
