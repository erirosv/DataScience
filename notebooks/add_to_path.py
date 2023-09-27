import sys
import os

def add_parent_directory_to_path():
    parent_dir = os.path.dirname(os.getcwd())
    sys.path.append(parent_dir)

add_parent_directory_to_path()