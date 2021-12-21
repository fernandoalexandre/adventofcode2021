from copy import deepcopy

def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()


def dice_roll(prev, min = 1, max = 101) -> int:
    prev += 1
    return min + (prev - min) % (max - min)

def dice_rolls(prev: int, num_rolls: int) -> tuple:
    curr = 0
    for _ in range(0, num_rolls):
        prev = dice_roll(prev)
        curr += prev
    return curr, prev

def get_position(pos, steps, min = 1, max = 11):
    val = (pos + steps)
    return min + (val - min) % (max - min)

def part1(player: list, expected_result: int = None, should_print: bool = True) -> None:
    part1 = 0

    score = [0,0]

    dice = 0
    total_rolls = 0
    for i in range(0, 999):
        if should_print:
            print(f"Turn {i}")
            print(f"Dice {dice} {dice+1} {dice+2}")
        steps, dice = dice_rolls(dice, 3)
        player[0] = get_position(player[0], steps)
        score[0] += player[0]
        total_rolls += 3
        if score[0] >= 1000:
            part1 = score[1]*total_rolls
            break

        if should_print:
            print(f"Player 1: {player[0]} | P1 score: {score[0]}")
            print(f"Dice {dice} {dice+1} {dice+2}")

        steps, dice = dice_rolls(dice, 3)
        player[1] = get_position(player[1], steps)
        score[1] += player[1]
        total_rolls += 3
        if score[1] >= 1000:
            part1 = score[0]*total_rolls
            break

        if should_print:
            print(f"Player 2: {player[1]} | P2 score: {score[1]}")

    if should_print:
        print(f"P1 score: {score[0]} | P2 score: {score[1]}")
        print(f"Dice: {dice}")

    print(f"Part 1: {part1}")
    if expected_result is not None:
        if expected_result == part1:
            print("Test passed!")
        else:
            print(f"Test failed! {expected_result} != {part1} (calculated)")

def part2(player: list, expected_result: int = None, should_print: bool = True) -> None:
    part2 = 0

    universes = []

    for p in player:
        pos = p
        score = 0

        total_rolls = 1
        for i in range(0, 999):
            if should_print:
                print(f"Turn {i}")

            
            pos = max(
                get_position(pos, 3),
                get_position(pos, 4),
                get_position(pos, 5),
                get_position(pos, 6),
                get_position(pos, 7),
                get_position(pos, 8),
                get_position(pos, 9),
            )

            score += pos

            print(f"max(pos) = {pos}")
            print(f"score = {score}")

            
            if i == 0:
                total_rolls = 18
            else:
                total_rolls **= 3

            if score >= 21:
                universes.append(total_rolls)
                break

        if should_print:
            print(*universes)

    part2 = max(universes)

    print(f"Part 2: {part2}")
    if expected_result is not None:
        if expected_result == part2:
            print("Test passed!")
        else:
            print(f"Test failed! {expected_result} != {part2} (calculated)")


def parse(content):
    algo = content[0].rstrip('\n').replace("#", '1').replace(".", '0')

    lmap = []

    for i in range(2, len(content)):
        lmap.append(list(content[i].rstrip('\n').replace("#", '1').replace(".", '0')))
    
    return algo, lmap

input = [8, 10]
input_example = [4, 8]

def main():
    print("-------------- Part 1 ------------------")
    part1(deepcopy(input_example), 739785, should_print=True)
    part1(deepcopy(input), should_print=False)

    print("-------------- Part 2 ------------------")

    part2(deepcopy(input_example), 444356092776315, should_print=True)

    #part2(input_example, should_print=False)

if __name__ == "__main__":
    main()
