import re


def extract_markdown_links(text:str) -> list[tuple]:
    result = []
    embed_matches = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    if matches is not None and len(matches) != 0:
        result.extend(matches)
    if embed_matches is not None and len(embed_matches) != 0:
        for m in embed_matches:
            if m not in result:
                result.extend(embed_matches)
    return result

def main():
    txt = "This is a markdown ![marklink](https://example.com) and another link ![md](https://another.com) and fin and another link [kontemplate](https://kontemplate.io)"
    print(extract_markdown_links(txt))

if __name__ == "__main__":
    main()


