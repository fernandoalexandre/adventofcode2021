boards = []

input = [30,35,8,2,39,37,72,7,81,41,25,46,56,18,89,70,0,15,84,75,88,67,42,44,94,71,79,65,58,52,96,83,54,29,14,95,66,61,97,68,57,90,55,32,17,47,20,98,1,69,63,62,31,86,77,85,87,93,26,40,24,19,48,76,73,49,34,45,82,22,80,78,23,6,59,91,64,43,21,51,13,3,53,99,4,28,33,74,12,9,36,50,60,11,27,10,5,16,92,38]

def read_file(path):
    with open(path) as fp:
        content = fp.readlines()
        board = []
        i = 0
        for row in content:
            row = row.rstrip("\n")
            if row != "":
                #print(f"'{row}'")
                board.append([{"val": int(x), "mark": False} for x in row.split(" ")])
            else:
                boards.append({"won": False, "board": board})
                board = []
            i += 1
        fp.readline()

def count_score(idx, draw):
    result = 0
    for row in range(0, 5):
        for col in range(0, 5):
            if not boards[idx]["board"][row][col]["mark"]:
                result += boards[idx]["board"][row][col]["val"]
    result *= draw

    print(f"Win Score: {result}")

def check_win(idx: int, draw: int):
    #row win
    for i in range(0, 5):
        has_row_win = True
        has_col_win = True
        for j in range(0, 5):
            has_row_win = has_row_win and boards[idx]["board"][i][j]["mark"]
            has_col_win = has_col_win and boards[idx]["board"][j][i]["mark"]
        
        if has_row_win or has_col_win:
            boards[idx]["won"] = True
            count_score(idx, draw)

    
def main():
    read_file("day4/input")

    print(f"Found {len(boards)} boards!")

    # run the shizz
    for draw in input:
        for idx in range(0, len(boards)):
            if not boards[idx]["won"]:
                for row in range(0, 5):
                    for col in range(0, 5):
                        boards[idx]["board"][row][col] = {"val": boards[idx]["board"][row][col]["val"], "mark": boards[idx]["board"][row][col]["mark"] or boards[idx]["board"][row][col]["val"] == draw}
                check_win(idx, draw)

    print("Finished")

if __name__ == "__main__":
    main()