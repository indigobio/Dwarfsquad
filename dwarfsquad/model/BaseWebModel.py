import json
from copy import deepcopy
import bson


class BaseWebModel(dict, object):
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    required_fields = {'None': None}

    def __init__(self, item):
        if not isinstance(item, dict):
            item = {}
        super(BaseWebModel, self).__init__(item)

        # id gets precedence here because the response from web uses 'id'
        if item.get('id') and bson.ObjectId.is_valid(str(item.get('id'))):
            self._id = str(self.id)
        elif item.get('_id') and bson.ObjectId.is_valid(str(item.get('_id'))):
            self._id = str(self._id)
        elif item.get('_id') and isinstance(item.get('_id'), dict):
            self._id = str(item.get('_id').get("$oid"))
        else:
            self._id = str(bson.ObjectId())

        self.id = self._id

    def __getattribute__(self, attr):
        try:
            return super(BaseWebModel, self).__getitem__(attr)
        except KeyError:
            return super(BaseWebModel, self).__getattribute__(attr)

    def __getattr__(self, attr):
        if attr in self:
            return self[attr]
        raise AttributeError(attr)

    @classmethod
    def load(cls, item):
        return cls(item)

    @classmethod
    def className(cls):
        return cls.__name__

    def build_entities_with_id(self, dictionary):
        return dict(self.get_missing_items(dictionary).items() + dictionary.items())

    def build_required_entities_only(self, dictionary):
        return dict(self.get_missing_items(dictionary).items() + self.get_required_items(dictionary).items())

    def get_required_items(self, dictionary=None):
        if not dictionary:
            dictionary = self

        return_dict = {}
        for key, val in dictionary.iteritems():
            if isinstance(val, list) and key in self.required_fields.keys():
                return_dict[key] = [v.get_required_items() if isinstance(v, BaseWebModel) else v for v in val]
            elif isinstance(val, BaseWebModel) and key in self.required_fields.keys():
                return_dict[key] = val.get_required_items()
            elif key in self.required_fields.keys():
                return_dict[key] = val
        return return_dict

    def get_missing_items(self, dictionary=None):
        if not dictionary:
            dictionary = self
        return dict((key, value) for key, value in deepcopy(self.required_fields).iteritems() if key not in dictionary)

    def dump(self):
        return json.dumps(dict(self.get_required_items().items() + self.get_missing_items().items()))

    def enumerate_arrays(self, model, items):
        try:
            return [model(item) for item in items if isinstance(item, dict)]
        except (ValueError, TypeError):
            return []