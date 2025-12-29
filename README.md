# FeishuConvert

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Convert LaTeX/Markdown math delimiters to Feishu-compatible `$$formula$$` format.

## Supported Formats

- `$formula$` → `$$formula$$`
- `$$formula$$` → `$$formula$$` (preserved)
- `\[formula\]` → `$$formula$$`
- `\(formula\)` → `$$formula$$`

## Quick Start

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone & setup
git clone https://github.com/ChennoShen239/FeishuConvert.git
cd FeishuConvert
uv sync

# Run
uv run python app.py
# or
python app.py
```

Access at `http://127.0.0.1:3000`

## Example

**Input:**
```
$\alpha$ and \[\beta(1-\theta)\alpha f^{\prime}(k^d)=1\]
```

**Output:**
```
$$ \alpha $$ and $$ \beta(1-\theta)\alpha f^{\prime}(k^d)=1 $$
```

## Tech Stack

- **Backend:** Flask 3.0.0
- **Regex:** regex 2023.10.3 (full regex support)
- **Package Manager:** uv
- **Python:** ≥3.8

## Implementation

- Regex-based delimiter conversion with lookahead/lookbehind
- Smart whitespace handling (preserves spacing, removes empty lines)
- Batch processing support
- Auto-copy to clipboard via Web API

## License

MIT
