from flask import Flask, request, render_template_string
import regex as re

app = Flask(__name__)

def convert_math_delimiters(text):
    """Convert Markdown math delimiters to Feishu compatible format.

    Args:
        text (str): Markdown text containing math formulas

    Returns:
        str: Converted text with Feishu compatible math delimiters
    """
    def replace_match(match):
        formula = match.group(1).strip()
        return f"$${formula}$$"

    # 保护已有的$$公式
    text = re.sub(r"\$\$([^\$]+)\$\$", lambda m: f"__DOUBLE_DOLLAR_{m.group(1)}_END_DOUBLE_DOLLAR__", text)

    # 转换各种公式定界符
    text = re.sub(r"(?<!\$)\$([^\$]+?)\$(?!\$)", replace_match, text)
    text = re.sub(r"\\\[(.*?)\\\]", replace_match, text, flags=re.DOTALL)
    text = re.sub(r"\\\((.*?)\\\)", replace_match, text)

    # 恢复被保护的$$公式
    text = text.replace("__DOUBLE_DOLLAR_", "$$").replace("_END_DOUBLE_DOLLAR__", "$$")

    result = ""
    in_math = False
    for part in re.split(r"(\$\$.*?\$\$)", text):
        if part.startswith("$$") and part.endswith("$$"):
            if result and not result.endswith(" ") and not in_math and not result.endswith(tuple([",", ".", ";", "!", "?"])):
                result += " "
            result += part
            in_math = True
        elif part:
            lines = part.splitlines()
            non_empty_lines = [line.strip() for line in lines if line.strip()]
            cleaned_part = "\n".join(non_empty_lines)
            cleaned_part = cleaned_part.strip()
            if cleaned_part: # 如果处理后的部分不为空
                if result and cleaned_part and not result.endswith(" ") and not result.endswith(tuple([",", ".", ";", "!", "?"])):
                  if in_math:
                    result += " "
                  elif not cleaned_part.startswith(tuple([",", ".", ";", "!", "?"])):
                    result += " "
                result += cleaned_part
            in_math = False
    return result.strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    """Handle requests to the main page.

    Returns:
        str: Rendered HTML template with conversion results
    """
    converted_text = ''
    if request.method == 'POST':
        input_text = request.form.get('input_text', '')
        converted_text = convert_math_delimiters(input_text)
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return converted_text
    
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Markdown Formula Converter</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
        <style>
            :root {
                --primary-color: #007AFF;
                --background-color: #F5F5F7;
                --surface-color: #FFFFFF;
                --text-color: #1D1D1F;
                --border-radius: 12px;
                --transition-speed: 0.3s;
                --font-family: 'Crimson Pro', serif;
            }

            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                background-color: var(--background-color);
                color: var(--text-color);
                line-height: 1.5;
                -webkit-font-smoothing: antialiased;
                padding: 40px 20px;
                font-family: var(--font-family);
            }

            .container {
                max-width: 800px;
                margin: 0 auto;
                background-color: var(--surface-color);
                border-radius: var(--border-radius);
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
                overflow: hidden;
            }

            .header {
                padding: 40px;
                text-align: center;
                border-bottom: 1px solid rgba(0, 0, 0, 0.1);
            }

            h1 {
                font-size: 42px;
                font-weight: 600;
                color: var(--text-color);
                margin-bottom: 10px;
                letter-spacing: -0.02em;
            }

            .subtitle {
                font-size: 20px;
                color: #86868B;
                margin-bottom: 30px;
                font-style: italic;
            }

            .content {
                padding: 40px;
            }

            .features {
                margin: 20px 0 30px;
                padding: 20px;
                background-color: rgba(0, 122, 255, 0.05);
                border-radius: var(--border-radius);
            }

            .features h2 {
                font-size: 24px;
                font-weight: 600;
                margin-bottom: 16px;
                color: var(--text-color);
            }

            .features ul {
                list-style-type: none;
                padding: 0;
                margin: 0;
            }

            .features li {
                display: flex;
                align-items: flex-start;
                margin-bottom: 12px;
                font-size: 16px;
                line-height: 1.6;
                color: #666;
            }

            .features li::before {
                content: "•";
                color: var(--primary-color);
                font-weight: bold;
                margin-right: 8px;
            }

            .example {
                font-family: monospace;
                background-color: #F5F5F7;
                padding: 2px 4px;
                border-radius: 4px;
                color: #666;
                user-select: none;
                white-space: nowrap;
            }

            .preview-container {
                display: flex;
                gap: 20px;
                margin-bottom: 20px;
            }

            .input-container {
                flex: 1;
            }

            label {
                display: block;
                font-size: 16px;
                font-weight: 400;
                margin-bottom: 8px;
                color: #86868B;
            }

            textarea {
                width: 100%;
                height: 180px;
                padding: 16px;
                border: 1px solid rgba(0, 0, 0, 0.1);
                border-radius: var(--border-radius);
                font-size: 16px;
                line-height: 1.5;
                color: var(--text-color);
                background-color: #FAFAFA;
                transition: all var(--transition-speed);
                resize: vertical;
                margin-bottom: 20px;
                font-family: var(--font-family);
            }

            button {
                display: block;
                width: 100%;
                padding: 16px;
                background-color: var(--primary-color);
                color: white;
                border: none;
                border-radius: var(--border-radius);
                font-size: 16px;
                font-weight: 600;
                cursor: pointer;
                transition: all var(--transition-speed);
            }

            button:hover {
                background-color: #0066CC;
                transform: translateY(-1px);
            }

            button:active {
                transform: translateY(0);
            }

            .result {
                margin-top: 30px;
                padding-top: 30px;
                border-top: 1px solid rgba(0, 0, 0, 0.1);
            }

            .result-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 16px;
            }

            .result-header h3 {
                font-size: 24px;
                font-weight: 600;
                margin: 0;
                white-space: nowrap;
            }

            .copy-button {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                padding: 6px 12px;
                background-color: var(--primary-color);
                color: white;
                border: none;
                border-radius: var(--border-radius);
                font-size: 13px;
                font-weight: 500;
                cursor: pointer;
                transition: all 0.2s ease;
                width: auto;
            }

            .copy-button.success {
                background-color: #34C759;
            }

            .toast {
                position: fixed;
                bottom: 20px;
                left: 50%;
                transform: translateX(-50%);
                background-color: rgba(0, 0, 0, 0.8);
                color: white;
                padding: 8px 16px;
                border-radius: 20px;
                font-size: 13px;
                opacity: 0;
                transition: opacity 0.2s ease;
            }

            .toast.show {
                opacity: 1;
            }

            .footer {
                text-align: center;
                padding: 20px;
                margin-top: 40px;
                border-top: 1px solid rgba(0, 0, 0, 0.1);
            }

            .github-link {
                display: inline-flex;
                align-items: center;
                color: #666;
                text-decoration: none;
                font-size: 14px;
                transition: color 0.2s ease;
            }

            .github-link:hover {
                color: var(--primary-color);
            }

            .github-link svg {
                margin-right: 6px;
                width: 20px;
                height: 20px;
            }

            @media (max-width: 768px) {
                .preview-container {
                    flex-direction: column;
                }

                body {
                    padding: 20px 10px;
                }

                .header, .content {
                    padding: 20px;
                }

                h1 {
                    font-size: 32px;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Markdown Formula Converter</h1>
                <div class="subtitle">Convert Markdown formulas to Feishu compatible format</div>
            </div>
            <div class="content">
                <div class="features">
                    <h2>Features</h2>
                    <ul>
                        <li>Support multiple formula formats: single <code class="example">$...$</code>, double <code class="example">$$...$$</code>, <code class="example">\\[...\\]</code> and <code class="example">\\(...\\)</code></li>
                        <li>Auto-convert to Feishu format: <code class="example">$$</code><i>formula</i><code class="example">$$</code></li>
                        <li>Smart space handling: no spaces within formulas, one space between formula and text</li>
                        <li>Auto-copy: results are automatically copied to clipboard</li>
                        <li>Batch conversion: convert multiple formulas at once</li>
                        <li>Format preservation: maintain all non-formula text formatting</li>
                    </ul>
                </div>
                <form id="convertForm">
                    <div class="input-container">
                        <label for="input_text">Input Markdown Text</label>
                        <textarea 
                            name="input_text" 
                            id="input_text" 
                            placeholder="Paste your Markdown text here, for example:
hello $\\frac{1}{2}$ and \\(x^2\\) and \\[E=mc^2\\]"
                        >{{ request.form.get('input_text', '') }}</textarea>
                    </div>
                    <button type="button" onclick="handleConvert()">Convert</button>
                </form>
                <div class="result" id="result-section" style="display: {{ 'block' if converted_text else 'none' }}">
                    <div class="result-header">
                        <h3>Result</h3>
                        <button class="copy-button" onclick="copyResult()">Copy</button>
                    </div>
                    <textarea id="result" readonly>{{ converted_text }}</textarea>
                </div>
            </div>
            <div class="footer">
                <a href="https://github.com/ChennoShen239/FeishuConvert" class="github-link" target="_blank">
                    <svg viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
                    </svg>
                    View Source on GitHub
                </a>
            </div>
        </div>
        <div class="toast" id="toast">Copied</div>

        <script>
            function handleConvert() {
                const input = document.getElementById('input_text').value;
                fetch('/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-Requested-With': 'XMLHttpRequest'
                    },
                    body: new URLSearchParams({
                        'input_text': input
                    })
                })
                .then(response => response.text())
                .then(text => {
                    const result = document.getElementById('result');
                    const resultSection = document.getElementById('result-section');
                    result.value = text;
                    resultSection.style.display = 'block';
                    copyResult();
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            }

            function copyResult() {
                const resultText = document.getElementById('result');
                const copyButton = document.querySelector('.copy-button');
                const toast = document.getElementById('toast');
                
                resultText.select();
                navigator.clipboard.writeText(resultText.value).then(() => {
                    copyButton.classList.add('success');
                    toast.classList.add('show');
                    
                    setTimeout(() => {
                        copyButton.classList.remove('success');
                        toast.classList.remove('show');
                    }, 1500);
                }).catch(err => {
                    console.error('Copy failed:', err);
                });
            }
        </script>
    </body>
    </html>
    '''
    
    return render_template_string(html_template, converted_text=converted_text)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)