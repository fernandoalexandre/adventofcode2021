from math import ceil, floor
from uuid import uuid4


class Node():
    def __init__(self, value: list | int, depth) -> None:
        self.parent = None
        self.left = None
        self.right = None
        self.depth = depth
        self.value = value
        self.id = uuid4()

    # build-in functions
    def __repr__(self) -> str:
        curr_str = ""
        if self.value is not None:
            return str(self.value)

        if self.left is not None:
            curr_str += f"[{self.left},"

        if self.right is not None:
            curr_str += f"{self.right}]"

        return curr_str

    def __eq__(self, other):
        if not isinstance(other, Node):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.id == other.id
    # ########

    def print_root(self) -> None:
        if self.parent is not None:
            self.parent.print_root()
        else:
            print(self)

    def get_value(self) -> None:
        return self.value

    def add_depth(self, amount: int) -> None:
        self.depth += amount
        if self.left is not None:
            self.left.add_depth(amount)
        if self.right is not None:
            self.right.add_depth(amount)

    def set_parent(self, parent) -> None:
        self.parent = parent

    def set_left(self, left) -> None:
        self.left = left
        self.left.set_parent(self)

    def set_right(self, right) -> None:
        self.right = right
        self.right.set_parent(self)

    def split(self) -> bool:
        if self.has_value():
            if self.value >= 10:
                # print(f"Splitting {self.value}")
                self.set_left(Node(floor(self.value/2), self.depth+1))
                self.set_right(Node(ceil(self.value/2),  self.depth+1))
                self.value = None

                if self.depth > 3:
                    # print(f"Exploding {self}")
                    # self.print_root()
                    self.expurosion()
                return True
        else:
            has_changed = False
            if self.left is not None:
                has_changed = has_changed or self.left.split()
            if self.right is not None:
                has_changed = has_changed or self.right.split()

            return has_changed
        return False

    def sum_value(self, value: int) -> None:
        self.value += value

    def has_pair(self) -> bool:
        return self.value is None and self.left.get_value() is not None and self.right.get_value() is not None

    def has_value(self) -> bool:
        return self.value is not None

    def has_parent(self) -> bool:
        return self.parent is not None

    def get_magnitude(self) -> int:
        total = 0
        if self.left.has_value():
            total += 3 * self.left.get_value()
        else:
            total += 3 * self.left.get_magnitude()

        if self.right.has_value():
            total += 2 * self.right.get_value()
        else:
            total += 2 * self.right.get_magnitude()

        return total

    def get_max_depth(self):
        if self.has_value():
            return self.depth
        return max(self.left.get_max_depth(), self.right.get_max_depth())

    def up_expurosion(self, source, direction: str, value: int):
        is_source_left = source == self.left
        is_source_right = source == self.right

        if (is_source_left and direction == "left") or (is_source_right and direction == "right"):
            if self.has_parent():
                self.parent.up_expurosion(self, direction, value)
            else:
                # Nothing to do, we hit root on a direction there is nothing else to do
                return None

        if is_source_left and direction == "right":
            self.right.down_expurosion("left", value)

        if is_source_right and direction == "left":
            self.left.down_expurosion("right", value)

        if self.has_pair() and self.depth > 3:
            self.expurosion()

    def down_expurosion(self, direction: str, value: int) -> None:
        if self.has_value():
            # print(f"{self} , {self.get_value()} + {value}")
            self.sum_value(value)
        else:
            if direction == "left":
                self.left.down_expurosion(direction, value)
            else:
                self.right.down_expurosion(direction, value)

    def expurosion(self):
        # EXPUROSION
        # print(f"Expurosion! {self}")
        left_value = self.left.get_value()
        right_value = self.right.get_value()

        self.left = None
        self.right = None
        self.value = 0

        self.parent.up_expurosion(self, "left", left_value)
        self.parent.up_expurosion(self, "right", right_value)

    def explode(self):
        # If any pair is nested inside four pairs, the leftmost such pair explodes.
        # If any regular number is 10 or greater, the leftmost such regular number splits.

        # print(f"Processing depth {self.depth}: {self}")
        if self.has_pair():
            self.expurosion() if self.depth > 3 else None
        else:
            if self.left is not None:
                self.left.explode()
            if self.right is not None:
                self.right.explode()

        if self.parent is None:
            has_changed = self.split()
            while has_changed:
                self.explode()
                has_changed = self.split()
