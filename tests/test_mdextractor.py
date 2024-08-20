import unittest
from mdextractor import extract_md_blocks


class TestMDExtractor(unittest.TestCase):
    def test_multiple_blocks(self):
        text = """
```
block 1
```
some text or not
```
block 2
```
"""
        self.assertEqual(extract_md_blocks(text), ["block 1", "block 2"])

    def test_with_language_specifier(self):
        text = """
```sometype
block1
```
"""
        self.assertEqual(extract_md_blocks(text), ["block1"])

    def test_single_line(self):
        text = "sometext ```python example```"
        self.assertEqual(extract_md_blocks(text), ["example"])

    def test_no_blocks(self):
        text = "No code blocks here."
        self.assertEqual(extract_md_blocks(text), [])

    def test_empty_string(self):
        self.assertEqual(extract_md_blocks(""), [])

    def test_whitespace_only_string(self):
        self.assertEqual(extract_md_blocks("     "), [])

    def test_malformed_fences(self):
        text = "```incomplete code block"
        self.assertEqual(extract_md_blocks(text), [])

    def test_nested_code_blocks(self):
        text = """
```
Outer ```inner``` end
```
"""
        self.assertEqual(extract_md_blocks(text), ["Outer", "end"])

    def test_consecutive_backticks(self):
        text = "Here is an example of `inline code` and a block: ```code block```"
        self.assertEqual(extract_md_blocks(text), ["block"])

    def test_incorrect_code_block(self):
        text = "```block1"
        self.assertEqual(extract_md_blocks(text), [])


if __name__ == '__main__':
    unittest.main()