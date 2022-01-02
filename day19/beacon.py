from __future__ import annotations

from trajectory import Trajectory


class Beacon():
    def __init__(self, pos: tuple) -> None:
        self.pos = pos
        self.trajectories = []

    def __repr__(self) -> str:
        return f"{self.pos}"

    def add_other_beacon(self, other_beacon: Beacon) -> None:
        if not isinstance(other_beacon, Beacon):
            return NotImplemented()

        self.trajectories.append(Trajectory(self.pos, other_beacon.pos))

    def get_likeliness(self, other_beacon: Beacon) -> tuple:
        if not isinstance(other_beacon, Beacon):
            return NotImplemented()

        total_eq = 0
        total = len(self.trajectories)

        if total == 0:
            return 0.0, total_eq, total

        for s_t in self.trajectories:
            for o_t in other_beacon.trajectories:
                if s_t.eq_dist(o_t):
                    total_eq += 1
                    print(f"{s_t} {s_t.get_direction_vectors()} ~ {o_t} {o_t.get_direction_vectors()}")

        # returns percentage, number, total
        return total_eq/total, total_eq, len(self.trajectories)
