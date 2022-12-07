from typing import List
from common import *


class DirCommand:
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return f"Dir: {self.path}"


class ListCommand:
    def __init__(self):
        self.results = []

    def add_result(self, result):
        self.results.append(result)

    def __str__(self):
        res = '\n'.join([str(x) for x in self.results])
        return f"List:\n{res}"


class ListCommandResult:
    def __init__(self, type, name, size=None):
        self.type = type
        self.name = name
        self.size = size

    @staticmethod
    def parse(line):
        [part1, part2] = line.split()
        if part1 == "dir":
            return ListCommandResult("dir", part2)
        else:
            return ListCommandResult("file", part2, part1)

    def __str__(self):
        return f"{self.type} - {self.name}"


class Directory:

    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.parent = parent

    def add(self, child):
        self.children.append(child)

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def get_size(self):
        return sum([child.get_size() for child in self.children])

    def get_file_path(self):
        res = f"{self.name}"
        if self.parent != None:
            res = self.parent.get_file_path() + "/" + res

        return res[1:] if res.startswith("//") else res

    def __str__(self):
        files = '\n'.join([str(x) for x in self.children])
        return f"{self.name} ({len(self.children)}):\n{files}"


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def __str__(self):
        return f"{self.size} {self.name}"


class Filesystem:
    def __init__(self):
        self.fs = None
        self.pointer = None

    def mkdir(self, name):
        new_dir = Directory(name, self.pointer)
        self.pointer.add(new_dir)

    def mkfile(self, name, size):
        new_file = File(name, size)
        self.pointer.add(new_file)

    def cwd(self, name):
        if name == "..":
            self.pointer = self.pointer.get_parent()
        elif name == "/":
            self.fs = Directory("/", None)
            self.pointer = self.fs
        else:
            for f in self.pointer.get_children():
                if isinstance(f, Directory) and f.name == name:
                    self.pointer = f
                    break

    def as_hash_dir(self):
        res = {}
        return self._add_hash_dir_child(self.fs, res)

    def _add_hash_dir_child(self, p, r):
        if isinstance(p, Directory):
            r[p.get_file_path()] = p.get_size()
            for pp in p.children:
                self._add_hash_dir_child(pp, r)

        return r

    def __str__(self):
        return f"{self.fs}"

    @staticmethod
    def from_session(session):
        fs = Filesystem()
        for command in session:
            if isinstance(command, DirCommand):
                fs.cwd(command.path)
            elif isinstance(command, ListCommand):
                for result in command.results:
                    if result.type == "dir":
                        fs.mkdir(result.name)
                    elif result.type == "file":
                        fs.mkfile(result.name, int(result.size))
        return fs


class CommandSession:
    def __init__(self):
        self.session = []

    def add_command(self, command):
        self.session.append(command)

    def get_last_command(self):
        return self.session[-1] if len(self.session) > 0 else None

    def __str__(self):
        return "\n".join([str(x) for x in self.session])

    def __iter__(self):
        return iter(self.session)

    @staticmethod
    def from_input(data):
        session = CommandSession()
        for line in data:
            if line.startswith('$'):
                [_, cmd] = line.split("$")
                if cmd.strip().startswith("cd"):
                    [_, path] = cmd.split()
                    session.add_command(DirCommand(path.strip()))
                elif cmd.strip().startswith("ls"):
                    session.add_command(ListCommand())
            else:
                last_command = session.get_last_command()
                if isinstance(last_command, ListCommand):
                    last_command.add_result(ListCommandResult.parse(line))

        return session


def calculate_result1(dir_tree):
    return sum([v for v in dir_tree.values() if v <= 100000])


def calculate_result2(dir_tree):
    TOTAL_SPACE = 70000000
    NEEDED_SPACE = 30000000
    root_size = dir_tree["/"]
    freed_space = TOTAL_SPACE - root_size

    sizes = sorted(dir_tree.values())
    for size in sizes:
        more_freed_space = freed_space + size
        if more_freed_space >= NEEDED_SPACE:
            return size


def day7_1(data: List[str]) -> int:
    session = CommandSession.from_input(data)
    root_dir = Filesystem.from_session(session)
    return calculate_result1(root_dir.as_hash_dir())


def day7_2(data: List[str]) -> int:
    session = CommandSession.from_input(data)
    root_dir = Filesystem.from_session(session)
    return calculate_result2(root_dir.as_hash_dir())


if __name__ == "__main__":
    data = read_data(7, parser=str, test=True)
    do(7, data, answers=[95437, 24933642], test=True)
    data = read_data(7, parser=str)
    do(7, data, answers=[1334506, 7421137])
