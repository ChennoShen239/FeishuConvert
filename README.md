# FeishuConvert

A simple yet powerful tool to convert various Markdown formula formats to Feishu-compatible format.

[中文文档](README_zh.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- 🔄 Support multiple formula formats
  - Single dollar: `$...$`
  - Double dollar: `$$...$$`
  - LaTeX brackets: `\[...\]`
  - LaTeX parentheses: `\(...\)`
- ✨ Auto-convert to Feishu format: `$$formula$$`
- 🎯 Smart space handling
  - No spaces within formulas
  - One space between formula and text
- 📋 Auto-copy: results are automatically copied to clipboard
- 🚀 Batch conversion: convert multiple formulas at once
- 💫 Format preservation: maintain all non-formula text formatting

## Quick Start

### Requirements

- Python 3.6+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ChennoShen239/FeishuConvert.git
cd FeishuConvert
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Visit in browser: `http://localhost:3000`

### Usage Example

Input:
```
hello $\frac{1}{2}$ and \(x^2\) and \[E=mc^2\]
```

Output:
```
hello $$\frac{1}{2}$$ and $$x^2$$ and $$E=mc^2$$
```

## Tech Stack

- Backend: Flask (Python)
- Frontend: Pure HTML/CSS/JavaScript
- Style: Apple Design System inspired

## Project Structure

```
FeishuConvert/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── README.md          # Documentation (English)
├── README_zh.md       # Documentation (Chinese)
└── LICENSE            # MIT license
```

## Development Plan

- [ ] Add more formula format support
- [ ] Provide API interface
- [ ] Add batch file processing
- [ ] Support custom conversion rules
- [ ] Add dark theme

## Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details