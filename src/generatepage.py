from markdown2html import markdown_to_html_node
from os.path import isfile, exists, dirname, isdir, join
from os import makedirs, pardir, listdir, mkdir 
from shutil import copy


def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_content = ""
    template_content = ""
    with open(from_path, "r") as f:
        markdown_content = f.read()
    with open(template_path, "r") as t:
        template_content = t.read()
    
    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_content)

    dir_name_dest = dirname(dest_path)
    if not exists(dir_name_dest):
        makedirs(dir_name_dest)

    with open(dest_path, "w") as write_context:
        write_context.write(template_content)

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
    __gen_html(dir_path_content, template_path=template_path, dst_dirpath=dest_dir_path)

def __gen_html(src_dirpath: str, template_path: str, dst_dirpath) -> None:
    for file_folder in listdir(path=src_dirpath):
        content_fullpath = join(src_dirpath, file_folder)
        if isfile(content_fullpath):
            if not exists(dst_dirpath):
                mkdir(dst_dirpath)
            if content_fullpath.endswith(".md"): 
                destination_fullpath = join(dst_dirpath, file_folder.replace(".md",".html"))
                generate_page(from_path= content_fullpath, template_path=template_path, dest_path=destination_fullpath)
        elif isdir(content_fullpath):
            dest_dir = join(dst_dirpath, file_folder)
            __gen_html(src_dirpath=content_fullpath, template_path=template_path, dst_dirpath=dest_dir)

def extract_title(markdown: str) -> str:
    firstline = markdown.strip()
    heading = __get_heading(firstline)
    if heading is not None:
        return heading
    else:
        raise Exception("There is no heading for this file")

def __get_heading(markdown: str) -> str:
    if markdown.startswith("# "):
        return markdown.lstrip("# ").split("\n",maxsplit=1)[0]
    elif markdown.startswith("## "):
        return markdown.lstrip("## ").split("\n",maxsplit=1)[0]
    elif markdown.startswith("### "):
        return markdown.lstrip("### ").split("\n",maxsplit=1)[0]
    elif markdown.startswith("#### "):
        return markdown.lstrip("#### ").split("\n",maxsplit=1)[0]
    elif markdown.startswith("##### "):
        return markdown.lstrip("##### ").split("\n",maxsplit=1)[0]
    elif markdown.startswith("###### "):
        return markdown.lstrip("###### ").split("\n",maxsplit=1)[0]
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

    generate_page(from_path="/home/vignesh/workspace/github.com/vigneshsekar314/staticSiteGen/content/index.md", 
                  template_path="/home/vignesh/workspace/github.com/vigneshsekar314/staticSiteGen/template.html",
                  dest_path="/home/vignesh/workspace/github.com/vigneshsekar314/staticSiteGen/public/index.html")


if __name__ == "__main__":
    main()