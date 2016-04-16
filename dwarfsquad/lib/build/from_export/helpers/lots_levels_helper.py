import os
from dwarfsquad.lib.utils import to_stderr
from csv_helper import read_csv


def get_lots_levels_csv(export_dir):

    lots_levels_csv = os.path.join(export_dir, 'lots_levels.csv')
    try:
        assert os.path.exists(lots_levels_csv)
    except AssertionError:
        to_stderr("Could not find lots_levels.csv. Skipping.")
        return []

    return read_csv(lots_levels_csv)