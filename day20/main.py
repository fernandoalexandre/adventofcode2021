def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()


def is_valid(i, j, n, m):
    return 0 <= i <= n and 0 <= j <= m

def get_adj_values(map: list, row: int, col: int, padding: str) -> str:
    max_row = len(map)-1
    max_col = len(map[0])-1

    values = ''

    slots = [
        [row-1, col-1], # tl
        [row-1, col],   # tm
        [row-1, col+1], # tr
        [row, col-1],   # ml
        [row, col],     # mm
        [row, col+1],   # mr
        [row+1, col-1], # bl
        [row+1, col],   # bm
        [row+1, col+1]  # br
    ]

    for i in range(0, len(slots)):
        if is_valid(slots[i][0], slots[i][1], max_row, max_col):
            values += map[slots[i][0]][slots[i][1]]
        else:
            values += padding

    return str(values)


def part1(lmap: list, algo: str) -> None:
    print("--- Part 1 Ship-it ---")

    new_map = []

    for it in range(0, 2):
        padding = '0' if it % 2 == 0 else '1'
        part1 = 0
        for k in range(0, len(lmap)):
            lmap[k].insert(0, padding)
            lmap[k].append(padding)
        lmap.insert(0, [padding for _ in range(0, len(lmap[0]))])
        lmap.append([padding for _ in range(0, len(lmap[0]))])
        for i in range(0, len(lmap)):
            new_map.append([])
            for j in range(0, len(lmap[0])):
                idx = int(get_adj_values(lmap, i, j, padding), 2)
                val = algo[idx]

                part1 += 1 if val == '1' else 0

                new_map[i].append(val)

        for i in range(0, len(new_map)):
            print(*new_map[i], sep="")
        print("-------")

        lmap = new_map
        new_map = []

    print(f"Part 1: {part1}")


def part2(content: list) -> None:
    print("--- Part 2 Ship-it ---")

    part2 = 0

    print(f"Part 2: {part2}")


def main():
    content = read_file("day20/input_example")

    algo = content[0].rstrip('\n').replace("#", '1').replace(".", '0')

    lmap = []

    for i in range(2, len(content)):
        lmap.append(list(content[i].rstrip('\n').replace("#", '1').replace(".", '0')))

    print("-------------- Part 1 ------------------")

    part1(lmap, algo)

    print("-------------- Part 2 ------------------")

    part2(content)

if __name__ == "__main__":
    main()
