# FeishuConvert - Markdown公式转换器

一个简单而强大的工具，用于将各种格式的Markdown数学公式转换为飞书文档支持的格式。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 功能特点

- 🔄 支持多种公式格式转换
  - 单美元符号：`$...$`
  - 双美元符号：`$$...$$`
  - LaTeX方括号：`\[...\]`
  - LaTeX圆括号：`\(...\)`
- ✨ 自动统一转换为飞书支持的格式：`$$公式$$`
- 🎯 智能处理空格
  - 公式内部无空格
  - 公式与文本之间保持一个空格
- 📋 自动复制功能
  - 转换后自动复制到剪贴板
  - 提供手动复制按钮
- 🚀 批量转换：支持一次性转换多个公式
- 💫 保持原文格式：除公式外的其他文本格式保持不变

## 在线体验

访问：`http://localhost:3000`（本地部署后）

## 快速开始

### 环境要求

- Python 3.6+
- pip（Python包管理器）

### 安装步骤

1. 克隆仓库：
```bash
git clone https://github.com/ChennoShen239/FeishuConvert.git
cd FeishuConvert
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行应用：
```bash
python app.py
```

4. 在浏览器中访问：`http://localhost:3000`

### 使用示例

输入：
```
hello $1233$ and \(2321\) and \[23124\]
```

输出：
```
hello $$1233$$ and $$2321$$ and $$23124$$
```

## 技术栈

- 后端：Flask (Python)
- 前端：原生 HTML/CSS/JavaScript
- 样式：采用苹果设计风格

## 项目结构

```
FeishuConvert/
├── app.py              # 主应用文件
├── requirements.txt    # 项目依赖
├── README.md          # 项目文档
└── LICENSE            # MIT许可证
```

## 开发计划

- [ ] 添加更多公式格式支持
- [ ] 提供API接口
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