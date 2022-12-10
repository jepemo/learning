from typing import List
from common import *
from dataclasses import dataclass


@dataclass
class Add:
    value: int


@dataclass
class Noop:
    pass


# class Machine:
#     def __init__(self, instructions):
#         self.instructions = instructions
#         self.register = 1
#         self.cycle_num = 0
#         self.current = None

#     def cycle(self):
#         if len(self.instructions) == 0:
#             return -1

#         self.cycle_num += 1
#         # print("->", self.cycle_num, len(self.instructions),
#         #       self.current, self.register)
#         if self.current != None:
#             if self.current.num_cycles > 0:
#                 self.current.num_cycles -= 1
#                 if self.current.num_cycles == 0:
#                     if isinstance(self.current, Add):
#                         self.register += self.current.value
#                     if len(self.instructions) > 0:
#                         self.current = self.instructions.pop(0)
#         else:
#             self.current = self.instructions.pop(0)
#             self.current.num_cycles -= 1

#         return self.cycle_num

#     def get_register(self):
#         return self.register


class Machine:
    def __init__(self, instructions):
        self.instructions = instructions

    def simulate(self):
        result = []
        register = 1
        cycle = 1
        last_instr = None
        for instr in self.instructions:
            if last_instr != None and isinstance(last_instr, Add):
                register += last_instr.value

            if isinstance(instr, Noop):
                result.append((cycle, instr, register))
                cycle += 1
            elif isinstance(instr, Add):
                result.append((cycle, instr, register))
                result.append((cycle+1, instr, register))
                cycle += 2

            last_instr = instr

        return result


def parse_instruction(line):
    if line.strip().startswith("noop"):
        return Noop()
    elif line.strip().startswith("addx"):
        parts = line.split()
        return Add(int(parts[1]))


def day10_1(data: List[str]) -> int:
    instructions = list(map(parse_instruction, data))
    machine = Machine(instructions)
    trace = machine.simulate()
    result = 0
    for t in trace:
        (idx, _, v) = t
        if idx % 40 == 20:
            result += (idx * v)
        else:
            pass

    return result


def day10_2(data: List[str]) -> int:
    instructions = list(map(parse_instruction, data))
    machine = Machine(instructions)
    trace = machine.simulate()
    for t in trace:
        (idx, _, v) = t
        xpos = (idx-1) % 40
        if xpos in [v-1, v, v+1]:
            # if xpos == v:
            print("#", end='')
        else:
            print(".", end='')

        # print(t)

        if idx % 40 == 0:
            print("")

    return 0


if __name__ == "__main__":
    data = read_data(10, parser=str, test=True)
    do(10, data, answers=[13140, 0], test=True)
    data = read_data(10, parser=str)
    do(10, data, answers=[12840, 0])
