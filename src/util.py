from leafnode import LeafNode
from htmlnode import HTMLNode
from parentnode import ParentNode
from textnode import TextNode

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: str) -> list[TextNode]:
    handlNon(old_nodes)
    text_type_text, text_type_bold, text_type_italic,text_type_code,text_type_link,text_type_image = "text", "bold", "italic", "code", "link", "image"
    valid_txt_types = [text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image]
    if text_type not in valid_txt_types:
        raise ValueError("argument 'text type' is not a valid text type")
    node_delimited = []
    for node in old_nodes:
        if type(node) != TextNode:
            node_delimited.append(node)
        else:
            # is_delimiter_start = False
            # startswith_delim = node.text.startswith(delimiter)
            # endswith_delim = node.text.endswith(delimiter)
            node_text = node.text
            if delimiter == "*" and node.text.startswith("* "):
                node_text = node.text[2:]
            delimiter_count = countof(node_text, delimiter) # TODO: implement this functionality with a much simpler approach
            if delimiter_count % 2 != 0: 
                    raise Exception(f"delimiter {delimiter} is kept open")
            for (index, txt) in enumerate(node.text.split(delimiter)):
                if index % 2 == 0:
                    if len(txt) != 0:
                        #node_delimited.append(TextNode(txt, text_type_text))
                        node_delimited.append(TextNode(txt, node.text_type, node.url))
                else:
                    if len(txt) != 0:
                        if text_type == text_type_code and txt.startswith("\n"):
                            node_delimited.append(TextNode(txt[1:], text_type))
                        else:
                            node_delimited.append(TextNode(txt, text_type))

                
    return node_delimited

def gen_node(txtlst: list[str], type: str) -> list:
    handlNon(txtlst)
    return TextNode(" ".join(txtlst),type)


def handlNon(obj):
    if obj is None:
        return None

def countof(words: str, char_to_count: str) -> int:
    c = 0
    word_length = words.__len__()
    for (index, character) in enumerate(words):
        if index == 0 or index == word_length -1: 
            if character == char_to_count: # TODO: need to think for more cases before fully implementing this 
                c += 1
        elif character == char_to_count:
            pre_space = words[index-1] == " "
            post_space = words[index+1] == " "
            line_start = words[index-1] == "\n"
            if not (pre_space and post_space) and not (line_start and char_to_count == "*" and post_space):
                c += 1
    return c


def main():
    n = TextNode("This is text with a `code block` word", "text")
    print(split_nodes_delimiter([n], "`", "code"))

if __name__ == "__main__":
    main()
