import json
import os
from dwarfsquad.lib.utils import to_stderr
from .helpers import build_full_ac_from_json


def build_assay_configuration(path_to_json):

    abs_json_path = os.path.abspath(path_to_json)
    assert os.path.isfile(abs_json_path)

    to_stderr("Building ac from json file.")
    with open(abs_json_path, 'r') as f:
        ac_json = json.load(f)
        ac = build_full_ac_from_json(ac_json)
    return ac
