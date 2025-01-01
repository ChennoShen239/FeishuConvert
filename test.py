import regex as re

def convert_math_delimiters(text):
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

# 测试用例 (包含所有之前的测试用例和新的空行/换行测试用例)
test_cases = [
    # ... (之前的测试用例)
    r"""
    测试多行公式与文本混合，包含空行：

    \[

    \max_{x} f(x) = \int_{a}^{b} g(x, t) dt


    \]

    这是一段文本。

    另一段文本。

    """, # 测试多行公式和空行
    r"""
    测试只有空行的情况：


    """, # 测试只有空行
    "测试文本中的\n换行符是否保留。", #测试文本中的换行符
    "测试公式中的\n换行符是否保留：$\\frac{1}{\n2}$",
    r"""
    测试公式前后都有空行：

    $a$

    """,
    r"""测试公式内部和前后都有空行：

    $
    a

    $
    """
]

for test_case in test_cases:
    converted = convert_math_delimiters(test_case)
    print(f"Input:\n{test_case}")
    print(f"Output:\n{converted}")
    print("-" * 20)