import sys
sys.path.insert(0, "/home/vignesh/workspace/github.com/vigneshsekar314/staticSiteGen/src")
import unittest
from markdown2html import markdown2HTML


class TestMarkdown2HTML(unittest.TestCase):

    def test_headings(self):
        md1 = "# heading 1 are the most important text in a webpage."
        md2 = "## heading 2 are the next important text in a webpage."
        md3 = "### heading 3 are used for important texts for users to read."
        md4 = "#### heading 4 are subtle topics to attract user attention."
        md5 = "##### heading 5 is something I don't know where it is being used."
        md6 = "###### heading 6 is a thing that exists. I don't even know why we use heading 5."
        md7 = "# Make it flashy.\n\n## Make it catchy."
        expected1 = "<h1>heading 1 are the most important text in a webpage.</h1>"
        expected2 = "<h2>heading 2 are the next important text in a webpage.</h2>"
        expected3 = "<h3>heading 3 are used for important texts for users to read.</h3>"
        expected4 = "<h4>heading 4 are subtle topics to attract user attention.</h4>"
        expected5 = "<h5>heading 5 is something I don't know where it is being used.</h5>"
        expected6 = "<h6>heading 6 is a thing that exists. I don't even know why we use heading 5.</h6>"
        expected7 = "<h1>Make it flashy.</h1><h2>Make it catchy.</h2>"
        actual1 = markdown2HTML(md1)
        actual2 = markdown2HTML(md2)
        actual3 = markdown2HTML(md3)
        actual4 = markdown2HTML(md4)
        actual5 = markdown2HTML(md5)
        actual6 = markdown2HTML(md6)
        actual7 = markdown2HTML(md7)
        self.assertEqual([actual1, actual2, actual3, actual4, actual5, actual6, actual7], [expected1, expected2, expected3, expected4, expected5, expected6, expected7])

    def test_paragraphs(self):
        md = "This is a normal paragraph.\n\nAdding multi-lines to check if it is recognizing it properly.\n\nThis is a simple test."
        expected = "<p>This is a normal paragraph.</p><p>Adding multi-lines to check if it is recognizing it properly.</p><p>This is a simple test.</p>"
        actual = markdown2HTML(md)
        self.assertEqual(actual, expected)

    def test_unordered_lists(self):
        md1 = "* Rule 1 of developer: get the job done, then iterate and make it better.\n* Rule 2 of a developer: write unit test so you don't embarass yourself.\n* Rule 3 of a developer: Play around and experiment to learn."
        md2 = "Important points for Debugging:\n\n* Keep breakpoints at regular intervals.\n* If an exception occured between breakpoints, debug line by line from the last hit breakpoint."
        expected1 = "<ul><li>Rule 1 of developer: get the job done, then iterate and make it better.</li><li>Rule 2 of a developer: write unit test so you don't embarass yourself.</li><li>Rule 3 of a developer: Play around and experiment to learn.</li></ul>"
        expected2 = "<p>Important points for Debugging:</p><ul><li>Keep breakpoints at regular intervals.</li><li>If an exception occured between breakpoints, debug line by line from the last hit breakpoint.</li></ul>"
        actual1 = markdown2HTML(md1)
        actual2 = markdown2HTML(md2)
        self.assertEqual([actual1, actual2], [expected1, expected2])

    def test_ordered_list(self):
        md1 = "1. Rule 1 of the 10x developer: never stop learning.\n2. Keep trying new things and expand your horizon.\n3. Go beyond the basics and understand the bottlenecks and strengths of framework.\n4. Build your own tools and use open-source to increase productivity."
        expected1 = "<ol><li>Rule 1 of the 10x developer: never stop learning.</li><li>Keep trying new things and expand your horizon.</li><li>Go beyond the basics and understand the bottlenecks and strengths of framework.</li><li>Build your own tools and use open-source to increase productivity.</li></ol>"
        actual1 = markdown2HTML(md1)
        md2 = "Tips for a good software development:\n\n1. Understand the requirements.\n2. Breakdown a complex problem into individual sub-units.\n3. Integrate each sub-unit.\n4. See the full picture instead of seeing each element as a sub-block."
        expected2 = "<p>Tips for a good software development:</p><ol><li>Understand the requirements.</li><li>Breakdown a complex problem into individual sub-units.</li><li>Integrate each sub-unit.</li><li>See the full picture instead of seeing each element as a sub-block.</li></ol>"
        actual2 = markdown2HTML(md2)
        self.assertEqual([actual1, actual2], [expected1, expected2])

    def test_blockquote(self):
        md1 = "> A quote must be short and concise, yet reveal a deep understanding of nature.\n> Quotes often are abstract and require some level of comprehension to apply it in everyday life."
        md2 = "Some good quotes here:\n\n> Education is the progressive discovery of our own ignorance.\n> As our island of knowledge expands, so does our shoreline of ignorance."
        expected1 = "<blockquote>A quote must be short and concise, yet reveal a deep understanding of nature.\nQuotes often are abstract and require some level of comprehension to apply it in everyday life.</blockquote>"
        expected2 = "<p>Some good quotes here:</p><blockquote>Education is the progressive discovery of our own ignorance.\nAs our island of knowledge expands, so does our shoreline of ignorance.</blockquote>"
        actual1 = markdown2HTML(md1)
        actual2 = markdown2HTML(md2)
        self.assertEqual([actual1, actual2], [expected1, expected2])

    def test_bold_italic(self):
        md1 = "*slantic text are trendy now.* **be strong, stand proud.**\n\n*There is both beauty and stupidity in bravery.*"
        expected1 = "<p><i>slantic text are trendy now.</i> <b>be strong, stand proud.</b></p><p><i>There is both beauty and stupidity in bravery.</i></p>"
        actual1 = markdown2HTML(md1)
        self.assertEqual(actual1, expected1)

    def test_code(self):
        md1 = "```const developer = make_your_own_thing(passion, creativity, curious, ideas);```\n\n```const artist = make_ordinary_unfamiliar();```"
        expected1 = "<pre><code>const developer = make_your_own_thing(passion, creativity, curious, ideas);</code></pre><pre><code>const artist = make_ordinary_unfamiliar();</code></pre>"
        actual1 = markdown2HTML(md1)
        self.assertEqual(actual1, expected1)

if __name__ == "__main__":
    unittest.main()