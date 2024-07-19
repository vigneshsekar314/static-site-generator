from leafnode import LeafNode

def text_node_to_html_node(text_node):
    text_type = ["text", "bold", "italic", "code", "link", "image"]
    if text_node not in text_type:
        raise ValueError("text type is not valid")
    switch text_node:
        case "text":


