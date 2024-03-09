[![PyPI version](https://badge.fury.io/py/mdextractor.svg)](https://badge.fury.io/py/mdextractor)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/mdextractor)](https://pepy.tech/project/mdextractor)

# mdextractor

`mdextractor` is a Python package designed for extracting code blocks from Markdown text. It efficiently identifies blocks enclosed in triple backticks (\`\`\`), optionally preceded by language identifiers, and extracts their contents.

## Installation

To install `mdextractor`, use pip:

```bash
pip install mdextractor
```

## Usage

Using `mdextractor` is straightforward. Here's an example:

```python
from mdextractor import extract_md_blocks

text = """
\`\`\`python
print("Hello, Markdown!")
\`\`\`
"""

blocks = extract_md_blocks(text)
print(blocks)
# Output: ['print("Hello, Markdown!")']
```

This package is useful in various applications where extracting code or preformatted text from Markdown is necessary.

## Features

- Efficient extraction of Markdown code blocks.
- Supports language specifiers following the opening backticks.
- Works with multi-line and single-line code blocks.
- Simple API with a single function call.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/chigwell/mdextractor/issues).

## License

`mdextractor` is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
