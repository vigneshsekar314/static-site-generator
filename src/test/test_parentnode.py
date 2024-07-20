from parentnode import ParentNode
from leafnode import LeafNode

import unittest

class TestParentNode(unittest.TestCase):

    def test_children_none(self):
        with self.assertRaises(ValueError):
            pn = ParentNode("div", None, {"class":"lowkey"})
            pn.to_html()

    def test_empty_tag(self):
        with self.assertRaises(ValueError):
            pan = ParentNode("", [LeafNode("p", "east or west, vim is best :) !!")])
            pan.to_html()

    def test_None_tag(self):
        with self.assertRaises(ValueError):
            pad = ParentNode(None, [LeafNode("p", "wingarium jutsu")])
            pad.to_html()

    def test_html_with_leaves(self):
        pr = ParentNode("div", [LeafNode("p", "CRPG is the best genre"), LeafNode("p", "take a deep look at the python logo ... -\_(*-*)_/-"), LeafNode("p", "why vim? No, why anything other than vim?")], {"align": "center", "bgcolor":"brown"})
        html = "<div align=\"center\" bgcolor=\"brown\"><p>CRPG is the best genre</p><p>take a deep look at the python logo ... -\_(*-*)_/-</p><p>why vim? No, why anything other than vim?</p></div>"
        self.assertEqual(pr.to_html(), html)

    def test_html_with_parent(self):
        pt = ParentNode("div",[ParentNode("a", [LeafNode(None,"Set your heart ablaze")], {"href":"http://example.com"})], {"align":"center"})
        htm = "<div align=\"center\"><a href=\"http://example.com\">Set your heart ablaze</a></div>"
        self.assertEqual(pt.to_html(), htm)


if __name__ == "__main__":
    unittest.main()



            
            



