---
name: vibe-knowledge
description: 制作「Vibe 知识大赏」风格的知识科普短视频：纯前端 Canvas 动画 + BGM 卡点 + 逐帧导出 4K 60fps MP4。覆盖选题、BGM 分析、分镜文案、动画实现、逐帧检查、导出和发布文案全流程。当用户想做 vibe 知识大赏、知识科普动画视频、抖音/B站科普短片、"用代码做一个讲 XX 的视频"，或提到参考 vibe-gpt-evolution / 运气的形状 / 月老的算法 / 何时该停下 这类作品时使用。
---

# Vibe 知识大赏

一条 Vibe 知识大赏 = 一个 HTML 页面。画面全部由 `render(t)` 按时间纯函数画出来，播放时跟着 BGM 走，导出时逐帧离线渲染成 4K 60fps MP4，不用录屏。

内容上的灵魂是**选题**和**和观众有关的第一句话**；形式上的灵魂是**卡点**和**丝滑转场**。

## 资源

| 文件 | 用途 |
|---|---|
| `assets/template.html` | 引擎模板：背景/颗粒/暗角、字幕系统、转场工具、两种结尾组件、播放器、4K60 导出、file:// 兜底 |
| `assets/analyze.html` | BGM 分析：时长、有效结尾、BPM、段落突变点（爆发/安静）、每秒能量 |
| `assets/start.bat` | 双击启动本地服务器并打开浏览器（给用户用） |
| `scripts/frame_sink.py` | 接收页面 POST 的帧拼图存成 jpg，用 Read 查看画面 |
| `references/aesthetics.md` | **用户的审美要求和踩过的坑，动手前必读** |
| `references/topics.md` | 选题公式、评判标准、选题库 |
| `references/engine.md` | 模板 API、场景写法、转场配方、常见 bug |
| `references/publishing.md` | 发布标题 / 描述 / 话题 / 封面帧 |

## 流程

按顺序走，每个 ★ 处停下来等用户确认。

### 1. 选题 ★

读 `references/topics.md`。给 6 个左右候选，用表格列出：标题、硬核模型、反直觉结论、核心画面。给出推荐和理由，等用户选。用户已经有选题就跳过。

### 2. 要求

用户会给做视频的要求。没提到的部分用 `references/aesthetics.md` 里的默认值（横屏 1920×1080，导出 4K 60fps，无顶部进度条等）。

### 3. 建项目

在用户工作目录新建项目文件夹，拷入 `assets/template.html`（改名 `index.html`）、`assets/start.bat`、BGM（命名 `bgm.mp4`；视频文件带音轨也可以）。BGM 没指定就问用户要。

本地预览需要 http 服务器（file:// 下浏览器禁止解码音频）。用 `.claude/launch.json` 配一个 `python -m http.server <port> --directory <项目>`，再用 preview 工具打开。

### 4. 分析 BGM

把 `assets/analyze.html` 拷进项目，打开后读 `window.R`：

- `musicEnd`：音乐真正结束的秒数 → 视频总长
- `sections`：能量突变点 → 段落边界（爆发处放核心揭晓，安静段放情绪 / 反思）
- `bpm` / `beat`：字幕和动作尽量落在小节线上

### 5. 分镜 + 文案 ★

先出一张分镜表给用户看（时间 | 段落 | 画面 | 字幕 | 转场），确认后再写代码。写法要求：

- **0–3 秒必须有视觉锚点**：一个和主题强相关的物件（骰子、手机聊天界面、卡片……）+ 入场动作
- **第一句字幕和观众相关**（"如果你这辈子会遇见 10 个人"），不要上来讲术语和历史
- 结构：钩子提问 → 直觉的失败 / 冲突 → 揭晓答案 → 为什么（可视化证明）→ 反转或另一面（放在安静段）→ 生活应用 → 结尾抛问题
- 字幕每条 3–4 秒、一到两行；关键词 `{金色}`、情绪词 `[玫红]`
- 每个段落之间写清楚转场：推进到哪个细节、细节铺满后展开成什么
- 结尾：情感类用**二选一**，科普类用**片名 + 英文**（见 aesthetics.md）
- 事实和数字要核对（公式、年份、奖项）

### 6. 实现

读 `references/engine.md`。在模板上改：`CONFIG`、`CAPS`、`LABELS`、`TINTS`，写每个场景函数，在 `render()` 里按时间分派。场景之间的交接（上一场最后一帧 = 下一场第一帧）要逐个对齐。

### 7. 逐帧检查

浏览器面板截图常超时或分辨率太低，统一用帧拼图：

```bash
python -I <skill>/scripts/frame_sink.py <scratchpad>/frames
```

（后台运行）页面控制台里 `await dump('a.jpg', [t1, t2, t3, t4])`，再用 Read 看 `<scratchpad>/frames/a.jpg`。每个场景至少看：入场、中段、转场前一刻、转场后一刻。对照 engine.md 末尾的检查清单。

### 8. 导出测试

在控制台跑一小段导出验证编码器可用：拦截 `HTMLAnchorElement.prototype.click`，`await exportMP4(60, 2, 2)`，确认 3840×2160、音频 AAC。完整导出交给用户点按钮（130 秒约 13–15 分钟）。

### 9. 交付 ★

告诉用户：怎么打开（双击 `start.bat`）、怎么导出、导出时长、哪些没验证过（例如你听不到音乐，卡点要用户实际听一遍）。需要的话按 `references/publishing.md` 给发布文案。
