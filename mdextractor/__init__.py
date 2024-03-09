import re


def extract_md_blocks(text):
    pattern = r"```(?:\w+\s+)?(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    return [block.strip() for block in matches]
