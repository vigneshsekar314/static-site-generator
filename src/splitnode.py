from textnode import TextNode
from md import extract_markdown_links
from constants import text_type_image, text_type_link, text_type_text
import re


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    result = []
    for textNd in old_nodes:
        text = textNd.text
        split_tmp = text
        markdowns = extract_markdown_links(text)
        for mk in markdowns:
            sections = split_tmp.split(f"![{mk[0]}]({mk[1]})", 1)
            if sections[0] != "":
                result.append(TextNode(sections[0], text_type = "text"))
            result.append(TextNode(mk[0], text_type=text_type_image, url=mk[1]))
            split_tmp = sections[1] if len(sections) > 1 else ""
        if split_tmp is not None and split_tmp != "":
            result.append(TextNode(split_tmp, text_type_text))
    return result


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    result = []
    for textNd in old_nodes:
        text = textNd.text
        split_tmp = text
        markdowns = extract_markdown_links(text)
        for mk in markdowns:
            sections = split_tmp.split(f"[{mk[0]}]({mk[1]})", 1)
            if sections[0] != "":
                result.append(TextNode(sections[0], text_type = "text"))
            result.append(TextNode(mk[0], text_type=text_type_link, url=mk[1]))
            split_tmp = sections[1]
        if split_tmp is not None and split_tmp != "":
            result.append(TextNode(split_tmp, text_type_text))
    return result
    


def main():
    originaltxt = "this is an ![image](https://example.com) being embedded here bro. Also make sure to use some ![image](nothing) here."
    tn = TextNode(text=originaltxt,text_type="text")
    print(f"original text is: {originaltxt}")
    print(split_nodes_image([tn]))

if __name__ == "__main__":
    main()
