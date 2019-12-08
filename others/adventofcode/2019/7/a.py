#!/usr/bin/env python3

import sys

# input_values = [5]

def read_input():
	with open("input.txt", "r") as f:
		content = f.read()
		values = content.split(",")
		return list(map(int, values))

def read_input_test(ind):
    content = ""
    if ind == 0:
        content = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
    elif ind == 1:
        content = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
    elif ind == 2:
        content = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"

    values = content.split(",")
    return list(map(int, values))

class Machine:
    def __init__(self, machine_code, phase, signal):
        self.machine_code = machine_code.copy()

        self.inputs = [int(phase), int(signal)]
        self.outputs = []

    def read_input_value(self):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            raise Exception("No more values in input")

    def op_sum(self, p, state, mp1=0, mp2=0, mp3=0):
        pos1 = state[p+1]
        pos2 = state[p+2]
        pos3 = state[p+3]
        
        val1 = state[pos1] if mp1 == 0 else state[p+1]
        val2 = state[pos2] if mp2 == 0 else state[p+2]

        id3 = pos3 if mp3 == 0 else p+3
        state[id3] = val1 + val2
        
        return (p+4, state)
	
    def op_mult(self, p, state, mp1=0, mp2=0, mp3=0):
        
        pos1 = state[p+1]
        pos2 = state[p+2]
        pos3 = state[p+3]
        
        val1 = state[pos1] if mp1 == 0 else state[p+1]
        val2 = state[pos2] if mp2 == 0 else state[p+2]
        
        id3 = pos3 if mp3 == 0 else p+3
        state[id3] = val1 * val2
        
        return (p+4, state)
        
    def op_input(self, p, state, mp1=None, mp2=None, mp3=None, input_value=None):
        input_value = self.read_input_value()
        
        pos1 = state[p+1]
        state[pos1] = input_value
        
        return (p+2, state)
        
    def op_output(self, p, state, mp1=None, mp2=None, mp3=None):
        pos1 = state[p+1]
        value = state[pos1]
        # print(">>>", value)
        self.outputs.append(value)
        return (p+2, state)
        
    def op_jump_if_true(self, p, state, mp1=None, mp2=None, mp3=None):
        pos1 = state[p+1]
        pos2 = state[p+2]
        
        val1 = state[pos1] if mp1 == 0 else state[p+1]
        val2 = state[pos2] if mp2 == 0 else state[p+2]
        
        new_pos = p+3
        if int(val1) != 0:
            new_pos = int(val2)
        return (new_pos, state)
        
    def op_jump_if_false(self, p, state, mp1=None, mp2=None, mp3=None):
        pos1 = state[p+1]
        pos2 = state[p+2]
        
        val1 = state[pos1] if mp1 == 0 else state[p+1]
        val2 = state[pos2] if mp2 == 0 else state[p+2]
        
        new_pos = p+3
        if int(val1) == 0:
            new_pos = int(val2)
        return (new_pos, state)
        
    def op_less_than(self, p, state, mp1=None, mp2=None, mp3=None):
        pos1 = state[p+1]
        pos2 = state[p+2]
        pos3 = state[p+3]
        
        val1 = state[pos1] if mp1 == 0 else state[p+1]
        val2 = state[pos2] if mp2 == 0 else state[p+2]
        
        id3 = pos3 if mp3 == 0 else p+3
        
        if val1 < val2:
            state[id3] = 1
        else:
            state[id3] = 0
        
        return (p+4, state)
        
    def op_equals(self, p, state, mp1=None, mp2=None, mp3=None):
        pos1 = state[p+1]
        pos2 = state[p+2]
        pos3 = state[p+3]
        
        val1 = state[pos1] if mp1 == 0 else state[p+1]
        val2 = state[pos2] if mp2 == 0 else state[p+2]
        
        id3 = pos3 if mp3 == 0 else p+3
        
        if val1 == val2:
            state[id3] = 1
        else:
            state[id3] = 0
        
        return (p+4, state)
        
    def op_halt(self, p, state, mp1=None, mp2=None, mp3=None):
        return (-1, state)
        
    def get_op_handler(self, op_code):
        if op_code == 1:
            return self.op_sum
        elif op_code == 2:
            return self.op_mult
        elif op_code == 3:
            return self.op_input
        elif op_code == 4:
            return self.op_output
        elif op_code == 5:
            return self.op_jump_if_true
        elif op_code == 6:
            return self.op_jump_if_false
        elif op_code == 7:
            return self.op_less_than
        elif op_code == 8:
            return self.op_equals
        elif op_code == 99:
            return self.op_halt
        else:
            raise NotImplementedError("op_code {} not implemeted".format(op_code))
            
    def read_op_code(self, raw_op_code):
        s_i = "{}".format(raw_op_code)
        if len(s_i) == 1 or len(s_i) == 2:
            return (raw_op_code, 0, 0, 0)
        elif len(s_i) == 3:
            op_code = int(s_i[-2:])
            m1 = int(s_i[0])
            return (op_code, m1, 0, 0)
        elif len(s_i) == 4:
            op_code = int(s_i[-2:])
            m1 = int(s_i[1])
            m2 = int(s_i[0])
            return (op_code, m1, m2, 0)
        elif len(s_i) == 5:
            op_code = int(s_i[-2:])
            m1 = int(s_i[2])
            m2 = int(s_i[1])
            m3 = int(s_i[0])
            return (op_code, m1, m2, m3)
        else:
            raise Exception("Incorrect op_code: {}".format(raw_op_code))
            
    def execute(self):
        it = 0
        last_pos_code = len(self.machine_code)
        # print("ini")
        while it < last_pos_code:
            (op_code, mode_1, mode_2, mode_3) = self.read_op_code(self.machine_code[it])
            op_handler = self.get_op_handler(op_code)

            (new_it, new_state) = op_handler(it, self.machine_code, mode_1, mode_2, mode_3)
            
            if new_it < 0:
                # return new_state
                return self.outputs[-1]
            else:
                it = new_it
                self.machine_code = new_state
        
        # # return machine_code
        return self.outputs[-1]

def all_distinct(x):
    return len(x) == len(set(x))

def gen_num():
    for a in range(0, 5):
        for b in range(0, 5):
            for c in range(0, 5):
                for d in range(0, 5):
                    for e in range(0, 5):
                        if all_distinct([a, b, c, d, e]):
                            yield f"{a}{b}{c}{d}{e}"

	
if __name__ == "__main__":
    machine_code = read_input()
    # machine_code = read_input_test(2)
    result_phase = None
    result_value = -1
    for str_num in gen_num():
        # str_num = "{:05d}".format(num)
        # str_num = "43210"

        signal = 0
        for ind in range(0, 5):
            phase = int(str_num[ind])
            # print("IN:", phase, signal)
            machine = Machine(machine_code, phase, signal)
            signal = machine.execute()
            # print("OUT:", signal)

        # print(str_num, "->", signal)
        # break

        if signal > result_value:
            result_value = signal
            result_phase = str_num
        

    print("result_phase=", result_phase, "result_value=", result_value)

	
