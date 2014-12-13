class Page:

    def __init__(self, marco):
        self.size = marco.get_size()
        self.instruction = []
        self.marco = marco
        self.associate_marco(marco)

    def associate_marco(self, marco):
        marco.set_is_full()

    def get_marco(self):
        return self.marco

    def get_size(self):
        return self.size

    def add_number_instruction(self, instrution):
        self.instruction = instrution

