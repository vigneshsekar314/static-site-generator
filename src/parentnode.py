from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):

    def __init__(self, tag: str | None, children: [HTMLNode], props: dict | None=None) -> None:
        super().__init__(tag=tag, value=None, children=children, props=props)


    def to_html(self):
        if self.children is None or len(self.children) == 0:
            raise ValueError("pass children object to the constructor with atleast one child")
        if self.tag is None or self.tag == "":
            raise ValueError("tag property should not be None or empty")
        html_str = "<" + self.tag 
        if self.props is not None and len(self.props) > 0:
            html_str += self.props_to_html() + ">"
        else:
            html_str += ">"
        
        for child in self.children:
            if child is not None:
                html_str += child.to_html()

        html_str += "</" + self.tag + ">"
        return html_str

def main():
    ln = LeafNode("a", "click me", {"href":"http://example.com", "bgcolor":"blue"})
    ln2 = LeafNode("p", "this is a short statement", {"align":"center", "margin":"0 2"})
    ln3 = LeafNode("p", "I like markdown", {"align":"center", "margin":"0 2"})
    ln4 = LeafNode("p", "nvim is the best editor", {"align":"center", "margin":"0 2"})
    pn = ParentNode("div", [ln, ln2], {"class":"main", "color":"orange"})
    pn2 = ParentNode("div", [ln3, ln4], {"class":"branch", "color":"white"})
    pn3 = ParentNode("div", [pn, pn2], {"class":"top", "align":"center"}) 
    print(pn3.to_html())

if __name__ == "__main__":
    main()


