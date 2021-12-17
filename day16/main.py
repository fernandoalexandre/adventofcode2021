
def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()

def is_valid(i, j, n, m):
    return 0 <= i <= n and 0 <= j <= m

def part1(packets):
    part1 = 0


    print("--- Part 1 Ship-it ---")
    for packet in packets:
        part1, _ = parse_packet_p1(packet)
        print(f"Part 1: {part1}")

    return part1

def part2(packets):
    part2 = 0

    print("--- Part 1 Ship-it ---")
    for packet in packets:
        part2, _ = parse_packet_p2(packet)
        print(f"Part 2: {part2}")

    return part2

def main():
    content = read_file("day17/input_example")

    packets = []
    for line in content:
        packets.append(bin(int('1'+line.rstrip("\n"), 16))[3:])

    print("-------------- Part 1 ------------------")

    p1 = part1(packets)

    print("-------------- Part 2 ------------------")

    p2 = part2(packets)

if __name__ == "__main__":
    main()