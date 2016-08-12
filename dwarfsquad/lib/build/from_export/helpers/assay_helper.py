import os
from dwarfsquad.lib.utils import to_stderr
from .csv_helper import read_csv


def get_assay_csv(export_dir):

    assay_csv = os.path.join(export_dir, 'assay.csv')
    try:
        assert os.path.exists(assay_csv)
    except AssertionError:
        to_stderr("Could not find assay.csv. Skipping.")
        return []

    return read_csv(assay_csv)


def get_assay_name(path_to_assay):
    to_stderr(path_to_assay)
    assay_name = os.path.split(path_to_assay)[1]
    to_stderr("Found assay named " + assay_name)
    assert assay_name
    return assay_name
