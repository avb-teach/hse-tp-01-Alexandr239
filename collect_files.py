import os
import shutil
import sys

in_dir = sys.argv[1]
out_dir = sys.argv[2]
max_depth = None
if len(sys.argv) == 4 and sys.argv[3]:
    max_depth = int(sys.argv[3])
# in_dir = '/tmp/in_dir'
# out_dir = '/tmp/out_dir'

# print(f"{in_dir=}, {out_dir=}, {max_depth=}")
files = {}


def get_dir_files(d):
    # print(f"{d=}, {depth=}")
    d_list = os.listdir(d)
    for f in d_list:
        f_name = os.path.join(d, f)
        # print(f"{f=}, {f_name=}")
        if os.path.islink(f_name):
            continue
        elif os.path.isdir(f_name):
            get_dir_files(f_name)
        elif os.path.isfile(f_name):
            tmp = f
            if files.get(f) is not None:
                files[f] += 1
                name_ext = f.split(".")
                if len(name_ext) == 1:
                    name_ext[0] = f"{name_ext[0]}{str(files.get(f))}"
                elif len(name_ext) > 1:
                    name_ext[-2] = f"{name_ext[-2]}{str(files.get(f))}"
                tmp = ".".join(name_ext)
            else:
                files[f] = 0
            shutil.copy(f_name, os.path.join(out_dir, tmp))


get_dir_files(in_dir)
