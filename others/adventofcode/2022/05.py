import math

from typing import List
from common import *


def parse_stack(data):
    num_elems = int(math.ceil(len(data[0]) / 4))
    stacks = [[] for x in range(num_elems)]
    for line in data:
        if line.startswith(" 1"):
            break

        col = 0
        for i in range(0, len(data[0]), 4):
            elem = line[i:i+3]
            if elem.startswith("["):
                chars = [x for x in elem]
                stacks[col].append(chars[1])
            col += 1

    return stacks


def parse_moves(data):
    moves = []
    for line in data:
        if line.startswith('move'):
            [_move, num_elems, _from, orig, _to, dest] = line.split()
            moves.append({
                "num": int(num_elems),
                "orig": int(orig),
                "dest": int(dest)
            })

    return moves


def update_stack(stack, move):
    orig_idx = move['orig'] - 1
    dest_idx = move['dest'] - 1
    stack_orig = stack[orig_idx]
    stack_dest = stack[dest_idx]
    for i in range(move['num']):
        elem = stack_orig.pop(0)
        stack_dest.insert(0, elem)
    stack[orig_idx] = stack_orig
    stack[dest_idx] = stack_dest
    return stack


def update_stack_9001(stack, move):
    orig_idx = move['orig'] - 1
    dest_idx = move['dest'] - 1
    num = move['num']
    stack_orig = stack[orig_idx]
    stack_dest = stack[dest_idx]
    elems = stack_orig[0:num]
    stack_orig = stack_orig[num:]
    stack_dest = elems + stack_dest
    stack[orig_idx] = stack_orig
    stack[dest_idx] = stack_dest
    return stack


def get_top_elems(stack):
    return ''.join([x[0] for x in stack])


def day5_1(data: List[str]) -> int:
    stack = parse_stack(data)
    moves = parse_moves(data)

    for move in moves:
        stack = update_stack(stack, move)

    return get_top_elems(stack)


def day5_2(data: List[str]) -> int:
    stack = parse_stack(data)
    moves = parse_moves(data)

    for move in moves:
        stack = update_stack_9001(stack, move)

    return get_top_elems(stack)


if __name__ == "__main__":
    data = read_data(5, parser=str, test=True)
    do(5, data, answers=['CMZ', 'MCD'], test=True)
    data = read_data(5, parser=str)
    do(5, data, answers=['FWNSHLDNZ', 'RNRGDNFQG'])
