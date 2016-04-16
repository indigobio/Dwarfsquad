from BaseWebModel import BaseWebModel


class QaRuleSchema(BaseWebModel):
    required_fields = {
        "name": "",
        "display_name": "",
        "description": "",
        "rule_parameters": []
    }

    @classmethod
    def __str__(cls):
        return "qa_rule_schemas"

    def __init__(self, *args):
        base = {}
        for arg in reversed(args):
            assert isinstance(arg, dict)
            base = dict(base.items() + arg.items())

        BaseWebModel.__init__(self, self.build_required_entities_only(base))
        self.set_rule_parameters(self.enumerate_arrays(RuleParameter, self.rule_parameters))

    def set_rule_parameters(self, rule_parameters):
        assert isinstance(rule_parameters, list)
        self.rule_parameters = rule_parameters


class RuleParameter(BaseWebModel):
    required_fields = {
        "name": "",
        "description": "",
        "type": "",
        "scope": ""
    }

    @classmethod
    def __str__(cls):
        return "rule_parameter"

    def __init__(self, *args):
        base = {}
        for arg in reversed(args):
            assert isinstance(arg, dict)
            base = dict(base.items() + arg.items())
        BaseWebModel.__init__(self, self.build_required_entities_only(base))