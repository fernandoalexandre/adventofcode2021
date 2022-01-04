from __future__ import annotations

from copy import deepcopy

from beacon import Beacon


class Scanner():
    def __init__(self, id: int) -> None:
        self.id = id
        self.pos = (0, 0, 0)
        self.beacons: list[Beacon] = []
        self.detected_scanners: list[tuple] = []

    def __repr__(self) -> str:
        return f"S({self.id})"

    def add_beacon(self, point: tuple) -> None:
        new_beacon = Beacon(point)
        for b in self.beacons:
            b.add_other_beacon(new_beacon)
            new_beacon.add_other_beacon(b)
        self.beacons.append(new_beacon)

    def translate_scanner(self, coefficient: tuple) -> None:
        self.pos = (
            self.pos[0]+coefficient[0],
            self.pos[1]+coefficient[1],
            self.pos[2]+coefficient[2],
        )

    def import_scanner(self, o_scanner: Scanner) -> bool:
        for i in range(0, len(self.beacons)):
            for j in range(0, len(o_scanner.beacons)):
                likeliness = self.beacons[i].get_likeliness(deepcopy(o_scanner.beacons[j]))
                if likeliness['match'] > 1:
                    # print(f"Found coefficient: {likeliness['coefficient']} ({likeliness['match']}/{likeliness['total']})")

                    self._add_detected_scanner(o_scanner, likeliness)
                    return True
        return False

    def _add_detected_scanner(self, o_scanner: Scanner, likeliness: tuple) -> None:
        self.detected_scanners.append((
            o_scanner.pos[0] + likeliness['coefficient'][0],
            o_scanner.pos[1] + likeliness['coefficient'][1],
            o_scanner.pos[2] + likeliness['coefficient'][2],
        ))

        for beacon in o_scanner.beacons:
            new_beacon = deepcopy(beacon)
            new_beacon.swap_coordinates(likeliness['swap'])
            new_beacon.multiply_coordinates(likeliness['reflection'])
            new_beacon.add_coordinates(likeliness['coefficient'])
            if new_beacon not in self.beacons:
                print(f"Adding beacon {new_beacon.pos}")
                self.add_beacon(new_beacon.pos)
            else:
                print(f"Already found beacon {new_beacon}, ignoring...")
