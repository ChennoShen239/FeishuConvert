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
        <title>Markdown公式转换器</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            :root {
                --primary-color: #007AFF;
                --background-color: #F5F5F7;
                --surface-color: #FFFFFF;
                --text-color: #1D1D1F;
                --border-radius: 12px;
                --transition-speed: 0.3s;
            }

            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Helvetica Neue", Arial, sans-serif;
            }

            body {
                background-color: var(--background-color);
                color: var(--text-color);
                line-height: 1.5;
                -webkit-font-smoothing: antialiased;
                padding: 40px 20px;
            }

            .container {
                max-width: 800px;
                margin: 0 auto;
                background-color: var(--surface-color);
                border-radius: var(--border-radius);
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
                overflow: hidden;
                transition: transform var(--transition-speed);
            }

            .container:hover {
                transform: translateY(-2px);
            }

            .header {
                padding: 40px;
                text-align: center;
                border-bottom: 1px solid rgba(0, 0, 0, 0.1);
            }

            h1 {
                font-size: 32px;
                font-weight: 600;
                color: var(--text-color);
                margin-bottom: 10px;
            }

            .subtitle {
                font-size: 16px;
                color: #86868B;
                margin-bottom: 30px;
            }

            .content {
                padding: 40px;
            }

            label {
                display: block;
                font-size: 14px;
                font-weight: 500;
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
            }

            textarea:focus {
                outline: none;
                border-color: var(--primary-color);
                box-shadow: 0 0 0 3px rgba(0, 122, 255, 0.1);
                background-color: var(--surface-color);
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
                font-weight: 500;
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

            .copy-button {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                padding: 8px 16px;
                background-color: var(--surface-color);
                color: var(--primary-color);
                border: 1px solid var(--primary-color);
                border-radius: var(--border-radius);
                font-size: 14px;
                font-weight: 500;
                cursor: pointer;
                transition: all var(--transition-speed);
                margin-top: 12px;
            }

            .copy-button:hover {
                background-color: rgba(0, 122, 255, 0.1);
            }

            .copy-button:active {
                background-color: rgba(0, 122, 255, 0.2);
            }

            .copy-button.success {
                background-color: #34C759;
                color: white;
                border-color: #34C759;
            }

            .copy-feedback {
                position: fixed;
                top: 20px;
                left: 50%;
                transform: translateX(-50%);
                background-color: rgba(52, 199, 89, 0.9);
                color: white;
                padding: 12px 24px;
                border-radius: var(--border-radius);
                font-size: 14px;
                font-weight: 500;
                opacity: 0;
                transition: opacity var(--transition-speed);
                pointer-events: none;
                z-index: 1000;
            }

            .copy-feedback.show {
                opacity: 1;
            }

            .result-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 16px;
                white-space: nowrap;
            }

            .result-header h3 {
                margin: 0;
                font-size: 18px;
                font-weight: 500;
            }

            .features {
                margin: 20px 0 30px;
                padding: 20px;
                background-color: rgba(0, 122, 255, 0.05);
                border-radius: var(--border-radius);
            }

            .features h2 {
                font-size: 18px;
                font-weight: 500;
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
                font-size: 14px;
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
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Markdown公式转换器</h1>
                <div class="subtitle">将普通Markdown公式转换为飞书兼容格式</div>
            </div>
            <div class="content">
                <div class="features">
                    <h2>功能说明</h2>
                    <ul>
                        <li>支持多种公式格式转换：单个<span class="example">$...$</span>、双<span class="example">$$...$$</span>、<span class="example">\[...\]</span>和<span class="example">\(...\)</span></li>
                        <li>自动统一转换为飞书支持的格式：<span class="example">$$公式$$</span></li>
                        <li>智能处理空格：公式内部无空格，公式与文本之间保持一个空格</li>
                        <li>自动复制：转换后的结果会自动复制到剪贴板</li>
                        <li>支持批量转换：可一次性转换多个公式</li>
                        <li>保持原文格式：除公式外的其他文本格式保持不变</li>
                    </ul>
                </div>
                <form method="POST">
                    <div>
                        <label for="input_text">输入Markdown文本</label>
                        <textarea 
                            name="input_text" 
                            id="input_text" 
                            placeholder="在这里粘贴您的Markdown文本，例如：
hello $1233$ and \(2321\) and \[23124\]"
                        >{{ request.form.get('input_text', '') }}</textarea>
                    </div>
                    <button type="submit">转换</button>
                </form>
                {% if converted_text %}
                <div class="result">
                    <div class="result-header">
                        <h3>转换结果</h3>
                        <button class="copy-button" onclick="copyResult()">
                            复制结果
                        </button>
                    </div>
                    <textarea id="result" readonly>{{ converted_text }}</textarea>
                </div>
                {% endif %}
            </div>
        </div>
        <div class="copy-feedback" id="copyFeedback">已复制到剪贴板</div>

        <script>
            function copyResult() {
                const resultText = document.getElementById('result');
                const copyButton = document.querySelector('.copy-button');
                const feedback = document.getElementById('copyFeedback');
                
                // 选择文本
                resultText.select();
                
                // 复制到剪贴板
                navigator.clipboard.writeText(resultText.value).then(() => {
                    // 显示成功状态
                    copyButton.classList.add('success');
                    copyButton.textContent = '复制成功';
                    feedback.classList.add('show');
                    
                    // 3秒后恢复原状
                    setTimeout(() => {
                        copyButton.classList.remove('success');
                        copyButton.textContent = '复制结果';
                        feedback.classList.remove('show');
                    }, 3000);
                }).catch(err => {
                    console.error('复制失败:', err);
                });
            }

            // 如果存在转换结果，自动复制
            window.onload = function() {
                const resultText = document.getElementById('result');
                if (resultText) {
                    copyResult();
                }
            }
        </script>
    </body>
    </html>
    '''
    
    return render_template_string(html_template, converted_text=converted_text)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True) 