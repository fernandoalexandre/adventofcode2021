
def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()

def find_sheet_size(content: list):
    max_row = 0
    max_col = 0
    for line in content:
        line = line.rstrip("\n")
        
        if line == "":
            return max_row, max_col
        
        col, row = list(map(int, line.split(",")))

        max_row = row if row > max_row else max_row
        max_col = col if col > max_col else max_col

        

def fold(sheet, axis, value):
    result_sheet = []
    # Smallest sheet after a fold
    foldee = []
    if axis == "y":
        result_sheet = sheet[:value]
        foldee = sheet[value+1:]

        for i in range(0, len(foldee)):
            for j in range(0, len(foldee[i])):
                if foldee[i][j] == "#":
                    result_sheet[-(i+1)][j] = "#"
    elif axis == "x":
        foldee = []

        for line in sheet:
            result_sheet.append(line[:value])
            foldee.append(line[value+1:])

        for i in range(0, len(foldee)):
            for j in range(0, len(foldee[i])):
                if foldee[i][j] == "#":
                    result_sheet[i][-(j+1)] = "#"

    else:
        return None

    return result_sheet

def main():
    content = read_file("day13/input")

    max_row, max_col = find_sheet_size(content)
    sheet = []
    fold_list = []

    for i in range(0, max_row+1):
        sheet.append([" "] * (max_col+1))

    for line in content:
        line = line.rstrip("\n")
        if line.startswith("fold"):
            fold_list.append(line.lstrip("fold along ").split("="))
        elif line == "":
            continue
        else:
            col, row = list(map(int, line.split(",")))
            sheet[row][col] = "#"

    print("-------------- Part 1 ------------------")
    folded_sheet = fold(sheet, fold_list[0][0], int(fold_list[0][1]))

    part1 = 0
    for line in folded_sheet:
        for col in line:
            if col == "#":
                part1 +=1

    print(f"Part 1: {part1}")


    print("-------------- Part 2 ------------------")
    folded_sheet =  sheet
    for fold_entry in fold_list:
        folded_sheet = fold(folded_sheet, fold_entry[0], int(fold_entry[1]))

    for line in folded_sheet:
        print(*line, sep="")
    





if __name__ == "__main__":
    main()