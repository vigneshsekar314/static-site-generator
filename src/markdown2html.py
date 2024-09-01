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
            hn = []
            tnode = text_to_textnodes(block_tmp)
            for tn in tnode:
                htmlnds = text_node_to_html_node(tn)
                hn.append(htmlnds)
            hnds = ParentNode(tag,children=hn)
            html_nodes.append(hnds)
        case "code":
            hn = []
            nodes = text_to_textnodes(block)
            for nd in nodes:
                htmlnd = text_node_to_html_node(nd)
                hn.append(htmlnd)
            rnode = ParentNode("pre", children=hn)
            html_nodes.append(rnode)
        case "quote":
            block_tmp = ""
            for i in block.split("\n"):
                block_tmp += "\n" + i[2:]
            tnode= text_to_textnodes(block_tmp)
            htmlnds = []
            for tn in tnode:
                htmlnds.append(text_node_to_html_node(tn))
            hnds = ParentNode("blockquote",children=htmlnds)
            html_nodes.append(hnds)
        case "unordered_list":
            lnodes: list[LeafNode] = []
            for lis in block.split("\n"):
                tn = text_to_textnodes("\n" + lis[2:])
                for t in tn:
                   hn = text_node_to_html_node(t)
                   pn = ParentNode("li", children=[hn])
                   lnodes.append(pn)
            pnd = ParentNode("ul",children= lnodes)
            html_nodes.append(pnd)
        case "ordered_list":
            lnodes = []
            for lis in block.split("\n"):
                lnodes.append(LeafNode("li", lis[2:]))
            pnd = ParentNode("ol",children= lnodes)
            html_nodes.append(pnd)
        case "paragraph":
            nodes = text_to_textnodes(block)
            for nd in nodes:
                pn = text_node_to_html_node(nd)
                html_nodes.append(pn)
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
    # markdown_text = "## Adventures of void.\n\nWhat is void?\n\n- void is nothing\n- void is empty\n- void surrounds all\n\nWe can find interesting reactions between the void and the voidless."
    markdown_text = ""
    with open('/home/vignesh/workspace/github.com/vigneshsekar314/staticSiteGen/src/check/markdown2.md') as e:
        markdown_text = e.read()
    print(markdown2HTML(markdown_text))


if __name__ == "__main__":
    main()