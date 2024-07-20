import unittest
from util import split_nodes_delimiter
from textnode import TextNode


class TestUtil(unittest.TestCase):

    def test_onlytext(self):
        n = TextNode("normal text", "text")
        newnode = split_nodes_delimiter([n], "`", "code")
        self.assertEqual(newnode, [TextNode("normal text","text")])

    def test_text_code(self):
        n = TextNode("`python != nodejs` is a code", "text")
        newnode = split_nodes_delimiter([n], "`", "code")
        result = [TextNode("python != nodejs", "code"), TextNode(" is a code","text")]
        self.assertEqual(newnode, result)

    def test_delimiter_open(self):
        n = TextNode("this is open `an open delimiter should throw error","text")
        with self.assertRaises(Exception):
            newnode = split_nodes_delimiter([n], "`", "code")

    def test_italic(self):
        n = TextNode("this is an *italic* text","text")
        newnode = split_nodes_delimiter([n], "*", "italic")
        result = [TextNode("this is an ", "text"), TextNode("italic","italic"), TextNode(" text","text")]
        self.assertEqual(newnode, result)

    def test_bold(self):
        n = TextNode("this is an **bold** text","text")
        newnode = split_nodes_delimiter([n], "**", "bold")
        result = [TextNode("this is an ", "text"), TextNode("bold","bold"), TextNode(" text","text")]
        self.assertEqual(newnode, result)

    def test_invalid_texttype(self):
        with self.assertRaises(ValueError):
            n = TextNode("this is testing an invalid text type", "text")
            newnode = split_nodes_delimiter([n], "*", "smug")

if __name__ == "__main__":
    unittest.main()

