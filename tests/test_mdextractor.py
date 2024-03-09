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
        text = "sometext ```python example ```"
        self.assertEqual(extract_md_blocks(text), ["example"])

    def test_no_blocks(self):
        text = "No code blocks here."
        self.assertEqual(extract_md_blocks(text), [])

if __name__ == '__main__':
    unittest.main()