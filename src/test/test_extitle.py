import sys
sys.path.insert(0, "/home/vignesh/workspace/github.com/vigneshsekar314/staticSiteGen/src")
from unittest import TestCase, main
from generatepage import extract_title


class TestExtractTitle(TestCase):

    def test_h1(self):
        para = "# Heading of the century\n\nWhere there is a will there is a program"
        title = extract_title(para)
        self.assertEqual(title, "h1")


    def test_h2(self):
        para = "## Heading of the century\n\nWhere there is a will there is a program"
        title = extract_title(para)
        self.assertEqual(title, "h2")

    def test_h3(self):
        para = "### Heading of the century\n\nWhere there is a will there is a program"
        title = extract_title(para)
        self.assertEqual(title, "h3")
    
    def test_h4(self):
        para = "#### Heading of the century\n\nWhere there is a will there is a program"
        title = extract_title(para)
        self.assertEqual(title, "h4")

    def test_h5(self):
        para = "##### Heading of the century\n\nWhere there is a will there is a program"
        title = extract_title(para)
        self.assertEqual(title, "h5")

    def test_h6(self):
        para = "###### Heading of the century\n\nWhere there is a will there is a program"
        title = extract_title(para)
        self.assertEqual(title, "h6")


if __name__ == "__main__":
    main()