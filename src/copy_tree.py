import os
import shutil


def copy_tree(src_dir, dst_dir):
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    os.mkdir(dst_dir)

    for file in os.listdir(src_dir):
        src_path = os.path.join(src_dir, file)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_dir)
        elif os.path.isdir(src_path):
            copy_tree(src_path, os.path.join(dst_dir, file))
