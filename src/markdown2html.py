from htmlnode import HTMLNode 
from leafnode import LeafNode
from parentnode import ParentNode
from nodechain import text_to_textnodes 
from textnode import text_node_to_html_node 
from blocks import markdown_to_blocks, block_to_block

def markdown2HTML(markdown: str) -> str:
    html_str = ""
    #  TODO: logic for markdown to HTML
    nodes: list[HTMLNode] = []
    blocks = markdown_to_blocks(markdown=markdown)
    for block in blocks:
        block_type = block_to_block(block)
        html_nds = block2HTMLNode(block, block_type)
        nodes.extend(html_nds)
    for nod in nodes:
        html_str += nod.to_html()
    return html_str

def block2HTMLNode(block: str, block_type: str):
    html_nodes = []
    match(block_type) :
        case "heading":
            hcount = wordcount(block, "#")
            tag = "h" + str(hcount)
            #  remove # from the block
            block_tmp = block[(hcount+1):]
            text_nd = LeafNode(tag,block_tmp)
            html_nodes.append(text_nd)
        case "code":
            nodes = text_to_textnodes(block)
            for nd in nodes:
                htmlnd = text_node_to_html_node(nd)
                html_nodes.append(htmlnd)
        case "quote":
            block_tmp = ""
            for i in block.split("\n"):
                block_tmp += i[2:]
            text_nd = LeafNode("blockquote",block_tmp)
            html_nodes.append(text_nd)
        case "unordered_list":
            lnodes: list[LeafNode] = []
            for lis in block.split("\n"):
                lnodes.append(LeafNode("li", lis[2:]))
            pnd = ParentNode("ul",children= lnodes)
            html_nodes.append(pnd)
        case "ordered_list":
            lnodes = []
            for lis in block.split("\n"):
                lnodes.append(LeafNode("li", lis[2:]))
            pnd = ParentNode("ol",children= lnodes)
            html_nodes.append(pnd)
        case "paragraph":
            # nodes = text_to_textnodes(block)
            lnode = LeafNode("p", block)
            html_nodes.append(lnode)
            # for nd in nodes:
            #     htmlnd = text_node_to_html_node(nd)
            #     html_nodes.append(htmlnd)
        case _:
            pass
    return html_nodes


def wordcount(fulltext: str, word: str) -> int: 
    wrdcount = 0
    for i in range(fulltext.__len__()):
        if fulltext[i] == word[0]:
            is_match = True 
            itemp = i
            for j in range(word.__len__()):
                if fulltext[itemp] != word[j]:
                    is_match = False
                    break
                itemp+=1
            if is_match:
                i = itemp
                wrdcount += 1
    return wrdcount

def main():
    markdown_text = "## Adventures of void.\n\nWhat is void?\n\n- void is nothing\n- void is empty\n- void surrounds all\n\nWe can find interesting reactions between the void and the voidless."
    print(markdown2HTML(markdown_text))


if __name__ == "__main__":
    main()