
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

    


def main():
    paragraph = ""
    with open("./check/paragraph.txt", "r") as f:
        paragraph = f.read()
    print(paragraph)
    print(markdown_to_blocks(paragraph))


if __name__ == "__main__":
    main()
    