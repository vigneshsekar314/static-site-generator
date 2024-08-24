import sys
sys.path.insert(0, "/home/vignesh/workspace/github.com/vigneshsekar314/staticSiteGen/src")
import unittest
from blocks import block_to_block


class TestBlock2Block(unittest.TestCase):

    def test_check_all_heading(self):
        block = "# The adventures of my mind."
        block_type = block_to_block(block)
        self.assertEqual(block_type, "heading")

    def test_check_invalid_heading(self):
        block = "# The adventures of my mind.\nThe story begins with the awareness born within the mind."
        block_type = block_to_block(block)
        self.assertEqual(block_type, "paragraph")

    def test_check_code(self):
        block = "```let infinite = recursion_without_exit_condition()\nlet finite = recursion()```"
        block_type = block_to_block(block)
        self.assertEqual(block_type, "code")

    def test_invalid_code(self):
        block = "```let infinite = recursion_without_exit_condition()\nlet finite = recursion()``` is a code block."
        block_type = block_to_block(block)
        self.assertEqual(block_type, "paragraph")

    def test_quote(self):
        block = "> A nice winter should be cold.\n> The sayings that look deep and declarative are not quotes."
        block_type = block_to_block(block)
        self.assertEqual(block_type, "quote")

    def test_invalid_quote(self):
        block = "> A nice winter should be cold.\n> The sayings that look deep and declarative are not quotes.\nQuotes should be short but not dumb."
        block_type = block_to_block(block)
        self.assertEqual(block_type, "paragraph")

    def test_unordered(self):
        block = "* Take a spoon of attention.\n* Combine with effort.\n* And voila you did some work."
        block_type = block_to_block(block)
        self.assertEqual(block_type, "unordered_list")

    def test_invalid_unordered(self):
        block = "* Take a spoon of attention.\n* Combine with effort.\n* And voila you did some work.\n*Add some stress at the end."
        block_type = block_to_block(block)
        self.assertEqual(block_type, "paragraph")

    def test_ordered(self):
        block = "1. Take a spoon of attention.\n2. Combine with effort.\n3. And voila you did some work."
        block_type = block_to_block(block)
        self.assertEqual(block_type, "ordered_list")
        

    def test_invalid_ordered(self):
        block = "1. Take a spoon of attention.\n2. Combine with effort.\n3. And voila you did some work.\n4.Make sure to add some stresss at the end."
        block_type = block_to_block(block)
        self.assertEqual(block_type, "paragraph")

    def test_paragraph(self):
        block = "Do not underestimate the power of simple sentences."
        block_type = block_to_block(block)
        self.assertEqual(block_type, "paragraph")

if __name__ == "__main__":
    unittest.main()