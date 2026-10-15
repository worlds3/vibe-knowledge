# Vibe 知识大赏

用纯前端 Canvas 动画做的知识科普短视频。每一期都是一个 HTML 页面：画面全部由 `render(t)` 按时间算出来，跟着 BGM 卡点播放，也能在页面里逐帧导出 **4K 60fps MP4**，不用录屏。

| 作品 | 内容 | 画幅 |
|---|---|---|
| [《何时该停下》](stop-37/) | 最优停止理论 / 37% 法则：遇到第几个人，就该停下？ | 横屏 1080p，导出 120fps |
| [《从噪声到世界》](noise-to-world/) | AI 绘画与视频的进化史：GAN → Diffusion → CLIP → Stable Diffusion → Sora → 世界模型 | 横屏，导出 4K 60fps |

## 观看 / 导出

浏览器禁止 `file://` 页面读取音频，所以要用本地服务器打开：

- Windows：双击作品文件夹里的 `start.bat`
- 其他系统：在作品文件夹里运行 `python -m http.server 8737`，打开 http://localhost:8737

页面里点「播放」观看，点「导出 MP4」逐帧渲染成视频文件（需要最新版 Chrome / Edge，导出时保持标签页在前台）。

快捷键：空格 播放/暂停 · ← → 快退/快进 5 秒 · F 全屏 · Esc 回到面板

## 制作流程：vibe-knowledge skill

[`skill/vibe-knowledge`](skill/vibe-knowledge/) 是把整套制作流程沉淀下来的 Claude Code skill：选题 → BGM 分析 → 分镜文案 → 动画实现 → 逐帧检查 → 4K 导出 → 发布文案。包含引擎模板、BGM 分析页、审美规范和踩坑记录。

安装：把 `skill/vibe-knowledge` 复制到 `~/.claude/skills/`，然后在 Claude Code 里说「做一期 Vibe 知识大赏，讲 XX」或输入 `/vibe-knowledge`。

## 致谢

- 实现方式参考了 [Vibe-GPT-Evolution](https://github.com/wwwyh007/Vibe-GPT-Evolution)（《运气的形状》），BGM 也来自该项目
- 由 Claude 制作
