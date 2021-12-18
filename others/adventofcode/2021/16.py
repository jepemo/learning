from common import *
import sys
import math


def test_and_result():
    return [
        # ('D2FE28', 2021),
        # ('38006F45291200', 30),
        # ('EE00D40C823060', 6),
        ('8A004A801A8002F478', 16),
        ('620080001611562C8802118E34', 12),
        ('C0015000016115A2E0802F182340', 23),
        ('A0016C880162017C3686B18A3D4780', 31)
    ]


class PacketParser:
    def __init__(self):
        pass

    def hex_to_binary(self, hex_data):
        return bin(int(hex_data, 16))[2:].zfill(8)

    def bin_to_num(self, bin_seq):
        val = ''.join(bin_seq)
        return int(f'0b{val}', 2)

    def read_version(self, bin_seq):
        return (self.bin_to_num(bin_seq[0:3]), bin_seq[3:])

    def read_type_id(self, bin_seq):
        return (self.bin_to_num(bin_seq[0:3]), bin_seq[3:])

    def read_length_type(self, bin_list):
        return (bin_list[0], bin_list[1:])

    def read_num_digits(self, length_type, bin_list):
        if length_type == '0':
            return (self.bin_to_num(bin_list[0:15]), True, bin_list[15:])
        else:
            return (self.bin_to_num(bin_list[0:11]), False, bin_list[11:])

    def parse_digits(self, bin_seq):
        num_list = []
        ind = 0
        for i in range(0, len(bin_seq), 5):
            vals = bin_seq[i+1:i+5]
            num_list.extend(vals)

            if bin_seq[i] == '0':
                ind = i+5
                break

        num = self.bin_to_num(num_list)

        return (num, bin_seq[ind:])

    def parse(self, sequence):
        print("-------")
        print("Parse: ", sequence)
        bin_str = self.hex_to_binary(sequence)
        bin_list = list(bin_str)
        # print(len(bin_list))
        # print(''.join(bin_list))
        if len(bin_list) % 4 != 0:
            zeros = ['0' for _i in range(4-(len(bin_list) % 4))]
            bin_list = zeros + bin_list

        (value, _bin_list) = self._parse_binary(bin_list)
        return value

    def _parse_binary(self, bin_list, ident=''):
        data = {}
        data["children"] = []

        print(ident, f"Packet: {''.join(bin_list)}")
        (version, bin_list) = self.read_version(bin_list)
        print(ident, "Version=", version)
        data["version"] = version
        (type_id, bin_list) = self.read_type_id(bin_list)
        print(ident, "TypeId=", type_id)
        data["type_id"] = type_id
        if (type_id == 4):
            (value, bin_list) = self.parse_digits(bin_list)
            print(ident, "Value=", value)
            data["value"] = value
            return (data, bin_list)
        else:
            (length_type, bin_list) = self.read_length_type(bin_list)
            print(ident, "LengthType=", length_type)
            data["length_type"] = length_type
            (num_digits, is_num_bits, bin_list) = self.read_num_digits(
                length_type, bin_list)
            if is_num_bits:
                print(ident, "NumBits=", num_digits)
                data["num_bits"] = num_digits
                sublist = [x for x in bin_list[0:num_digits]]
                bin_list = bin_list[num_digits:]
                values = []
                while sublist != []:
                    (value, sublist) = self._parse_binary(
                        sublist, ident=ident+' ')
                    values.append(value)
                data["children"] = values
            else:
                print(ident, "NumSubPackets=", num_digits)
                data["num_subpackages"] = num_digits
                values = []
                for i in range(num_digits):
                    (value, bin_list) = self._parse_binary(
                        bin_list, ident=ident+' ')
                    values.append(value)
                data["children"] = values

        print(ident, "Values=", values)
        return (data, bin_list)


def test_and_result2():
    return [
        ('C200B40A82', 3),
        # ('04005AC33890', 54),
        ('880086C3E88112', 7),
        ('CE00C43D881120', 9),
        ('D8005AC2A8F0', 1),
        ('F600BC2D8F', 0),
        ('9C005AC2F8F0', 0),
        ('9C0141080250320F1802104A08', 1),
    ]


# 010
# 000
# 00000001011010110000110011100010010000


class PacketCalculator:
    def __init__(self):
        pass

    def calculate(self, tree):
        type_id = tree["type_id"]
        if type_id == 4:
            return tree["value"]
        else:
            child_values = [self.calculate(x) for x in tree["children"]]
            if type_id == 0:
                return sum(child_values)
            elif type_id == 1:
                return math.prod(child_values)
            elif type_id == 2:
                return min(child_values)
            elif type_id == 3:
                return max(child_values)
            elif type_id == 5:
                return 1 if child_values[0] > child_values[1] else 0
            elif type_id == 6:
                return 1 if child_values[0] < child_values[1] else 0
            elif type_id == 7:
                return 1 if child_values[0] == child_values[1] else 0
        sys.exit(1)
        # return -1


def get_versions(data):
    versions = []
    versions.append(data["version"])
    for child in data["children"]:
        versions.extend(get_versions(child))

    return versions


def calc_1(test):
    parser = PacketParser()
    data = parser.parse(test)
    versions = get_versions(data)
    return sum(versions)


def calc_2(test):
    parser = PacketParser()
    tree = parser.parse(test)

    calc = PacketCalculator()
    return calc.calculate(tree)


if __name__ == "__main__":
    # print(int(b'0b01111', 2))
    # sys.exit(0)
    # for (test, result) in test_and_result():
    #     val = calc_1(test)
    #     if (val != result):
    #         print(f"Input: {test}, Expected: {result} != {val} :Calculated")
    #         break
    #     else:
    #         print(f"Input: {test} -> {val} OK!")

    # with open('data/input16.txt') as fin:
    #     inp = fin.read()
    #     print(calc_1(inp))

    # for (test, result) in test_and_result2():
    #     val = calc_2(test)
    #     if (val != result):
    #         print(f"Input: {test}, Expected: {result} != {val} :Calculated")
    #         break
    #     else:
    #         print(f"Input: {test} -> {result} == {val} OK!")

    with open('data/input16.txt') as fin:
        inp = fin.read()
        print(calc_2(inp))
