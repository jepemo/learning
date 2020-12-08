
import pprint
import copy

def load_data():
    with open("input.txt") as f:
        return f.read().split("\n")

def load_test_data():
    return """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".split("\n")

class Instruction:
    def __init__(self, _type, _arg0):
        self.type = _type
        self.arg0 = _arg0
    
    @staticmethod
    def read_from_line(line):
        sp = line.split()
        return Instruction(sp[0], int(sp[1]))

    def __repr__(self):
        return f"{self.type} ({self.arg0})"

    def __str__(self):
        return f"{self.type} ({self.arg0})"

def programs_generator(lines):
    base = list([Instruction.read_from_line(line) for line in lines])
    for ind in range(0, len(base)):
        ins = base[ind]
        if ins.type == "jmp":
            new = copy.deepcopy(base)
            new[ind].type = "nop"
            yield new
        elif ins.type == "nop":
            new = copy.deepcopy(base)
            new[ind].type = "jmp"
            yield new

class Machine:
    def __init__(self):
        self._reset()

    def _reset(self):
        self.instructions = []
        self.registers = {
            'accumulator': 0
        }
        self.pointer = 0
        self.path = []
        self.trace = []

    def load_program(self, instructions):
        self._reset()
        self.instructions = instructions 

    def load_program_from_lines(self, lines):
        self.instructions = list([Instruction.read_from_line(line) for line in lines])

    def execute(self):
        while self.pointer < len(self.instructions):
            if self.pointer in self.path:
                return 1

            ins = self.instructions[self.pointer]
            # self.trace.append(f"P:{self.pointer}, {}")print(self.pointer, ins, self.registers['accumulator'])
            self.path.append(self.pointer)
            if ins.type == "acc":
                self.registers['accumulator'] += ins.arg0
                self.pointer += 1
            elif ins.type == "jmp":
                self.pointer += ins.arg0
            elif ins.type == "nop":
                self.pointer += 1
            else:
                print("Error instruction not recognized", ins.type)

        return 0
        

    def get_register_value(self, register_name):
        return self.registers[register_name]

def main():
    lines = load_data()

    m = Machine()
    for program in programs_generator(lines):
        # pprint.pprint(program)
        m.load_program(program)
        status = m.execute()
        # print("Status=", status, "Acc=", m.get_register_value("accumulator"))
        if status == 0:
            res = m.get_register_value("accumulator")
            print("Res=", res)

if __name__ == "__main__":
    main()
