#!/usr/bin/env python3

TEST_DATA = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
"""

class OrbitTree:
    def __init__(self):
        self.orbits = {}
        self._base_root = "COM"

    def add_orbit(self, objOrbit, objBase):
        self.orbits[objOrbit] = objBase

    def get_objects(self):
        return list(self.orbits.keys())

    def calculate_number_orbits(self, obj_name):
        if obj_name == self._base_root:
            return 0
        else:
            return 1 + self.calculate_number_orbits(self.orbits[obj_name])

    def get_path_to_root(self, obj_name, res_list):
        next_obj = self.orbits[obj_name]
        if next_obj == self._base_root:
            return res_list
        else:
            res_list.append(next_obj)
            return self.get_path_to_root(next_obj, res_list)


    def calculate_min_distance(self, pa, pb):
        path_you = self.get_path_to_root("YOU", [])
        path_san = self.get_path_to_root("SAN", [])

        for y_it in range(len(path_you)):
            y = path_you[y_it]
            for s_it in range(len(path_san)):
                s = path_san[s_it]
                if y == s:
                    return y_it + s_it

        return 0

def load_test_data():
    return TEST_DATA.split()

def load_input():
    lines = []
    with open("input.txt", "r") as f:
        for line in f:
            lines.append(line.strip())

    return lines

def parse_orbit_map(orbit_map):
    splitted = orbit_map.split(")")
    return (splitted[0], splitted[1])

if __name__ == '__main__':
    tree = OrbitTree()
    orbit_maps = load_input()
    # orbit_maps = load_test_data()
    for orbit_map in orbit_maps:
        (objBase, objOrbit) = parse_orbit_map(orbit_map)
        tree.add_orbit(objOrbit, objBase)

    print(tree.calculate_min_distance("YOU", "SAN"))
