import os
import shutil


def delete_folder_content(folder_path):
    """ Deletes folder content by removing the path and recreating it """
    if os.path.isdir(folder_path):
        shutil.rmtree(folder_path)
        os.mkdir(folder_path)
