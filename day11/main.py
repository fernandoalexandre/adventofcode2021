
def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()

def is_valid(i, j, n, m):
    return 0 <= i <= n and 0 <= j <= m

def flash(map: list, row: int, col: int, already_flashed: list) -> list:
    max_row = len(map)-1
    max_col = len(map[0])-1

    more_to_flash = []

    slots = [
        [row+1, col],
        [row, col+1],
        [row-1, col],
        [row, col-1],
        [row+1,col-1],
        [row-1, col-1],
        [row-1, col+1],
        [row+1, col+1]
    ]

    for slot in slots:
        if is_valid(slot[0], slot[1], max_row, max_col): # right
            if slot not in already_flashed:
                map[slot[0]][slot[1]] += 1

                if map[slot[0]][slot[1]] >= 10:
                    more_to_flash.append(slot)
                
    
    return more_to_flash

def main():
    content = read_file("day11/input")

    part1 = 0
    part2 = 1
    octo_map = []

    for line in content:
        octo_map.append(list(map(int, list(line.rstrip("\n")))))

    max_row = len(octo_map)
    max_col = len(octo_map[0])
    already_flashed = []
    for step in range(0,99999999999):
        print(f"Step {step}")
        num_flash = 0
        for i in range(0, max_row):
            for j in range(0, max_col):
                if [i, j] not in already_flashed:
                    octo_map[i][j] += 1
                    if octo_map[i][j] >= 10:
                        print(f"flashing [{i},{j}]")
                        octo_map[i][j] = 0
                        already_flashed.append([i, j])
                        num_flash += 1

                        more_to_flash = flash(octo_map, i, j, already_flashed)
                        part1 += 1

                        while len(more_to_flash) != 0:
                            row, col = more_to_flash.pop()
                            octo_map[row][col] = 0
                            print(f"sub-flashing [{row},{col}]")
                            already_flashed.append([row, col])
                            num_flash += 1
                            flash_list = flash(octo_map, row, col, already_flashed)

                            part1 += 1
                            
                            for element in flash_list:
                                if element not in already_flashed and element not in more_to_flash:
                                    more_to_flash.insert(0, element)
        if num_flash == 100:
            part2 = step+1
            break
        num_flash = 0
        already_flashed = []
        for s in octo_map:
            print(*s)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")



if __name__ == "__main__":
    main()