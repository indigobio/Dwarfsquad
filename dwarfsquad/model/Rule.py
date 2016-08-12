from dwarfsquad.model.BaseWebModel import BaseWebModel


class Rule(BaseWebModel):
    required_fields = {
        'id': '',
        'name': '',
        'description': '',
        'schema': {},
        'compound_methods': []
    }

    @classmethod
    def __str__(cls):
        return "rule"

    def __init__(self, *args):
        base = {}
        for arg in reversed(args):
            assert isinstance(arg, dict)
            base = {**base, **arg}

        BaseWebModel.__init__(self, self.build_entities_with_id(base))
