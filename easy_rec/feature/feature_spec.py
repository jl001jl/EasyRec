from collections import OrderedDict
from json import dumps
from typing import Any, List, Dict


class FeatureSpec(object):
    __support_key__: List[str]
    __must_implement_key__: List[str]
    __spec_value__: Dict[str, Any]
    __spec_type__: Dict[str, Any]

    def __init__(self):
        self._container = OrderedDict()

    def __setitem__(self, key, value):
        self.__check_key_value_is_legal(key, value)
        self._container[key] = value

    def __getitem__(self, key):
        self.__check_key_is_legal(key)
        return self._container[key]

    def exist(self, key: str) -> bool:
        self.__check_key_is_legal(key)
        return key in self._container

    def get(self, key: str) -> Any:
        return self.__getitem__(key)

    def set(self, key: str, val: Any) -> None:
        self.__setitem__(key, val)

    def __str__(self):
        return dumps(self._container, indent=4)

    def is_completed(self) -> bool:
        return self.__check_is_completed()

    def __check_is_completed(self):
        for key in self.__must_implement_key__:
            if key not in self._container:
                return False
        return True

    def __check_key_is_legal(self, key: str) -> None:
        if key not in self.__must_implement_key__:
            raise KeyError(f"key {key} not supported!")

    def __check_key_value_is_legal(self, key: str, value: Any) -> None:
        self.__check_key_is_legal(key)
        if key in self.__spec_type__ and not isinstance(value, self.__spec_type__.get(key)):
            raise TypeError(f"value of key {key} not supported! it should be type: {self.__spec_type__.get(key)}!")
        if key in self.__spec_value__ and value != self.__spec_value__[key]:
            raise ValueError(f"value of key {key} not supported! it should be value: {self.__spec_value__.get(key)}!")

    @property
    def descriptor(self) -> OrderedDict:
        return self._container


class NumericFeatureSpec(FeatureSpec):
    __support_key__ = ["name", "source", "type", "index", "blood"]
    __must_implement_key__ = ["name", "type", "index"]
    __spec_type__ = {
        "name": str,
        "source": str,
        "type": str,
        "index": int,
        "blood": OrderedDict,
    }
    __spec_value__ = {
        "type": "numeric"
    }


class CategoryFeatureSpec(FeatureSpec):
    __support_key__ = ["name", "source", "type", "index", "blood", "vocab_size", "padding_idx", "share_with"]
    __must_implement_key__ = ["name", "type", "index", "vocab_size"]
    __spec_type__ = {
        "name": str,
        "source": str,
        "type": str,
        "index": int,
        "blood": OrderedDict,
        "vocab_size": int,
        "padding_idx": int,
        "share_embedding": str
    }
    __spec_value__ = {
        "type": "category"
    }


class SequenceFeatureSpec(FeatureSpec):
    __support_key__ = ["name", "source", "type", "index", "blood", "vocab_size", "padding_idx", "share_embedding",
                       "encoder", "max_len"]
    __must_implement_key__ = ["name", "type", "index", "vocab_size", "max_len", "padding_idx"]
    __spec_type__ = {
        "name": str,
        "source": str,
        "type": str,
        "index": list,
        "blood": OrderedDict,
        "vocab_size": int,
        "padding_idx": int,
        "share_embedding": str,
        "encoder": str,
        "max_len": int,
    }
    __spec_value__ = {
        "type": "sequence"
    }
