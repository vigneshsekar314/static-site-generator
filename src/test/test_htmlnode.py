import sys
sys.path.insert(0, "/home/vignesh/workspace/github.com/vigneshsekar314/staticSiteGen/src")
import unittest
from htmlnode import HTMLNode

class HtmlNodeTest(unittest.TestCase):

    def test_child_props_none(self):
        hnode = HTMLNode("p", "this is a para")
        self.assertEqual(hnode.children, None)
        self.assertEqual(hnode.props, None)
        
    def test_both_value_child_not_none(self):
        with self.assertRaises(ValueError):
            hnode = HTMLNode()

    def test_to_html_throw_error(self):
        with self.assertRaises(NotImplementedError):
            hnode = HTMLNode("a", "click here", None, {"href": "http://example.com", "target":"_blank"})
            hnode.to_html()

    def test_check_props(self):
            hnode = HTMLNode("a", "click here", None, {"href": "http://example.com", "target":"_blank"})
            self.assertEqual(hnode.props["href"], "http://example.com")

    def test_children(self):
            cnode = HTMLNode("p", "this is a para")
            hnode = HTMLNode("div",value=None,children=[cnode]) 
            self.assertEqual(hnode.children[0], cnode)

    def test_check_propstohtml(self):
            hnode = HTMLNode("a", "click here", None, {"href": "http://example.com", "target":"_blank"})
            self.assertEqual(hnode.props_to_html(), " href=\"http://example.com\" target=\"_blank\"")


if __name__ == "__main__":
    unittest.main()
