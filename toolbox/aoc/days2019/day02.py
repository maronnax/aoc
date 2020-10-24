import copy

class Opcode:
    OP1_ADD = 1
    OP2_MULT = 2
    OP3_HALT = 99


class Computer:
    def __init__(self, state):
        self.internal_state = copy.copy(state)
        self.instruction_ndx = 0

    def advance_state(self):
        self.op = self.internal_state[self.instruction_ndx]
        self.execute_command(self.op, self.instruction_ndx)
        self.instruction_ndx += 4
        return

    def run(self):
        try:
            while True:
                self.advance_state()
        except StopIteration:
            pass

        return copy.copy(self.internal_state)

    def execute_command(self, op, ndx):
        if self.op == Opcode.OP1_ADD:
            self.internal_state[self.internal_state[ndx+3]] = self.internal_state[self.internal_state[ndx+2]] + self.internal_state[self.internal_state[ndx+1]]
        elif self.op == Opcode.OP2_MULT:
            self.internal_state[self.internal_state[ndx+3]] = self.internal_state[self.internal_state[ndx+2]] * self.internal_state[self.internal_state[ndx+1]]
        elif self.op == Opcode.OP3_HALT:
            raise StopIteration()
        else:
            raise RuntimeError(f"Unknown Opcode {op} at position {ndx}")
