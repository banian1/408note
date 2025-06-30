import re
from pathlib import Path
def convert_latex_delimiters(text):
    # 替换行间公式： \[ ... \] → $$ ... $$
    text = re.sub(r'\\\[(.*?)\\\]', r'$$\1$$', text, flags=re.DOTALL)
    
    # 替换行内公式： \( ... \) → $ ... $
    text = re.sub(r'\\\((.*?)\\\)', r'$\1$', text, flags=re.DOTALL)
    
    return text

def convert_mkdocs_to_obsidian(text):
    # 处理 !!! 和 ???，支持 title 和可选 collapse
    pattern = re.compile(r'''
        ^
        (?P<collapse>!{3}|\?{3})       # !!! 或 ???
        \s+
        (?P<type>\w+)                  # note / warning / tip 等
        \s+
        (?P<title>[^\n]+)              # 标题（不加引号）
        \n
        (?P<content>(?:[ \t]+.+\n?)*)  # 缩进内容（必须缩进）
        ''', re.MULTILINE | re.VERBOSE)

    def replacer(match):
        collapse = match.group("collapse")
        type_ = match.group("type").lower()
        title = match.group("title")
        content = match.group("content")

        # 去掉前四个空格
        content = ''.join(line[4:] if line.startswith('    ') else line for line in content.splitlines(keepends=True))

        # 构造 admonition 块
        result = f"```ad-{type_}\n"
        if title:
            result += f"title: {title}\n"
        if collapse.startswith('?'):
            result += "collapse: closed\n"
        result += f"{content}```\n"
        return result

    return re.sub(pattern, replacer, text)

input_root = Path(r"C:\Users\banian\Documents\Obsidian Vault\408")
output_root = Path("..")
output_root.mkdir(exist_ok=True)
for md_file in input_root.rglob("*.md"):
    relative_path = md_file.relative_to(input_root)
    output_file = output_root / relative_path
    output_file.parent.mkdir(parents=True, exist_ok=True)

    content = md_file.read_text(encoding="utf-8")
    converted = convert_latex_delimiters(content)
    output_file.write_text(converted, encoding="utf-8")