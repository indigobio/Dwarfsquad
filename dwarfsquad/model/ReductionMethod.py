from dwarfsquad.model.BaseWebModel import BaseWebModel


class ReductionMethod(BaseWebModel):
    required_fields = {
        "activation_energy": "",
        "polarity": "unspecified",
        "lower_precursor_mass": "",
        "upper_precursor_mass": "",
        "lower_product_mass": "",
        "upper_product_mass": "",
        "combine_ions": False
    }

    @classmethod
    def __str__(cls):
        return "reduction method"

    def __init__(self, *args):
        base = {}
        for arg in reversed(args):
            assert isinstance(arg, dict)
            base = {**base, **arg}

        BaseWebModel.__init__(self, self.build_required_entities_only(base))

    def set_activation_energy(self, activation_energy):
        try:
            self.activation_energy = float(activation_energy)
        except ValueError:
            self.activation_energy = None

    def set_polarity(self, polarity):
        try:
            assert isinstance(polarity, str)
            assert polarity.lower() in ['unspecified', 'positive', 'negative']
            self.polarity = polarity.lower()
        except AssertionError:
            self.polarity = 'unspecified'

    def set_lower_precursor_mass(self, lower_precursor_mass):
        try:
            self.lower_precursor_mass = float(lower_precursor_mass)
        except ValueError:
            self.lower_precursor_mass = ""

    def set_upper_precursor_mass(self, upper_precursor_mass):
        try:
            self.upper_precursor_mass = float(upper_precursor_mass)
        except ValueError:
            self.upper_precursor_mass = ""

    def set_lower_product_mass(self, lower_product_mass):
        assert isinstance(float(lower_product_mass), float)
        self.lower_product_mass = lower_product_mass

    def set_upper_product_mass(self, upper_product_mass):
        assert isinstance(float(upper_product_mass), float)
        self.upper_product_mass = upper_product_mass

    def set_combine_ions(self, combine_ions):
        self.combine_ions = str(combine_ions).lower() == "true"
