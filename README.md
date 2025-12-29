# FeishuConvert

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A web-based tool that converts various formats of mathematical formulas in Markdown to Feishu (飞书) compatible format.

## Overview

FeishuConvert is designed to streamline the process of writing mathematical formulas in Feishu documents. It automatically converts various LaTeX and Markdown formula formats into Feishu's supported format, making it easier to maintain consistent formula formatting across your documents.

## Features

- **Multiple Formula Format Support**
  - Single dollar signs: `$formula$`
  - Double dollar signs: `$$formula$$`
  - LaTeX brackets: `\[formula\]`
  - LaTeX parentheses: `\(formula\)`

- **Smart Processing**
  - Intelligent space handling around formulas
  - Preserves line breaks while removing empty lines
  - Maintains non-formula text formatting
  - Batch conversion support

- **User Experience**
  - Modern, responsive web interface
  - Automatic result copying
  - Real-time preview
  - Mobile-friendly design

## Installation

### Prerequisites

- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer and resolver

### Setup

1. Install uv (if not already installed)
```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or via pip
pip install uv
```

2. Clone the repository
```bash
git clone https://github.com/ChennoShen239/FeishuConvert.git
cd FeishuConvert
```

3. Create a virtual environment and install dependencies
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e .
```

Alternatively, you can use uv to run the app directly without activating the virtual environment:
```bash
uv run python app.py
```

## Usage

1. Start the application
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:3000
```

3. Paste your text containing mathematical formulas into the input field

4. Click "Convert" to process the text

5. The converted text will be automatically copied to your clipboard

## Examples

Input:
```
If consumers expect that the productivity parameter will be equal to $\alpha$ next period, then:
\[\beta(1-\theta)\alpha f^{\prime}(k^d)=1\]
```

Output:
```
If consumers expect that the productivity parameter will be equal to $$ \alpha $$ next period, then:
$$ \beta(1-\theta)\alpha f^{\prime}(k^d)=1 $$
```

## Technical Details

### Dependencies

- Flask 3.0.0 - Web framework
- regex 2023.10.3 - Enhanced regular expression support

### Project Management

This project uses [uv](https://github.com/astral-sh/uv) for fast and reliable dependency management. The project configuration is defined in `pyproject.toml`.

### Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to all contributors who have helped with the project
- Special thanks to the Flask and regex package maintainers

## Contact

Project Link: [https://github.com/ChennoShen239/FeishuConvert](https://github.com/ChennoShen239/FeishuConvert)

---

Made with ❤️ for the Feishu community