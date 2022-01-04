from scanner import Scanner

from copy import copy

from operator import itemgetter


def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()


def parse(file_name: str) -> list[Scanner]:
    content = read_file(file_name)

    scanner_list = []
    scanner = None
    for line in content:
        line = line.rstrip("\n")
        if line == "":
            if scanner is not None:
                scanner_list.append(scanner)
        elif line.startswith("---"):
            scanner = Scanner(id=len(scanner_list))
        else:
            scanner.add_beacon(tuple(map(int, line.split(","))))
    scanner_list.append(scanner)

    return scanner_list


def main():
    scanners = parse("day19/input")

    source = scanners[0]

    scanners.remove(source)
    scanners.reverse()
    to_process = copy(scanners)

    print("-------------- Part 1 ------------------")

    while len(to_process) > 0:
        curr_scanner = to_process.pop()
        if not source.import_scanner(curr_scanner):
            print(f"Failed to import {source} with {curr_scanner}")
            # Avoid infinite loop for troubleshooting
            if len(to_process) > 0:
                to_process.insert(0, curr_scanner)
        else:
            print(f"Imported {source} with {curr_scanner}")

    print(f"Num Beacons: {len(source.beacons)}")

    for beacon in sorted([a.get_pos() for a in source.beacons], key=itemgetter(0, 1, 2)):
        print(f"{beacon}")

    for scanner in source.detected_scanners:
        print(f"Scanner {scanner}")

    print("-------------- Part 2 ------------------")

    # Used to not wait for re-processing...
    final_beacons = [
        (-1250, -3, 1250),
        (-1200, -59, 128),
        (1153, -188, 125),
        (-150, 4, 1292),
        (-1, 8, 2512),
        (1162, -148, 1277),
        (-1328, -124, -1155),
        (1081, 1192, 2368),
        (1231, -84, 2356),
        (1153, -1309, 2500),
        (1169, -1293, 1321),
        (24, -2428, -32),
        (-16, -51, -1141),
        (-152, 1133, 1178),
        (2313, -1342, 1280),
        (3599, -2502, 1336),
        (-1236, -2499, 1249),
        (-123, -1208, 1270),
        (-1240, -2442, 2467),
        (14, -1321, 2436),
        (2314, -2564, 1273),
        (26, -1207, 140),
        (1163, -123, 3669),
        (1054, -1224, 3645),
        (1034, -2418, 1317),
        (-29, -2478, 1235),
        (1222, -2393, 61),
        (1215, -29, 4902),
        (1223, -184, 6096)
    ]

    max_distance = 0.0
    for i in range(0, len(source.detected_scanners)):
        for j in range(i, len(source.detected_scanners)):
            dist = sum(abs(e1-e2) for e1, e2 in zip(source.detected_scanners[i], source.detected_scanners[j]))

            max_distance = dist if dist > max_distance else max_distance

    print(f"Part 2: max_distance = {max_distance}")


if __name__ == "__main__":
    main()
