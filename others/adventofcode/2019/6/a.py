#!/usr/bin/env python3

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
    for orbit_map in orbit_maps:
        (objBase, objOrbit) = parse_orbit_map(orbit_map)
        tree.add_orbit(objOrbit, objBase)

    res = sum(map(tree.calculate_number_orbits, tree.get_objects()))
    print(res)
