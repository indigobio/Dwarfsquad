import os
from dwarfsquad.lib.utils import to_stderr
from .csv_helper import read_csv


def get_compounds_csv(export_dir):

    compounds_csv = os.path.join(export_dir, 'compounds.csv')
    try:
        assert os.path.exists(compounds_csv)
    except AssertionError:
        to_stderr("Could not find compounds.csv. Skipping.")
        return []

    return read_csv(compounds_csv)