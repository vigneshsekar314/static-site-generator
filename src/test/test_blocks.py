import unittest
import sys
sys.path.insert(0, "/home/vignesh/workspace/github.com/vigneshsekar314/staticSiteGen/src")
from blocks import markdown_to_blocks


class TestBlocks(unittest.TestCase):

    def test_removespace(self):
        para = """
        This is a paragraph. It has some empty lines.


        But these empty lines should not come in the output.     


            
        """
        first_block = "This is a paragraph. It has some empty lines."
        second_block = "But these empty lines should not come in the output."
        expected = [first_block, second_block]
        actual = markdown_to_blocks(para)
        self.assertEqual(expected, actual)
    
    def test_multiline_split(self):
        para = """

        
        This is a paragraph. It has some empty lines.
        But these empty lines should not come in the output.     


        This is a continuous sequence of lines.
        # this is a heading
        ## this is a sub-heading
        ### this is a sub-sub-heading    
        """
        first_block = """This is a paragraph. It has some empty lines.
        But these empty lines should not come in the output."""
        second_block = """This is a continuous sequence of lines.
        # this is a heading
        ## this is a sub-heading
        ### this is a sub-sub-heading"""
        expected = [first_block, second_block]
        actual = markdown_to_blocks(para)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()