from __future__ import print_function
import sys
import os
import json
from bson import ObjectId
import zipfile
from openpyxl import load_workbook
from dwarfsquad.model import AssayConfiguration


def to_stderr(line):
    print(line, end='\n', file=sys.stderr)


def to_stdout(line):
    print(line, end='\n', file=sys.stdout)


def is_json_assay(data):

    if not isinstance(data, basestring) and not os.path.isfile(os.path.abspath(data)):
        return False

    try:
        with open(os.path.abspath(str(data)), 'r') as f:
            x = json.load(f)
            assert set(AssayConfiguration.required_fields.keys()).issubset(set(x.keys()))
            return True
    except Exception:
        return False


def is_xlsx_file(data):
    try:
        load_workbook(os.path.abspath(data))
        return True
    except Exception as e:
        return False


def is_valid_oid(data):

    if ObjectId.is_valid(data) and str(ObjectId(data)) == str(data):
        return True
    else:
        return False


def is_exported_assay(data):
    return isinstance(data, basestring) and \
           os.path.exists(data) and \
           os.path.exists(os.path.join(data, 'compounds.csv'))


def is_batch(data):
    if os.path.exists(data) and zipfile.is_zipfile(data):
        return file(data)


def map_chromatogram_methods(id_map, id_list):
    return_list = []
    for ch_id in id_list:
        try:
            return_list.append(id_map[ch_id])
        except KeyError:
            to_stderr("\nWarning: Chromatogram with id: " + str(ch_id) + " doesn't exist. Skipping.")

    return return_list


def assert_assay_configuration(ac):
    try:
        assert isinstance(ac, AssayConfiguration)
    except:
        raise AssertionError("ac is type: " + str(type(ac)))