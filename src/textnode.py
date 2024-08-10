from leafnode import LeafNode

class TextNode:
    def __init__(self, text: str, text_type: str, url: str | None = None):
        self.text = text 
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return type(self).__name__ + "(\"" + self.text + "\", \"" + self.text_type + "\", \"" + (self.url if self.url is not None else "None") + "\")"


def main():
    txt = TextNode("this is a text node", "bold", "https://www.kontemplate.io")
    print(txt)
    print(text_node_to_html_node(txt))

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    text_type = ["text", "bold", "italic", "code", "link", "image"]
    if text_node.text_type not in text_type:
        raise ValueError("text type is not valid")
    match text_node.text_type:
        case "text":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "link":
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case "image":
            return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text}) 
        case _:
            return


if __name__ == "__main__":
    main()



        
