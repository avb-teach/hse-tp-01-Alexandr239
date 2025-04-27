import os
import shutil
import sys

in_dir = sys.argv[1]
out_dir = sys.argv[2]
# in_dir = '/tmp/in_dir'
# out_dir = '/tmp/out_dir'

# print(f"{in_dir=}, {out_dir=}")


def get_dir_files(d, depth):
    # print(f"{d=}, {depth=}")
    d_list = os.listdir(d)
    for f in d_list:
        f_name = os.path.join(d, f)
        # print(f"{f=}, {f_name=}")
        if os.path.islink(f_name):
            continue
        elif os.path.isdir(f_name):
            get_dir_files(f_name, depth + 1)
        elif os.path.isfile(f_name):
            shutil.copy(f_name, out_dir)


get_dir_files(in_dir, 1)
