class Scanner():
    def __init__(self, id: int) -> None:
        self.id = id
        self.beacons = []
        self.distances = {}

    def add_beacon(self, point: tuple) -> None:
        self.beacons.append(point)

    def calculate_distances(self) -> None:
        # Distance3d  d = ((x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2)^1/2
        for i in range(0, len(self.beacons)):
            for j in range(i+1, len(self.beacons)):
                x1, y1, z1 = self.beacons[i]
                x2, y2, z2 = self.beacons[j]
                d = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
                key = (self.beacons[i], self.beacons[j])
                self.distances[key] = d
