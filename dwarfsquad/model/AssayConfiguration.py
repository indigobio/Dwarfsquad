from BaseWebModel import BaseWebModel
from CompoundMethod import CompoundMethod
from Lot import Lot
from bson import ObjectId
from QaRuleSchema import QaRuleSchema
from DisplaySettings import DisplaySettings


class AssayConfiguration(BaseWebModel):
    required_fields = {
        'name': "",
        'compute_version': "",
        'compound_methods': [],
        'lots': [],
        'macros': [],
        'one_step_review': False,
        'properties': {},
        'instruments': [],
        'qa_rule_schemas': [],
        'display_settings': DisplaySettings({})
    }

    @classmethod
    def __str__(cls):
        return "assay configuration"

    def __eq__(self, other):
        if isinstance(other, basestring):
            return self.name == other
        if isinstance(other, type(self)):
            return self.name == other.name
        if isinstance(other, ObjectId):
            return str(other) == self.id

    def __init__(self, *args):
        base = {}
        for arg in reversed(args):
            assert isinstance(arg, dict)
            base = dict(base.items() + arg.items())

        BaseWebModel.__init__(self, self.build_entities_with_id(base))

        self.set_display_settings(DisplaySettings(self.display_settings))
        self.qa_rule_schemas = self.enumerate_arrays(QaRuleSchema, self.qa_rule_schemas)
        self.compound_methods = self.enumerate_arrays(CompoundMethod, self.compound_methods)
        self.lots = self.enumerate_arrays(Lot, self.lots)

        if not 'id_map' in self.keys():
            self.id_map = {}

    def set_name(self, name):
        assert isinstance(name, basestring)
        self.name = name

    def set_compute_version(self, compute_version):
        self.compute_version = compute_version

    def set_properties(self, properties):
        assert isinstance(properties, dict)
        self.properties = properties

    def set_macros(self, macros):
        assert isinstance(macros, list)
        self.macros = macros

    def set_one_step_review(self, one_step_review):
        assert isinstance(one_step_review, bool)
        self.one_step_review = one_step_review

    def set_instruments(self, instruments):
        assert isinstance(instruments, list)
        self.instruments = instruments

    def set_display_settings(self, display_settings):
        assert isinstance(display_settings, DisplaySettings)
        self.display_settings = display_settings