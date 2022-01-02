from __future__ import annotations


class Trajectory():
    def __init__(self, src: tuple, dst: tuple) -> None:
        self.src = src
        self.dst = dst

        x1, y1, z1 = src
        x2, y2, z2 = dst

        self.distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
        self.direction = (x2 - x1, y2 - y1, z2 - z1)
        self.alt_direction = (x1 - x2, y1 - y2, z1 - z2)

    def __repr__(self) -> str:
        return f"{self.src} -> {self.dst}"

    def get_src(self) -> tuple:
        return self.src

    def get_dst(self) -> tuple:
        return self.dst

    def get_distance(self) -> tuple:
        return self.distance

    def get_direction_vectors(self) -> set:
        return set([self.direction, self.alt_direction])

    def __eq__(self, __o: Trajectory) -> bool:
        if not isinstance(__o, Trajectory):
            return NotImplemented()

        return self.get_direction_vectors() == __o.get_direction_vectors() and self.get_distance() == __o.get_distance()

    def eq_dist(self, __o: Trajectory) -> bool:
        if not isinstance(__o, Trajectory):
            return NotImplemented()

        return self.get_distance() == __o.get_distance()

    def get_reference_translation(self, other_trajectory: Trajectory) -> tuple:
        if not isinstance(other_trajectory, Trajectory):
            return NotImplemented()
        # TODO
        return NotImplemented()
        # (3,6,6) = (-9,5,6) -> (x, y, z) = (0,0,0) | (-7,11,12)
