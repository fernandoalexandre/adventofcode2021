import ast
from node import Node
from copy import deepcopy


def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()


class Tree():
    def __init__(self, data: list):
        self.root = self.parse(data, 0)
        self.depth = 0

    def add_p1(self, addee: Node) -> None:
        print(f"{self.root}  +  {addee.get_root()}")
        new_root = Node(None, -1)
        new_root.set_left(self.root)
        new_root.set_right(addee.get_root())
        self.root = new_root
        new_root.add_depth(1)

        # starting some $%#%

        if self.root.get_max_depth() > 3:
            self.root.explode()

        #print(f"New Root: {self.root}")

    def get_root(self) -> Node:
        return self.root

    def parse(self, data: list, depth=0) -> Node:
        # Leaf
        current_node = Node(None, depth)
        if isinstance(data[0], int):
            current_node.set_left(Node(data[0], depth+1))
        else:
            current_node.set_left(self.parse(data[0], depth + 1))

        if isinstance(data[1], int):
            current_node.set_right(Node(data[1], depth+1))
        else:
            current_node.set_right(self.parse(data[1], depth + 1))

        return current_node

    def get_magnitude(self) -> int:
        return self.root.get_magnitude()


def part1(list_eq: list) -> None:
    print("--- Part 1 Ship-it ---")

    current_eq = list_eq[0]
    for i in range(1, len(list_eq)):
        current_eq.add_p1(list_eq[i])

    print(f"Part 1: {current_eq.get_magnitude()}")


def part2(content: list) -> None:
    print("--- Part 2 Ship-it ---")

    part2 = 0

    for i in range(0, len(content)):
        for j in range(0, len(content)):
            if i == j:
                continue

            f = deepcopy(Tree(ast.literal_eval(content[i].rstrip("\n"))))
            s = deepcopy(Tree(ast.literal_eval(content[j].rstrip("\n"))))

            f.add_p1(s)
            part2 = max(part2, f.get_magnitude())

    print(f"Part 2: {part2}")


def main():
    content = read_file("day18/input")

    list_eq = []
    for line in content:
        list_eq.append(Tree(ast.literal_eval(line.rstrip("\n"))))

    print("-------------- Part 1 ------------------")

    part1(list_eq)

    print("-------------- Part 2 ------------------")

    part2(content)


if __name__ == "__main__":
    main()
