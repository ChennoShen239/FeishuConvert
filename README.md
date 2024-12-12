# FeishuConvert

一个简单的Web工具，用于将各种格式的Markdown数学公式转换为飞书（Feishu）兼容的格式。

## 功能特点

- 支持多种公式格式转换：
  - 单美元符号：`$公式$`
  - 双美元符号：`$$公式$$`
  - LaTeX方括号：`\[公式\]`
  - LaTeX圆括号：`\(公式\)`
- 智能空格处理
- 保留换行格式
- 自动复制结果
- 批量转换
- 美观的用户界面

## 使用方法

1. 克隆仓库：
```bash
git clone https://github.com/[your-username]/FeishuConvert.git
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

4. 在浏览器中访问：`http://127.0.0.1:3000`

## 技术栈

- Python Flask
- HTML/CSS/JavaScript
- Regular Expressions

## 许可证

MIT License