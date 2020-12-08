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
        print(sp)
        return Instruction(sp[0], int(sp[1]))

    def __str__(self):
        return f"{self.type} ({self.arg0})"

class Machine:
    def __init__(self):
        self.instructions = []
        self.registers = {
            'accumulator': 0
        }
        self.pointer = 0
        self.path = []

    def load_program_from_lines(self, lines):
        self.instructions = list([Instruction.read_from_line(line) for line in lines])

    def execute(self):
        while self.pointer < len(self.instructions)-1:
            if self.pointer in self.path:
                break

            ins = self.instructions[self.pointer]
            print(self.pointer, ins, self.registers['accumulator'])
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
        

    def get_register_value(self, register_name):
        return self.registers[register_name]

def main():
    lines = load_data()

    m = Machine()
    m.load_program_from_lines(lines)
    m.execute()
    res = m.get_register_value("accumulator")
    print("Res=", res)

if __name__ == "__main__":
    main()
