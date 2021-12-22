from copy import deepcopy
import itertools
from functools import cache


def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()


def dice_roll(prev, min=1, max=101) -> int:
    prev += 1
    return min + (prev - min) % (max - min)


def dice_rolls(prev: int, num_rolls: int) -> tuple:
    curr = 0
    for _ in range(0, num_rolls):
        prev = dice_roll(prev)
        curr += prev
    return curr, prev


@cache
def get_position(pos, steps, min=1, max=11):
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


possibilities = {
    # didn't get to use this, but could be further optimized
    3: 1,  # 1, 1, 1
    4: 3,  # 1, 1, 2 | 1, 2, 1 | 2, 1 ,1
    5: 6,  # 3, 1, 1*3 | 2, 2, 1*3
    6: 7,  # 3, 2, 1 | 3, 1, 2 | 1, 3, 2 | 1, 2, 3 | 2, 1, 3 | 2, 3, 1 | 2, 2, 2
    7: 6,  # 3, 3, 1*3 | 3, 2, 2*3
    8: 3,  # 3, 3, 2 | 3, 2, 3 | 2, 3, 3
    9: 1,  # 3, 3, 3
}


def part2(player: list, expected_result: int = None, should_print: bool = True) -> None:
    part2 = 0

    part2 = max(recursive_sweep(player[0], player[1], 0, 0, True))

    print(f"Part 2: {part2}")
    if expected_result is not None:
        if expected_result == part2:
            print("Test passed!")
        else:
            print(f"Test failed! {expected_result} != {part2} (calculated)")


throws = [sum(x) for x in itertools.product([1, 2, 3], repeat=3)]


@cache
def recursive_sweep(p1_pos, p2_pos, p1_score, p2_score, is_p1):
    # Heavily inspired on a comment on reddit...
    if p1_score >= 21:
        return 1, 0
    if p2_score >= 21:
        return 0, 1
    curr_pos = p1_pos if is_p1 else p2_pos
    possible_positions = [get_position(curr_pos, j) for j in throws]
    if is_p1:
        child_universes = (recursive_sweep(position, p2_pos, p1_score+position, p2_score, False) for position in possible_positions)
    else:
        child_universes = (recursive_sweep(p1_pos, position, p1_score, p2_score+position, True) for position in possible_positions)
    return sum(p1 for p1, _ in child_universes), sum(p2 for _, p2 in child_universes)


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

    part2(deepcopy(input), should_print=False)

if __name__ == "__main__":
    main()
