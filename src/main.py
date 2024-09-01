from os import getcwd, listdir, pardir, mkdir 
from os.path import abspath, join, exists, isfile, isdir
from shutil import rmtree, copy

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
