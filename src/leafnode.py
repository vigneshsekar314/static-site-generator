from htmlnode import HTMLNode


class LeafNode(HTMLNode):

    def __init__(self, tag: str | None, value: str, props: dict | None = None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self) -> str:
        html_str = ""
        if self.tag is not None:
            opening_tag: str = "<" + self.tag + ">" 
            closing_tag: str = "</" + self.tag + ">"
            if self.props is None:
                html_str =  opening_tag + str(self.value) + closing_tag
            else:
                html_str = "<" + self.tag 
                html_str += self.props_to_html() + ">"
                html_str += str(self.value) + closing_tag

        else:
            html_str = self.value

        return str(html_str)

def main():
    lf = LeafNode("p","hi how are yu?")
    lf2 = LeafNode("a", "click me", {"href":"http://example.com","bgcolor":"blue"})
    lf3 = LeafNode(None, value="I made a statement.")
    print(f"para: {lf.to_html()}")
    print(f"anchor: {lf2.to_html()}")
    print(f"text: {lf3.to_html()}")

if __name__ == "__main__":
    main()
