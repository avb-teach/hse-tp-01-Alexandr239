import os
import shutil
import sys

in_dir = sys.argv[1]
out_dir = sys.argv[2]
max_depth = 1
if len(sys.argv) == 4 and sys.argv[3]:
    max_depth = int(sys.argv[3])

if not in_dir.endswith("/"):
    in_dir += "/"
if not out_dir.endswith("/"):
    out_dir += "/"

files = {}


def get_dir_files(d, depth):
    d_list = os.listdir(d)
    for f in d_list:
        f_name = os.path.join(d, f)
        if os.path.islink(f_name):
            continue
        elif os.path.isdir(f_name):
            get_dir_files(f_name, depth + 1)
        elif os.path.isfile(f_name):
            tmp = f
            path_arr = f_name.replace(in_dir, "", 1).split("/")
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
            path_arr.pop()
            if len(path_arr) >= max_depth - 1:
                path_arr = path_arr[len(path_arr) - (max_depth - 1):len(path_arr)]
            out_dir_tmp = os.path.join(out_dir, "/".join(path_arr))
            os.makedirs(out_dir_tmp, exist_ok=True)
            shutil.copy(f_name, os.path.join(out_dir_tmp, tmp))


get_dir_files(in_dir, 1)
