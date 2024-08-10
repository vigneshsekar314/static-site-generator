from textnode import TextNode
from splitnode import split_nodes_image, split_nodes_link
from md import extract_markdown_links
from util import split_nodes_delimiter
from constants import \
text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link,\
text_type_image

def text_to_textnodes(text: str) -> list[TextNode]:
    result = [TextNode(text, text_type_text)]
    result = split_nodes_delimiter(result ,"**", text_type_bold)
    result = split_nodes_delimiter(result, "*", text_type_italic)
    result = split_nodes_delimiter(result, "`", text_type_code)
    result = split_nodes_image(result)
    result = split_nodes_link(result) 
    return result

def main():
    content = ""
    # with open('./check/markdowns.txt', 'r') as fileOpen:
       # content = fileOpen.read()
    content= "This is supposed to be a markdown file with many elements like **bold**, *italic*, `codeing content`, [link](https://example.com) and an ![image](https://example.com)."
    print(f"original text: {content}")
    print(text_to_textnodes(content))

if __name__ == "__main__":
    main()

