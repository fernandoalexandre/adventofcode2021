from beacon import Beacon
from scanner import Scanner


def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()


def part1(list_eq: list) -> None:
    print("--- Part 1 Ship-it ---")
    part1 = 0

    print(f"Part 1: {part1}")


def part2(content: list) -> None:
    print("--- Part 2 Ship-it ---")

    part2 = 0

    print(f"Part 2: {part2}")


def parse(file_name: str) -> list[Beacon]:
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

    return scanner_list


def main():
    scanners = parse("day19/input_example")

    for s_1 in range(0, len(scanners)):
        src = scanners[s_1]
        for s_2 in range(s_1, len(scanners)):
            dst = scanners[s_2]
            if src.id == dst.id:
                continue

            print(f"Matching Scanner {src.id} with {dst.id}")
            for i in range(0, len(src.beacons)):
                for j in range(0, len(dst.beacons)):
                    likeliness = src.beacons[i].get_likeliness(dst.beacons[j])
                    if likeliness[1] > 0.0:
                        print(f"{src.beacons[i]} ~ {dst.beacons[j]} (likeliness={likeliness[1]}/{likeliness[2]})")

    print("-------------- Part 1 ------------------")

    part1(scanners)

    print("-------------- Part 2 ------------------")

    part2(scanners)


if __name__ == "__main__":
    main()
