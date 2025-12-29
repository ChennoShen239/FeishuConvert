# FeishuConvert

[English](README.md) | [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

将 LaTeX/Markdown 数学公式定界符转换为飞书兼容的 `$$formula$$` 格式。

## 支持的格式

- `$formula$` → `$$formula$$`
- `$$formula$$` → `$$formula$$` (保留)
- `\[formula\]` → `$$formula$$`
- `\(formula\)` → `$$formula$$`

## 快速开始

```bash
# 安装 uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 克隆并设置
git clone https://github.com/ChennoShen239/FeishuConvert.git
cd FeishuConvert
uv sync

# 运行
uv run python app.py
# 或
python app.py
```

访问 `http://127.0.0.1:3000`

## 示例

**输入:**

```
$\alpha$ 和 \[\beta(1-\theta)\alpha f^{\prime}(k^d)=1\]
```

**输出:**

```
$$ \alpha $$ 和 $$ \beta(1-\theta)\alpha f^{\prime}(k^d)=1 $$
```

## 技术栈

- **后端:** Flask 3.0.0
- **正则:** regex 2023.10.3 (完整 regex 支持)
- **包管理:** uv
- **Python:** ≥3.8

## 实现细节

- 基于正则表达式的定界符转换（使用前瞻/后顾断言）
- 智能空格处理（保留间距，移除空行）
- 批量处理支持
- 通过 Web API 自动复制到剪贴板

## 许可证

MIT
