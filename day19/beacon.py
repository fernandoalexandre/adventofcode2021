from __future__ import annotations

from numpy import matmul, array

from trajectory import Trajectory


class Beacon():
    def __init__(self, pos: tuple) -> None:
        self.pos: tuple = pos
        self.trajectories: list[Trajectory] = []

    def __repr__(self) -> str:
        return f"{self.pos}"

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Beacon):
            return NotImplemented()

        return self.pos == __o.pos

    def get_pos(self) -> tuple:
        return self.pos

    def add_other_beacon(self, other_beacon: Beacon) -> None:
        if not isinstance(other_beacon, Beacon):
            return NotImplemented()

        self.trajectories.append(Trajectory(self.pos, other_beacon.pos))

    def swap_coordinates(self, swap_idx: tuple) -> None:
        # Update all trajectories
        for trajectory in self.trajectories:
            trajectory.swap_coordinates(swap_idx)

        # Update this beacon's position
        new_pos = [self.pos[swap_idx[0]], self.pos[swap_idx[1]], self.pos[swap_idx[2]]]
        self.pos = tuple(new_pos)

    # Probably not needed
    def multiply_coordinates(self, coeficient: tuple) -> None:
        self.pos = (
            self.pos[0]*coeficient[0],
            self.pos[1]*coeficient[1],
            self.pos[2]*coeficient[2],
        )

        for trajectory in self.trajectories:
            trajectory.multiply_coordinates(coeficient)

    # Probably not needed
    def add_coordinates(self, coeficient: tuple) -> Beacon:
        self.pos = (
            self.pos[0]+coeficient[0],
            self.pos[1]+coeficient[1],
            self.pos[2]+coeficient[2],
        )

        for trajectory in self.trajectories:
            trajectory.add_coordinates(coeficient)

    def _find_swap(self, s_t: Trajectory, o_t: Trajectory) -> tuple:
        s_d = s_t.get_direction_vectors()[0]
        o_d = o_t.get_direction_vectors()[0]

        x, y, z = (abs(s_d[0]), abs(s_d[1]), abs(s_d[2]))
        o_x, o_y, o_z = (abs(o_d[0]), abs(o_d[1]), abs(o_d[2]))

        if x == o_x and y == o_y and z == o_z:
            return (0, 1, 2)
        elif x == o_z and y == o_y and z == o_x:
            return(2, 1, 0)
        elif x == o_x and y == o_z and z == o_y:
            return (0, 2, 1)
        elif x == o_y and y == o_z and z == o_x:
            return (1, 2, 0)
        elif x == o_z and y == o_x and z == o_y:
            return (2, 0, 1)
        elif x == o_y and y == o_x and z == o_z:
            return (1, 0, 2)

        return (0, 1, 2)

    def _find_reflection(self, s_t: Trajectory, o_t: Trajectory) -> tuple:
        s_d = s_t.get_direction_vectors()[0]
        o_d = o_t.get_direction_vectors()[0]

        f = 1
        if (s_d[0] > 0 and o_d[0] < 0) or (s_d[0] < 0 and o_d[0] > 0):
            f = -1
        s = 1
        if (s_d[1] > 0 and o_d[1] < 0) or (s_d[1] < 0 and o_d[1] > 0):
            s = -1
        t = 1
        if (s_d[2] > 0 and o_d[2] < 0) or (s_d[2] < 0 and o_d[2] > 0):
            t = -1

        return (f, s, t)

    def _get_coefficient(self, other: tuple, reflection: tuple) -> tuple:
        x = y = z = 0

        if self.pos[0] >= 0 and other[0] >= 0:
            x = self.pos[0] - other[0]
        elif self.pos[0] >= 0 and other[0] < 0:
            x = abs(self.pos[0]) + abs(other[0])
        elif self.pos[0] < 0 and other[0] >= 0:
            x = -(abs(self.pos[0]) + abs(other[0]))
        else:  # Both negative
            x = -(abs(self.pos[0]) - abs(other[0]))

        if self.pos[1] >= 0 and other[1] >= 0:
            y = self.pos[1] - other[1]
        elif self.pos[1] >= 0 and other[1] < 0:
            y = abs(self.pos[1]) + abs(other[1])
        elif self.pos[1] < 0 and other[1] >= 0:
            y = -(abs(self.pos[1]) + abs(other[1]))
        else:  # Both negative
            y = -(abs(self.pos[1]) - abs(other[1]))

        if self.pos[2] >= 0 and other[2] >= 0:
            z = self.pos[2] - other[2]
        elif self.pos[2] >= 0 and other[2] < 0:
            z = abs(self.pos[2]) + abs(other[2])
        elif self.pos[2] < 0 and other[2] >= 0:
            z = -(abs(self.pos[2]) + abs(other[2]))
        else:  # Both negative
            z = -(abs(self.pos[2]) - abs(other[2]))

        return (x, y, z)

    def get_likeliness(self, other_beacon: Beacon) -> dict:
        if not isinstance(other_beacon, Beacon):
            return NotImplemented()

        total_eq = 0
        total = len(self.trajectories)
        reflection = None
        swap = None
        coefficient = None

        if total == 0:
            return {
                "match_pct": 0.0,
                "match": total_eq,
                "total": len(self.trajectories),
                "reflection": reflection,
                "swap": swap,
            }

        for s_t in self.trajectories:
            for o_t in other_beacon.trajectories:
                if s_t.eq_dist(o_t):
                    total_eq += 1
                    swap = self._find_swap(s_t, o_t)
                    # print(f"Before: {s_t} {s_t.get_direction_vectors()} ~ {o_t} {o_t.get_direction_vectors()}")
                    # print(f"Before: Transformation: {swap}")
                    o_t.swap_coordinates(swap)
                    reflection = self._find_reflection(s_t, o_t)
                    # print(f"Before: Reflection: {reflection}")
                    o_t.multiply_coordinates(reflection)
                    # print(f"After: {s_t} {s_t.get_direction_vectors()} ~ {o_t} {o_t.get_direction_vectors()}")

        if total_eq > 1:
            other_beacon.swap_coordinates(swap)
            other_beacon.multiply_coordinates(reflection)
            coefficient = self._get_coefficient(other_beacon.pos, reflection)

        # returns percentage, number, total
        return {
            "match_pct": total_eq/total,
            "match": total_eq,
            "total": len(self.trajectories),
            "reflection": reflection,
            "swap": swap,
            "coefficient": coefficient
        }
