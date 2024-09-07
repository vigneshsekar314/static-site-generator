from textnode import TextNode
from md import extract_markdown_links
from constants import text_type_image, text_type_link, text_type_text
import re


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    result = []
    for textNd in old_nodes:
        text = textNd.text
        node_text_type = textNd.text_type
        node_type_url = textNd.url
        split_tmp = text
        markdowns = extract_markdown_links(text)
        for mk in markdowns:
            sections = split_tmp.split(f"![{mk[0]}]({mk[1]})", 1)
            # if sections[0] != "":
            if sections[0] != "" and sections[0] == split_tmp:
                continue
                # node_toadd = TextNode(sections[0], text_type = node_text_type)
                # if node_toadd not in result:
                    # result.append(node_toadd)
            else:
                node_toadd = TextNode(sections[0], text_type = node_text_type)
                if node_toadd not in result:
                    result.append(node_toadd)
                result.append(TextNode(mk[0], text_type=text_type_image, url=mk[1]))
            if len(sections) > 1:
                split_tmp = sections[1]
        if split_tmp is not None and split_tmp != "":
            result.append(TextNode(text=split_tmp, text_type=node_text_type, url=node_type_url))
    return result


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    result = []
    for textNd in old_nodes:
        text = textNd.text
        node_text_type = textNd.text_type
        node_url = textNd.url
        split_tmp = text
        markdowns = extract_markdown_links(text)
        for mk in markdowns:
            sections = split_tmp.split(f"[{mk[0]}]({mk[1]})", 1)
            if (sections[0] != "" and sections[0] == split_tmp) or sections[0].endswith("!"):  #  to prevent images being recognized as links
                continue
            else:
                node_toadd = TextNode(sections[0], text_type = node_text_type)
                if node_toadd not in result:
                    result.append(node_toadd)
                result.append(TextNode(mk[0], text_type=text_type_link, url=mk[1]))
            split_tmp = sections[1]
        if split_tmp is not None and split_tmp != "":
            result.append(TextNode(text=split_tmp, text_type=node_text_type, url=node_url))
    return result
    


def main():
    originaltxt = "this is an [not an image](https://example.com) being embedded here bro. Also make sure to use some ![image](/images/rivendell.png) here."
    tn = TextNode(text=originaltxt,text_type="text")
    print(f"original text is: {originaltxt}")
    print(split_nodes_image([tn]))
    # print(split_nodes_link([tn]))

if __name__ == "__main__":
    main()
