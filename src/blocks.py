
def markdown_to_blocks(markdown: str) -> list[str]:
    result = []
    for block in markdown.split("\n\n"):
        res = del_empty_lines(block)
        if res != "\n" and res != "":
            result.append(res)
    return result

def del_empty_lines(block):
    tmp_res = block
    tmp_res = tmp_res.lstrip(" ").rstrip(" ")
    while tmp_res.startswith("\n"):
        tmp_res = tmp_res[1:]
    while tmp_res.endswith("\n"):
        tmp_res = tmp_res[:-1]
    tmp_res = tmp_res.lstrip(" ").rstrip(" ")
    return tmp_res


def block_to_block(block: str) -> str:
    result = ""
    starting_sequence = starting_seq(block)
    match starting_sequence:
        case "# ":
            if multiline_blockcheck(block, "heading"):
                result = "heading"
            else:
                result = "paragraph"
        case "## ":
            if multiline_blockcheck(block, "heading"):
                result = "heading"
            else:
                result = "paragraph"
        case "### ":
            if multiline_blockcheck(block, "heading"):
                result = "heading"
            else:
                result = "paragraph"
        case "#### ":
            if multiline_blockcheck(block, "heading"):
                result = "heading"
            else:
                result = "paragraph"
        case "##### ":
            if multiline_blockcheck(block, "heading"):
                result = "heading"
            else:
                result = "paragraph"
        case "###### ":
            if multiline_blockcheck(block, "heading"):
                result = "heading"
            else:
                result = "paragraph"
        case "```":
            # ending = ending_seq(block)
            # if ending == "```":
            if block.endswith("```"):
                result = "code"
            else:
                result = "paragraph" 
        case "> ":
            if multiline_blockcheck(block, "quote"):
                result = "quote"
            else:
                result = "paragraph"
        case "* ":
            if multiline_blockcheck(block, "bullet_star"):
                result = "unordered_list"
            else:
                result = "paragraph"
        case "- ":
            if multiline_blockcheck(block, "bullet_dash"):
                result = "unordered_list"
            else:
                result = "paragraph"
        case starting_sequence if block[0].isdigit():
            if multiline_blockcheck(block, "numbered"):
                result = "ordered_list"            
            else:
                result = "paragraph"
        case _:
            result = "paragraph"

    return result

def multiline_blockcheck(block: str, check: str) -> bool:
    if check == "quote":
        for ln in block.split("\n"):
            if not ln.startswith("> "):
                return False
        return True   
    elif check == "bullet_star":
        for ln in block.split("\n"):
            if not ln.startswith("* "):
                return False
        return True
    elif check == "bullet_dash":
        for ln in block.split("\n"):
            if not ln.startswith("- "):
                return False
        return True
    elif check == "numbered":
        for ln in block.split("\n"):
            if not (ln[0].isdigit() and ln[1] == "." and ln[2] == " "):
                return False
        return True
    elif check == "heading":
        heading_start = ["# ", "## ", "### ", "#### ", "##### ", "###### "]
        for ln in block.split("\n"):
            is_heading = False
            for st in heading_start:
                if ln.startswith(st):
                    is_heading = True
                    break 
            if not is_heading:
                return False
        return True

    else:
        return False

        
        

def starting_seq(block: str) -> str:
    result = ""
    cpy = block
    if cpy.startswith("#"):
        while cpy.startswith("#"):
            result += "#"
            cpy = cpy[1:]
        return result + cpy[0] 
    elif cpy.startswith("`"):
        while cpy.startswith("`"):
            result+= "`"
            cpy = cpy[1:]
        return result
    else:
        return cpy[0:2] 

def ending_seq(block: str) -> str:
    result = ""
    cpy = block
    if cpy.endswith("`"):
        while cpy.endswith("`"):
            result += "`"
            cpy = cpy[1:]
        return result



def main():
    paragraph = ""
    # with open("./check/paragraph.txt", "r") as f:
        # paragraph = f.read()
    paragraph = """
This is a line.

# this is a heading 1

## this is a heading 2


This should represent another paragraph. Let us see how it does."""
    # print(paragraph)
    # print(markdown_to_blocks(paragraph))
    blocks = markdown_to_blocks(paragraph)
    block = "```let infinite = recursion_without_exit_condition()\nlet finite = recursion()```"
    block_type = block_to_block(block)
    for i in blocks:
        print(f"block: {i}")
        print(f"type: {block_to_block(i)}")


if __name__ == "__main__":
    main()
    