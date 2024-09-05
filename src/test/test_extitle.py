import sys
sys.path.insert(0, "/home/vignesh/workspace/github.com/vigneshsekar314/staticSiteGen/src")
from unittest import TestCase, main
from generatepage import extract_title


class TestExtractTitle(TestCase):

    def test_h1(self):
        para = "# Heading of the century\n\nWhere there is a will there is a program"
        title = extract_title(para)
        self.assertEqual(title, "Heading of the century")


    def test_h2(self):
        para = "## Heading of the centuries\n\nWhere there is a will there is a program"
        title = extract_title(para)
        self.assertEqual(title, "Heading of the centuries")

    def test_h3(self):
        para = "### Heading of the not so important century\n\nWhere there is a will there is a program"
        title = extract_title(para)
        self.assertEqual(title, "Heading of the not so important century")
    
    def test_h4(self):
        para = "#### Heading of the nobody cares century\n\nWhere there is a will there is a program"
        title = extract_title(para)
        self.assertEqual(title, "Heading of the nobody cares century")

    def test_h5(self):
        para = "##### Heading of the why does it matter\n\nWhere there is a will there is a program"
        title = extract_title(para)
        self.assertEqual(title, "Heading of the why does it matter")

    def test_h6(self):
        para = "###### Heading of the wait, it exists\n\nWhere there is a will there is a program"
        title = extract_title(para)
        self.assertEqual(title, "Heading of the wait, it exists")


if __name__ == "__main__":
    main()