from flask import Flask, request, render_template_string
import regex as re

app = Flask(__name__)

def convert_math_delimiters(text):
    # 匹配所有可能的数学公式格式并保持公式内容不变
    patterns = [
        (r'\$([^\$]+?)\$', lambda m: f' $${m.group(1).strip()}$$ '),  # 单$
        (r'\$\$([^\$]+?)\$\$', lambda m: f' $${m.group(1).strip()}$$ '),  # 双$
        (r'\\\[(.*?)\\\]', lambda m: f' $${m.group(1).strip()}$$ '),  # \[ \]
        (r'\\\((.*?)\\\)', lambda m: f' $${m.group(1).strip()}$$ ')  # \( \)
    ]
    
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)
    
    # 处理多余的空格
    # 1. 处理连续空格
    text = re.sub(r'\s+', ' ', text)
    
    # 2. 确保$$与普通文本之间只有一个空格
    text = re.sub(r'\s+\$\$', ' $$', text)
    text = re.sub(r'\$\$\s+', '$$ ', text)
    
    return text.strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    converted_text = ''
    if request.method == 'POST':
        input_text = request.form.get('input_text', '')
        converted_text = convert_math_delimiters(input_text)
    
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
                font-family: var(--font-family);
                letter-spacing: -0.02em;
            }

            .subtitle {
                font-size: 20px;
                color: #86868B;
                margin-bottom: 30px;
                font-style: italic;
                font-family: var(--font-family);
            }

            .content {
                padding: 40px;
            }

            label {
                display: block;
                font-size: 16px;
                font-weight: 400;
                margin-bottom: 8px;
                color: #86868B;
                font-family: var(--font-family);
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
                font-family: var(--font-family);
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

            .result h3 {
                font-size: 18px;
                font-weight: 500;
                margin-bottom: 16px;
                color: var(--text-color);
            }

            .result textarea {
                background-color: #F5F5F7;
                border-color: transparent;
            }

            .result textarea:focus {
                background-color: #F5F5F7;
                border-color: transparent;
                box-shadow: none;
            }

            @media (max-width: 600px) {
                body {
                    padding: 20px 10px;
                }

                .header, .content {
                    padding: 20px;
                }

                h1 {
                    font-size: 24px;
                }
            }

            .result-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 16px;
            }

            .result-header h3 {
                margin: 0;
                font-size: 18px;
                font-weight: 500;
                white-space: nowrap;
            }

            .features {
                margin: 20px 0 30px;
                padding: 20px;
                background-color: rgba(0, 122, 255, 0.05);
                border-radius: var(--border-radius);
                font-family: var(--font-family);
            }

            .features h2 {
                font-size: 24px;
                font-weight: 600;
                margin-bottom: 16px;
                color: var(--text-color);
                font-family: var(--font-family);
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

            .features li:before {
                content: "•";
                color: var(--primary-color);
                font-weight: bold;
                margin-right: 8px;
            }

            .features li:last-child {
                margin-bottom: 0;
            }

            .example {
                font-family: monospace;
                background-color: #F5F5F7;
                padding: 2px 4px;
                border-radius: 4px;
                color: #666;
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
            }

            .copy-button:hover {
                background-color: #0066CC;
                transform: translateY(-1px);
            }

            .copy-button:active {
                transform: translateY(0);
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
                font-size: 14px;
                opacity: 0;
                transition: opacity 0.2s ease;
                font-family: var(--font-family);
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
                font-size: 16px;
                transition: color 0.2s ease;
                font-family: var(--font-family);
            }

            .github-link:hover {
                color: var(--primary-color);
            }

            .github-link svg {
                margin-right: 6px;
                width: 20px;
                height: 20px;
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
                        <li>Support multiple formula formats: single <span class="example">$...$</span>, double <span class="example">$$...$$</span>, <span class="example">\[...\]</span> and <span class="example">\(...\)</span></li>
                        <li>Auto-convert to Feishu format: <span class="example">$$formula$$</span></li>
                        <li>Smart space handling: no spaces within formulas, one space between formula and text</li>
                        <li>Auto-copy: results are automatically copied to clipboard</li>
                        <li>Batch conversion: convert multiple formulas at once</li>
                        <li>Format preservation: maintain all non-formula text formatting</li>
                    </ul>
                </div>
                <form id="convertForm" onsubmit="handleSubmit(event)">
                    <div>
                        <label for="input_text">Input Markdown Text</label>
                        <textarea 
                            name="input_text" 
                            id="input_text" 
                            placeholder="Paste your Markdown text here, for example:
hello $1233$ and \(2321\) and \[23124\]"
                        >{{ request.form.get('input_text', '') }}</textarea>
                    </div>
                    <button type="submit">Convert</button>
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
            function handleSubmit(event) {
                event.preventDefault();
                const form = event.target;
                const formData = new FormData(form);

                fetch('/', {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.text())
                .then(html => {
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(html, 'text/html');
                    const newResult = doc.getElementById('result');
                    if (newResult) {
                        document.getElementById('result').value = newResult.value;
                        document.getElementById('result-section').style.display = 'block';
                        copyResult();
                    }
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
                    console.error('复制失败:', err);
                });
            }
        </script>
    </body>
    </html>
    '''
    
    return render_template_string(html_template, converted_text=converted_text)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True) 