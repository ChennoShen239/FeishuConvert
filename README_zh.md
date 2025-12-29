# FeishuConvert - Markdown 公式转换器

一个简单而强大的工具，用于将各种格式的 Markdown 数学公式转换为飞书文档支持的格式。

[English](README.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 功能特点

- 🔄 支持多种公式格式转换
  - 单美元符号：`$...$`
  - 双美元符号：`$$...$$`
  - LaTeX 方括号：`\[...\]`
  - LaTeX 圆括号：`\(...\)`
- ✨ 自动统一转换为飞书支持的格式：`$$公式$$`
- 🎯 智能处理空格
  - 公式内部无空格
  - 公式与文本之间保持一个空格
- 📋 自动复制：转换结果自动复制到剪贴板
- 🚀 批量转换：支持一次性转换多个公式
- 💫 保持原文格式：除公式外的其他文本格式保持不变

## 快速开始

### 环境要求

- Python 3.8 或更高版本
- [uv](https://github.com/astral-sh/uv) - 快速的 Python 包安装器和解析器

### 安装步骤

1. 安装 uv（如果尚未安装）

```bash
# macOS 和 Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# 或通过 pip 安装
pip install uv
```

2. 克隆仓库：

```bash
git clone https://github.com/ChennoShen239/FeishuConvert.git
cd FeishuConvert
```

3. 创建虚拟环境并安装依赖：

```bash
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -e .
```

或者，您可以直接使用 uv 运行应用，无需激活虚拟环境：

```bash
uv run python app.py
```

4. 在浏览器中访问：`http://localhost:3000`

### 使用示例

输入：

```
hello $\frac{1}{2}$ and \(x^2\) and \[E=mc^2\]
```

输出：

```
hello $$\frac{1}{2}$$ and $$x^2$$ and $$E=mc^2$$
```

## 技术栈

- 后端：Flask (Python)
- 前端：原生 HTML/CSS/JavaScript
- 样式：采用苹果设计风格
- 包管理：uv（快速可靠的依赖管理工具）

## 项目结构

```
FeishuConvert/
├── app.py              # 主应用文件
├── pyproject.toml      # 项目配置和依赖（uv）
├── requirements.txt    # 项目依赖（兼容性保留）
├── README.md          # 文档（英文）
├── README_zh.md       # 文档（中文）
└── LICENSE            # MIT许可证
```

## 开发计划

- [ ] 添加更多公式格式支持
- [ ] 提供 API 接口
- [ ] 添加批量文件处理功能
- [ ] 支持自定义转换规则
- [ ] 添加暗色主题

## 贡献指南

1. Fork 本仓库
2. 创建新的分支：`git checkout -b feature/your-feature`
3. 提交更改：`git commit -am 'Add some feature'`
4. 推送到分支：`git push origin feature/your-feature`
5. 提交 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情
