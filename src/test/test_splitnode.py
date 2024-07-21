import unittest
from splitnode import split_nodes_image, split_nodes_link
from textnode import TextNode
from constants import text_type_image, text_type_link, text_type_text


class TextSplitNode(unittest.TestCase):

    def test_splitimg(self):
        text = "this is a text with embedded image ![image](https://linkgoeshere.com) and it will show if its valid"
        actual = split_nodes_image([TextNode(text, 'text')])
        expected = [TextNode("this is a text with embedded image ", text_type_text),TextNode("image",text_type_image,"https://linkgoeshere.com"), TextNode(" and it will show if its valid", text_type_text)]
        self.assertEqual(actual, expected)

    def test_splitlink(self):
        text = "this is a text with embedded image [image](https://linkgoeshere.com) and it will show if its valid"
        actual = split_nodes_link([TextNode(text, text_type_text)])
        expected = [TextNode("this is a text with embedded image ", text_type_text),TextNode("image", text_type_link ,"https://linkgoeshere.com"), TextNode(" and it will show if its valid", text_type_text)]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

