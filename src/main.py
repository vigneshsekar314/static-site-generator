from os import getcwd, listdir, pardir, mkdir 
from os.path import abspath, join, exists, isfile, isdir
from shutil import rmtree, copy
from generatepage import generate_page, generate_pages_recursive

def copy_static_to_public():
    cwd = getcwd()
    basedir = abspath(cwd)
    static_filepath = join(basedir, "static")
    public_filepath = join(basedir, "public")
    if not exists(static_filepath):
        basedir = abspath(join(cwd, pardir))
        static_filepath = join(basedir, "static")
        public_filepath = join(basedir, "public")
        if not exists(static_filepath):
            raise Exception("static filepath does not exists.")
    if exists(public_filepath):
        rmtree(public_filepath)
    mkdir(public_filepath)
    __copy_dir(src_dirpath=static_filepath, dst_dirpath=public_filepath)
    # source_file = join(basedir, "content/index.md")
    template_file = join(basedir, "template.html")
    # destination_file = join(public_filepath, "index.html")
    # generate_page(from_path=source_file, template_path=template_file, dest_path=destination_file)
    source_folder = join(basedir, "content")
    generate_pages_recursive(dir_path_content=source_folder, template_path=template_file, dest_dir_path=public_filepath)


def __copy_dir(src_dirpath: str, dst_dirpath) -> None:
    for file_folder in listdir(path=src_dirpath):
        content_fullpath = join(src_dirpath, file_folder)
        if isfile(content_fullpath):
            if not exists(dst_dirpath):
                mkdir(dst_dirpath)
            copy(src = content_fullpath, dst = dst_dirpath)
        elif isdir(content_fullpath):
            dest_dir = join(dst_dirpath, file_folder)
            __copy_dir(content_fullpath, dest_dir)
    

if __name__ == "__main__":
    copy_static_to_public()
