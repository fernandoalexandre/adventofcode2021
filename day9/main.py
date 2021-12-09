def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()

def is_lowest(value: int, adj_values: list) -> bool:
    return value < min(adj_values)

def is_valid(i, j, n, m):
    return 0 <= i <= n and 0 <= j <= m

def get_adj_values(map: list, row: int, col: int) -> list:
    max_row = len(map)-1
    max_col = len(map[0])-1

    values = []

    if is_valid(row+1, col, max_row, max_col):
        values.append(map[row+1][col])
    if is_valid(row, col+1, max_row, max_col):
        values.append(map[row][col+1]) 
    if is_valid(row-1, col, max_row, max_col):
        values.append(map[row-1][col]) 
    if is_valid(row, col-1, max_row, max_col):
        values.append(map[row][col-1])
    
    return values

def find_basin(hmap: list, row: int, col: int, max_row: int, max_col: int, checked_positions: list) -> int:
    # returns the current size of basin and checked values
    total_basin = 1
    checked_positions.append([row, col])

    if is_valid(row+1, col, max_row, max_col):
        if hmap[row+1][col] != 9 and [row+1, col] not in checked_positions:
            basin_size, checked_positions = find_basin(hmap, row+1, col, max_row, max_col, checked_positions)
            total_basin += basin_size
    
    if is_valid(row, col+1, max_row, max_col):
        if hmap[row][col+1] != 9 and [row, col+1] not in checked_positions:
            basin_size, checked_positions = find_basin(hmap, row, col+1, max_row, max_col, checked_positions)
            total_basin += basin_size

    if is_valid(row-1, col, max_row, max_col):
        if hmap[row-1][col] != 9 and [row-1, col] not in checked_positions:
            basin_size, checked_positions = find_basin(hmap, row-1, col, max_row, max_col, checked_positions)
            total_basin += basin_size

    if is_valid(row, col-1, max_row, max_col):
        if hmap[row][col-1] != 9 and [row, col-1] not in checked_positions:
            basin_size, checked_positions = find_basin(hmap, row, col-1, max_row, max_col, checked_positions)
            total_basin += basin_size

    return total_basin, checked_positions

def main():
    content = read_file("day9/input")

    part1 = 0
    part2 = 1
    part2_lowest = []
    part2_basin_sizes = []

    hmap = []

    for line in content:
        hmap.append(list(map(int, list(line.rstrip("\n")))))

    for ridx in range(0, len(hmap)):
        for cidx in range(0, len(hmap[0])):
            current_slot = hmap[ridx][cidx]

            if is_lowest(current_slot, get_adj_values(hmap, ridx, cidx)):
                part1 += 1 + current_slot
                part2_lowest.append([ridx, cidx])
    
    # Part 2 find basins
    max_row = len(hmap)-1
    max_col = len(hmap[0])-1
    for lowest_pt in part2_lowest:
        checked_positions = []
        if lowest_pt not in checked_positions:
            basin_size, checked_positions = find_basin(hmap, lowest_pt[0], lowest_pt[1], max_row, max_col, checked_positions)
            part2_basin_sizes.append(basin_size)
    
    part2_basin_sizes = sorted(part2_basin_sizes)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2_basin_sizes[-1]*part2_basin_sizes[-2]*part2_basin_sizes[-3]}")



if __name__ == "__main__":
    main()