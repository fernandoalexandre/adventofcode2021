from __future__ import annotations


class Trajectory():
    def __init__(self, src: tuple, dst: tuple) -> None:
        self.src: tuple = src
        self.dst: tuple = dst

        self._update_trajectory()

    def __repr__(self) -> str:
        return f"{self.src} -> {self.dst}"

    def __hash__(self) -> int:
        return int(self.get_distance() * 10000000)

    def get_src(self) -> tuple:
        return self.src

    def get_dst(self) -> tuple:
        return self.dst

    def get_distance(self) -> tuple:
        return self.distance

    def get_direction_vectors(self) -> list[tuple]:
        return [self.direction, self.alt_direction]

    def _update_trajectory(self):
        x1, y1, z1 = self.src
        x2, y2, z2 = self.dst

        self.distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
        self.direction = (x2 - x1, y2 - y1, z2 - z1)
        self.alt_direction = (x1 - x2, y1 - y2, z1 - z2)

    def __eq__(self, __o: Trajectory) -> bool:
        if not isinstance(__o, Trajectory):
            return NotImplemented()

        return self.get_distance() == __o.get_distance()

    def eq_dist(self, __o: Trajectory) -> bool:
        if not isinstance(__o, Trajectory):
            return NotImplemented()

        return self.get_distance() == __o.get_distance()

    def swap_coordinates(self, swap_idx: tuple) -> None:
        new_src = [self.src[swap_idx[0]], self.src[swap_idx[1]], self.src[swap_idx[2]]]
        new_dst = [self.dst[swap_idx[0]], self.dst[swap_idx[1]], self.dst[swap_idx[2]]]

        # print(f"swap {swap_idx}")
        # print(f"{self.src} -> {tuple(new_src)}")
        # print(f"{self.dst} -> {tuple(new_dst)}")
        # print(f"trajectory = {self.direction}")

        self.src = tuple(new_src)
        self.dst = tuple(new_dst)

        self._update_trajectory()
        # print(f"trajectory = {self.direction}")

    def multiply_coordinates(self, coeficient: tuple) -> None:
        self.src = (
            self.src[0]*coeficient[0],
            self.src[1]*coeficient[1],
            self.src[2]*coeficient[2],
        )

        self.dst = (
            self.dst[0]*coeficient[0],
            self.dst[1]*coeficient[1],
            self.dst[2]*coeficient[2],
        )

        self._update_trajectory()

    def add_coordinates(self, coeficient: tuple) -> None:
        self.src = (
            self.src[0]+coeficient[0],
            self.src[1]+coeficient[1],
            self.src[2]+coeficient[2],
        )

        self.dst = (
            self.dst[0]+coeficient[0],
            self.dst[1]+coeficient[1],
            self.dst[2]+coeficient[2],
        )

        self._update_trajectory()

    def get_reference_translation(self, other_trajectory: Trajectory) -> tuple:
        if not isinstance(other_trajectory, Trajectory):
            return NotImplemented()
        # TODO
        return NotImplemented()
        # (3,6,6) = (-9,5,6) -> (x, y, z) = (0,0,0) | (-7,11,12)
