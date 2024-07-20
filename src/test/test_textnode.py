import unittest

from textnode import TextNode, text_node_to_html_node
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text Node", "bold")
        self.assertEqual(node.url, None)

    def test_txttype_neq(self):
        node = TextNode("This is a test node", "", "http://example.com")
        node2 = TextNode("This is a test node", "italic", "http://example.com")
        self.assertNotEqual(node, node2)

    def test_txt_to_leaf(self):
        node = TextNode("bold tag", "bold")
        lf = LeafNode("b", "bold tag")

        self.assertEqual(str(text_node_to_html_node(node)), str(lf))

if __name__ == "__main__":
    unittest.main()

