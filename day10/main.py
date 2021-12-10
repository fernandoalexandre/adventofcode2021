import math

def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()

part1_invalid = {}

match_table = {
    "(":")",
    "[":"]",
    "{":"}",
    "<":">",
}

def main():
    content = read_file("day10/input")

    part_1_scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    part_2_scores = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    part_2_line_scores = []

    part1 = 0
    part2 = 1

    for line in content:
        line = line.rstrip("\n")

        parsing = []

        # Part 1
        for char in list(line): 
            print(parsing)
            if char in match_table.keys():
                parsing.append(char)
            elif char in match_table.values():
                expected_close = match_table[parsing.pop()]
                if expected_close == char:
                    continue
                else:
                    print(f"Found invalid char!")
                    if char not in part1_invalid:
                        part1_invalid[char] = 1
                    else:
                        part1_invalid[char] += 1
                    break

        # Part 2
        parsing = []
        for char in list(line): 
            if char in match_table.keys():
                parsing.append(char)
            elif char in match_table.values():
                expected_close = match_table[parsing.pop()]
                if expected_close == char:
                    continue
                else:
                    parsing = []
                    break
        
        
        if len(parsing) > 0:
            current_score = 0
            parsing.reverse()
            for char in parsing:
                expected_close = match_table[char]
                
                current_score = current_score*5 + part_2_scores[expected_close]
        
            part_2_line_scores.append(current_score)

    # Part1 Scores
    for invalid_key in part1_invalid.keys():
        part1 += part1_invalid[invalid_key] * part_1_scores[invalid_key]

    # Part2 Scores
    p2_scores = sorted(part_2_line_scores)
    part2 = p2_scores[math.floor(len(part_2_line_scores)/2)]

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")



if __name__ == "__main__":
    main()