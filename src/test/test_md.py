import unittest
from md import extract_markdown_links


class TestMd(unittest.TestCase):

    def test_islinkshown(self):
        text = "this is a [link](https://example.com)"
        actual = extract_markdown_links(text)
        expected = [("link", "https://example.com")]
        self.assertEqual(actual, expected) 

