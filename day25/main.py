from operator import itemgetter

def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()

def print_map(right, bot, max_row, max_col):
    smap = [['.' for _ in range(0, max_col)] for _ in range(0, max_row)]

    for sea_cocumber in list(right):
        smap[sea_cocumber[0]][sea_cocumber[1]] = '>'
    
    for sea_cocumber in list(bot):
        smap[sea_cocumber[0]][sea_cocumber[1]] = 'v'
    
    for line in smap:
        print(*line, sep='')
    
    print("------------------")

def get_next_position(sea_cocumber: tuple, direction: str, max_row: int, max_col: int) -> tuple:
    if direction == ">":
        return (sea_cocumber[0], (sea_cocumber[1]+1) % max_col)
    elif direction == "v":
        return ((sea_cocumber[0]+1) % max_row, sea_cocumber[1])
    raise NotImplementedError(f"Invalid direction {direction}")

def simulate_step(right: set, bot: set, max_row: int, max_col: int, should_print: bool = True):
    has_changed = False

    sorted_right = sorted(right, key=itemgetter(0,1))
    sorted_bot = sorted(bot, key=itemgetter(0,1))

    new_right = set()
    new_bot = set()
    
    for sea_cocumber in sorted_right:
        new_sea_cocumber = get_next_position(sea_cocumber, '>', max_row, max_col)

        if new_sea_cocumber not in right and new_sea_cocumber not in bot:
            new_right.add(new_sea_cocumber)
            has_changed = True
        else:
            new_right.add(sea_cocumber)
    
    for sea_cocumber in sorted_bot:
        new_sea_cocumber = get_next_position(sea_cocumber, 'v', max_row, max_col)

        if new_sea_cocumber not in new_right and new_sea_cocumber not in bot:
            new_bot.add(new_sea_cocumber)
            has_changed = True
        else:
            new_bot.add(sea_cocumber)

    return has_changed, new_right, new_bot

def part1(right: set, bot: set, max_row: int, max_col: int, should_print: bool = True) -> None:
    part1 = 0

    if should_print:
            print_map(right, bot, max_row, max_col)

    changed = True
    while changed:
        changed, right, bot = simulate_step(right, bot, max_row, max_col, should_print)
        part1 += 1
        if should_print:
            print_map(right, bot, max_row, max_col)
    print(f"Part 1: {part1}")



def part2(inst_list: list, num_inputs: int, should_print: bool = True) -> None:
    part2 = 0

    print(f"Part 2: {part2}")


def parse(content):
    right = set()
    bot = set()
    max_row = len(content)
    max_col = len(content[0]) - 1  # remove \n

    for i in range(0, max_row):
        for j in range(0, max_col):
            line = content[i].rstrip('\n')
            if line[j] == "v":
                bot.add((i,j))
            elif line[j] == ">":
                right.add((i,j))

    return right, bot, max_row, max_col


def main():
    print("-------------- Part 1 ------------------")
    right, bot, max_row, max_col = parse(read_file("day25/input_example"))

    part1(right, bot, max_row, max_col, should_print=True)

    right, bot, max_row, max_col = parse(read_file("day25/input"))

    part1(right, bot, max_row, max_col, should_print=False)

    print("-------------- Part 2 ------------------")

    # part2(deepcopy(input_example), 444356092776315, should_print=True)

    # part2(deepcopy(input), should_print=False)


if __name__ == "__main__":
    main()
