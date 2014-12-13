class Marco:

    def __init__(self, id_marco, size_marco, first_position, last_position):
        self.id_marco = id_marco
        self.size_marco = size_marco
        self.first_position = first_position
        self.last_position = last_position
        self.is_free = True
        self.position_read = first_position

    def set_is_full(self):
        self.is_free = False

    def get_is_free(self):
        return self.is_free

    def get_size(self):
        return self.size_marco

    def get_first_position(self):
        return self.first_position

    def get_last_position(self):
        return self.last_position

    def next_post(self):
        position = self.position_read
        self.position_read += 1
        return position