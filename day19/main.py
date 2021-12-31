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


def parse(file_name: str) -> list:
    content = read_file(file_name)
    
    scanner_list = []
    scanner = None
    for line in content:
        line = line.rstrip("\n")
        if line == "":
            if scanner is not None:
                scanner_list.append(scanner)
        elif line.startswith("---"):
            if scanner is not None:
                scanner.calculate_distances()
            scanner = Scanner(id=len(scanner_list))
        else:
            scanner.add_beacon(tuple(map(int, line.split(","))))
    
    return scanner_list

def main():
    scanners = parse("day19/input_example")
    
    source = scanners[0]

    beacons = [[]]
    
    for scanner in scanners[1:]:
        print(f"Matching Scanner {source.id} with {scanner.id}")
        # key = scanner_id; Value: {source.beacon: set(other_matches)}
        matches = {}
        for i in range(0, len(source.beacons)):
            for j in range(i+1, len(source.beacons)):
                for k in range(0, len(scanner.beacons)):
                    for l in range(k+1, len(scanner.beacons)):
                        if source.distances[i][j] == scanner.distances[k][l] and source.distances[i][j] != 0.0:
                            s_x1, s_y1, s_z1 = scanner.beacons[i]
                            s_x2, s_y2, s_z2 = scanner.beacons[j]
                            dir_vector_source = (s_x2 - s_x1, s_y2 - s_y1, s_z2 - s_z1)
                            m_x1, m_y1, m_z1 = scanner.beacons[k]
                            m_x2, m_y2, m_z2 = scanner.beacons[l]
                            dir_vector_match = (m_x2 - m_x1, m_y2 - m_y1, m_z2 - m_z1)
                            print(f"Match ({source.beacons[i]}) -> ({source.beacons[j]}) with ({scanner.beacons[k]}) -> ({scanner.beacons[l]}) (d={source.distances[i][j]} | s_vect = {dir_vector_source} d_vect = {dir_vector_match})")
                            key = (source.beacons[i],source.beacons[j])
                            new_match = (scanner.beacons[k], scanner.beacons[l])
                            new_match_alt = (scanner.beacons[k], scanner.beacons[l])
                            #if key not in matches:




    print("-------------- Part 1 ------------------")

    part1(scanners)

    print("-------------- Part 2 ------------------")

    part2(scanners)


if __name__ == "__main__":
    main()
