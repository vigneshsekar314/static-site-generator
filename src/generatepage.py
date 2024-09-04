

def extract_title(markdown: str) -> str:
    firstline = markdown.strip()
    heading = get_heading(firstline)
    if heading is not None:
        return heading
    else:
        raise Exception("There is no heading for this file")

def get_heading(markdown: str) -> str:
    if markdown.startswith("# "):
        return "h1"
    elif markdown.startswith("## "):
        return "h2"
    elif markdown.startswith("### "):
        return "h3"
    elif markdown.startswith("#### "):
        return "h4"
    elif markdown.startswith("##### "):
        return "h5"
    elif markdown.startswith("###### "):
        return "h6"
    else:
        return None

def main():
    para = """
  # In a world
In a world where infinite possibilities exists, there lived a man who lived by his own rules
His rules seemed to be a cage trapping him in the eyes of those who adventured the nicities of life.

Little did they know, that his rules can give him the freedom for infinite possibilities.


"""
    print(extract_title(para))


if __name__ == "__main__":
    main()