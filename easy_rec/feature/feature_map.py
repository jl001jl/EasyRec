from collections import OrderedDict
from easy_rec.utils import make_dir
import json





class FeatureMap(object):
    def __init__(self, save_dir:str=".\\"):
        self.save_file = save_dir + "feature_map.json"
        self.num_fields = 0
        self.num_features = 0
        self.input_length = 0
        self.feature_specs = OrderedDict()

    def save(self, save_file=None)->None:
        if save_file is None:
            save_file = self.save_file
        make_dir(save_file)
        with open(save_file, 'w') as fp:
            json.dump(self.descriptor, fp, indent=4)

    @staticmethod
    def load(json_file):
        with open(json_file, 'w') as fp:
            ordered_dict = json.load(fp)
            feature_map = FeatureMap()
            for x in ["num_fields", "num_features","input_length"]:
                feature_map.__setattr__(x, ordered_dict[x])
            feature_map.__setattr__("feature_specs", OrderedDict(ordered_dict["feature_specs"]))

    @property
    def descriptor(self)->OrderedDict:
        ordered_dict = OrderedDict()
        for x in ["num_fields", "num_features", "input_length", "feature_specs"]:
            ordered_dict[x] = self.__getattribute__(x)
        return ordered_dict


if __name__ == '__main__':
    fm = FeatureMap()
    fm.save(".\\ss.json")

