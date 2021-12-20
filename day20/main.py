def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()

def print_map(lmap: list, iteration: int, should_print: bool) -> None:
    if should_print:
        print(f"---- Iteration {iteration} ----")
        for i in range(0, len(lmap)):
            print(*lmap[i], sep="")

def is_valid(i, j, n, m):
    return 0 <= i <= n and 0 <= j <= m

def get_adj_values(map: list, row: int, col: int, padding: str) -> tuple:
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


def part1(lmap: list, algo: str, num_it: int, expected_result: int = None, should_print: bool = True) -> None:
    new_map = []

    for it in range(0, num_it):
        part1 = 0

        if algo[0] == '1':
            padding = '0' if it % 2 == 0 else '1'
        else:
            padding = '0'
        
        # Add padding
        for k in range(0, len(lmap)):
            lmap[k].insert(0, padding)
            lmap[k].append(padding)
        lmap.insert(0, [padding for _ in range(0, len(lmap[0]))])
        lmap.append([padding for _ in range(0, len(lmap[0]))])
        
        print_map(lmap, it, should_print)
        # Process
        for i in range(0, len(lmap)):
            new_map.append([])
            for j in range(0, len(lmap[0])):
                bin_val = get_adj_values(lmap, i, j, padding)
                idx = int(bin_val, 2)
                val = algo[idx]

                new_map[i].append(val)

        lmap = new_map
        new_map = []

        print_map(lmap, it, should_print)

    for i in range(0, len(lmap)):
        for j in range(0, len(lmap[0])):
            if lmap[i][j] == '1':
                part1 += 1

    print(f"Part 1: {part1}")
    if expected_result is not None:
        if expected_result == part1:
            print("Test passed!")
        else:
            print(f"Test failed! {expected_result} != {part1} (calculated)")


def parse(content):
    algo = content[0].rstrip('\n').replace("#", '1').replace(".", '0')

    lmap = []

    for i in range(2, len(content)):
        lmap.append(list(content[i].rstrip('\n').replace("#", '1').replace(".", '0')))
    
    return algo, lmap

def main():
    ex_content = read_file("day20/input_example")
    content = read_file("day20/input")


    print("-------------- Part 1 ------------------")
    algo, lmap = parse(ex_content)
    part1(lmap, algo, 2, 35, should_print=False)

    algo, lmap = parse(content)
    part1(lmap, algo, 2, should_print=False)

    print("-------------- Part 2 ------------------")

    algo, lmap = parse(ex_content)
    part1(lmap, algo, 50, 3351, should_print=False)

    algo, lmap = parse(content)
    part1(lmap, algo, 50, should_print=False)

if __name__ == "__main__":
    main()
