from leafnode import LeafNode
import unittest


class LeafNodeTest(unittest.TestCase):

    def test_value_null(self):
        with self.assertRaises(ValueError):
            text = None
            lf = LeafNode("p", text)

    def test_no_tag_only_value(self):
        text_to_print = "this is a standard text"
        lf = LeafNode(None, text_to_print)
        self.assertEqual(lf.to_html(), text_to_print)

    def test_tag(self):
        text="marshmallow is good"
        html = "<p>" + text + "</p>"
        lf = LeafNode("p", text)
        self.assertEqual(lf.to_html(), html)

    def test_tag_with_attributes(self):
        text = "click me"
        html = "<a href=\"http://example.com\" bgcolor=\"blue\" class=\"anchor\">" + text + "</a>"
        lf = LeafNode("a", text, {"href":"http://example.com", "bgcolor":"blue", "class":"anchor"})
        self.assertEqual(lf.to_html(),html)


if __name__ == "__main__":
    unittest.main()

