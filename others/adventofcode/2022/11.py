from typing import List
from common import *

OP_SUM = 1
OP_MULT = 2


class Monkey:
    def __init__(self, num, initial_items, worry_operator, worry_level, test, test_if_true, test_if_false):
        self.num = num
        self.worry_operator = OP_SUM if worry_operator == "+" else OP_MULT
        self.worry_level = -1 if worry_level == "old" else int(worry_level)
        self.items = initial_items
        self.test = test
        self.test_if_true = test_if_true
        self.test_if_false = test_if_false
        self.num_inspected_items = 0
        self.manager = None

    def _calc_worry(self, value):
        operand = value if self.worry_level == -1 else self.worry_level

        if self.worry_operator == OP_SUM:
            return value + operand
        elif self.worry_operator == OP_MULT:
            return value * operand

        # raise NotImplemented()

    def process(self, divided_by):
        # print("Process:", len(self.items), "items")
        while True:
            # print("----> ", len(self.items), "items left")
            if len(self.items) == 0:
                break

            self.num_inspected_items += 1
            item = self.items.pop(0)

            worry = self._calc_worry(item)
            worry_level = worry // (1 if divided_by < 0 else divided_by)
            if (worry_level % self.test) == 0:
                self.manager.append_to_monkey(
                    self.test_if_true, item if divided_by < 0 else worry_level)
            else:
                self.manager.append_to_monkey(
                    self.test_if_false, item if divided_by < 0 else worry_level)
            # print("---> Finished", self.num)
            # self.manager.print()

    def __str__(self):
        # return f"Monkey {self.num}\t{self.items}"
        return f"Monkey {self.num}\t(worry={self.worry_operator}{self.worry_level})\t(test={self.test} / true: {self.test_if_true} false: {self.test_if_false})\t{self.items}"


class MonkeyManager:
    def __init__(self, monkeys):
        self.monkeys = monkeys
        for m in monkeys:
            m.manager = self

    def append_to_monkey(self, idx, val):
        self.monkeys[idx].items.append(val)

    def print(self):
        for m in self.monkeys:
            print(m)


def parse_input(lines):
    monkeys = []
    idx = None
    items = []
    worry_operator = None
    worry_level = None
    test = None
    test_if_true = None
    test_if_false = None
    for line in lines:
        line = line.strip()
        if line.startswith("Monkey"):
            if idx != None:
                monkeys.append(
                    Monkey(idx, items, worry_operator, worry_level, test, test_if_true, test_if_false))
            [_, num] = line.split()
            idx = int(''.join(num[0:-1]))
        elif line.startswith("Starting"):
            nums = line.split(":")
            items = list(map(int, nums[1].split(",")))
        elif line.startswith("Operation"):
            parts = line.split("=")
            parts = parts[1].split()
            worry_operator = parts[1].strip()
            worry_level = parts[2].strip()
        elif line.startswith("Test"):
            parts = line.split("by")
            test = int(parts[1].strip())
        elif line.startswith("If true"):
            parts = line.split("monkey")
            test_if_true = int(parts[1].strip())
        elif line.startswith("If false"):
            parts = line.split("monkey")
            test_if_false = int(parts[1].strip())

    monkeys.append(
        Monkey(idx, items, worry_operator, worry_level, test, test_if_true, test_if_false))

    return monkeys


def day11_1(data: List[str]) -> int:
    monkeys = parse_input(data)
    monkey_manager = MonkeyManager(monkeys)

    print("initial:")
    for m in monkeys:
        print(m)

    for i in range(20):
        # print("\nround:", i)
        for m in monkeys:
            # print("------> Processing monkey:", m.num)
            m.process(3)
            # print(m)

    xx = list(sorted(map(lambda x: x.num_inspected_items, monkeys), reverse=True))
    # print(xx)
    return xx[0] * xx[1]


def day11_2(data: List[str]) -> int:

    for i in range(1, 10000):
        monkeys = parse_input(data)
        monkey_manager = MonkeyManager(monkeys)
        for m in monkeys:
            m.process(i)

        if list(map(lambda x: x.num_inspected_items, monkeys)) == [2, 4, 3, 6]:
            print("Res:", i)
    # break

    monkeys = parse_input(data)
    monkey_manager = MonkeyManager(monkeys)

    print("initial:")
    for m in monkeys:
        print(m)

    for i in range(10000):
        # print("\nround:", i)
        for m in monkeys:
            # print("------> Processing monkey:", m.num)
            m.process(-1)
            # print(m)

        if i+1 in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
            print(f"== After round {i} ==")
            for m in monkeys:
                print(
                    f"Monkey {m.num} inspected items {m.num_inspected_items} times.")

    xx = list(sorted(map(lambda x: x.num_inspected_items, monkeys), reverse=True))
    print(xx)
    return xx[0] * xx[1]


if __name__ == "__main__":
    data = read_data(11, parser=str, test=True)
    do(11, data, answers=[10605, 2713310158], test=True)
    # data = read_data(11, parser=str)
    # do(11, data, answers=[0, 0])
