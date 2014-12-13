class MemoryAdmin:
    def __init__(self, memory, strategy):
        self.memory = memory
        self.strategy = strategy

    def save(self, pcb, program):
        self.strategy.save(pcb, program)

    def has_run_for(self, size):
        self.strategy.has_run_for(size)

    def next_post_free(self):
        return self.strategy.next_pos_free()

    def next_post(self):
        return self.strategy.next_position()

    def read_memory(self, pcb):
        return self.strategy.get_next_instruction(pcb)

    def delete_memory(self, program):
        self.strategy.delete_memory(program)

