import os


def make_dir(path:str):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
