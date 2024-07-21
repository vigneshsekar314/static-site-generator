import unittest
from splitnode import split_nodes_image, split_nodes_link
from textnode import TextNode


class TextSplitNode(unittest.TestCase):

    def test_splitimg(self):
        text = "this is a text with embedded image ![image](https://linkgoeshere.com) and it will show if its valid"
        actual = split_nodes_image([TextNode(text, 'text')])
        expected = [TextNode("this is a text with embedded image ", "text"),TextNode("image","link","https://linkgoeshere.com"), TextNode(" and it will show if its valid", "text")]
        self.assertEqual(actual, expected)

    def test_splitlink(self):
        text = "this is a text with embedded image [image](https://linkgoeshere.com) and it will show if its valid"
        actual = split_nodes_link([TextNode(text,'text')])
        expected = [TextNode("this is a text with embedded image ", "text"),TextNode("image","link","https://linkgoeshere.com"), TextNode(" and it will show if its valid", "text")]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

