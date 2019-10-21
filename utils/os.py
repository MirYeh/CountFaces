""" OS utilities """
import os


def save(local_path, data):
    last_dir_index = local_path.rfind(os.sep)
    dirs = local_path[:last_dir_index]
    if not os.path.exists(dirs):
        os.mkdir(dirs)

    with open(local_path, 'wb') as f:
        f.write(data)
