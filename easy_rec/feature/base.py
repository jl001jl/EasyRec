from collections import OrderedDict
from typing import Any
from json import dumps


class FeatureSpec(object):
    __legal__keys = ["name", "idx", "source"]
    __must_implement_keys = ["name", "idx"]

    def __init__(self):
        self.container = OrderedDict()

    def __setitem__(self, key, value):
        self.__check_key_is_legal(key)
        self.container[key] = value

    def __getitem__(self, key):
        self.__check_key_is_legal(key)
        return self.container[key]

    def exist(self, key: str) -> bool:
        self.__check_key_is_legal(key)
        return key in self.container

    def get(self, key: str) -> Any:
        return self.__getitem__(key)

    def set(self, key: str, val: Any) -> None:
        self.__setitem__(key, val)

    def __str__(self):
        return dumps(self.container, indent=4)

    def is_completed(self)->bool:
        return self.__check_is_completed()

    def __check_is_completed(self):
        for key in self.__must_implement_keys:
            if key not in self.container:
                return False
        return True

    def __check_key_is_legal(self, key:str)->None:
        if key not in self.__legal__keys:
            raise NotImplementedError(f"key: {key} not supported!")


if __name__ == '__main__':
    fs = FeatureSpec()
    fs["name"] = {'sdf':1, "fd":2}
    fs.set("idx", 0)
    print(fs.is_completed())
    print(fs)
