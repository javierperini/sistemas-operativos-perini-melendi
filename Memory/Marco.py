class Marco:

    def __init__(self, id_marco, size_marco, first_position, last_position):
        self.id_marco = id_marco
        self.size_marco = size_marco
        self.first_position = first_position
        self.last_position = last_position
        self.is_free = True
        self.position_read = first_position
        self.position_free = first_position

    def set_is_full(self):
        self.is_free = False

    def get_is_free(self):
        return self.is_free

    def get_id(self):
        return self.id_marco

    def get_size(self):
        return self.size_marco

    def get_first_position(self):
        return self.first_position

    def get_last_position(self):
        return self.last_position

    def next_free_pos(self):
        position = self.position_free
        self.position_free += 1
        return position

    def next_post(self):
        position = self.position_read
        self.position_read += 1
        return position