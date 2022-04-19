from collections import OrderedDict
from typing import Any


class FeatureSpec(object):
    __legal__keys=["name","idx"]

    def __init__(self):
        self.container = OrderedDict()

    def exist(self, key:str)->bool:
        return key in self.container

    def get(self, key:str)->Any:
        return self.container[key]

    def set(self, key:str, val:Any)->None:
        self.container[key] = val

