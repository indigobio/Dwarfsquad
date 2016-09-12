import datetime

from dwarfsquad.lib.compat import join_dicts
from dwarfsquad.model.BaseWebModel import BaseWebModel
from dwarfsquad.model.Level import Level
from dwarfsquad.model.LotCompound import LotCompound


class Lot(BaseWebModel):
    required_fields = {
        'name': '',
        'id': '',
        'levels': [],
        "created_at": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.000Z'),
        "updated_at": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.000Z'),
        'sample_type': 'STANDARD',
        'compounds': []
    }

    @classmethod
    def __str__(cls):
        return "lot"

    def __init__(self, *args):
        base = {}
        for arg in reversed(args):
            assert isinstance(arg, dict)
            base = join_dicts(arg, base)
        BaseWebModel.__init__(self, self.build_entities_with_id(base))

        self.levels = self.enumerate_arrays(Level, self.levels)
        self.compounds = self.enumerate_arrays(LotCompound, self.compounds)

    def set_name(self, name):
        assert isinstance(name, str)
        self.name = name

    def set_sample_type(self, sample_type):
        assert isinstance(sample_type, str)
        self.sample_type = sample_type

    def set_compounds(self, compounds):
        assert isinstance(compounds, list)
        self.compounds = compounds
