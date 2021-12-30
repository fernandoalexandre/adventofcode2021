# TODO

def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()


def part1(list_eq: list) -> None:
    print("--- Part 1 Ship-it ---")


    print(f"Part 1: {0}")


def part2(content: list) -> None:
    print("--- Part 2 Ship-it ---")

    part2 = 0

    print(f"Part 2: {part2}")


def main():
    content = read_file("day18/input")


    print("-------------- Part 1 ------------------")

    part1(list_eq)

    print("-------------- Part 2 ------------------")

    part2(content)


if __name__ == "__main__":
    main()
