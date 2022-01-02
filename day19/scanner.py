from beacon import Beacon


class Scanner():
    def __init__(self, id: int) -> None:
        self.id = id
        self.beacons: list[Beacon] = []

    def add_beacon(self, point: tuple) -> None:
        new_beacon = Beacon(point)
        for b in self.beacons:
            b.add_other_beacon(new_beacon)
        self.beacons.append(new_beacon)
