from copy import deepcopy
from dict_3d_map import dict_3d_map


def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()


def part1(inst_list: list, expected_result: int = None, should_print: bool = True) -> None:
    part1 = 0

    dmap = dict_3d_map()

    for i in inst_list:
        dmap.set_region(i["state"], i["x_region"], i["y_region"], i["z_region"], (-50, 50), (-50, 50), (-50, 50))

    part1 = dmap.get_state_count((-50, 50), (-50, 50), (-50, 50))

    print(f"Part 1: {part1}")
    if expected_result is not None:
        if expected_result == part1:
            print("Test passed!")
        else:
            print(f"Test failed! {expected_result} != {part1} (calculated)")


def part2(inst_list: list, expected_result: int = None, should_print: bool = True) -> None:
    part2 = 0

    dmap = dict_3d_map()

    count = 0
    for i in inst_list:
        print(f"[{count}/{len(inst_list)}] Setting region {i}")
        dmap.set_region_unbound(i["state"], i["x_region"], i["y_region"], i["z_region"])
        count += 1

    print("Counting on states")
    part2 = dmap.get_state_count()

    print(f"Part 2: {part2}")
    if expected_result is not None:
        if expected_result == part2:
            print("Test passed!")
        else:
            print(f"Test failed! {expected_result} != {part2} (calculated)")


def parse(content):
    list_inst = []
    min_x = float("inf")
    max_x = float("-inf")
    min_y = float("inf")
    max_y = float("-inf")
    min_z = float("inf")
    max_z = float("-inf")
    for i in range(0, len(content)):
        s = content[i].split(" ")
        s2 = s[1].split(",")
        s2_x = s2[0].split("..")
        s2_y = s2[1].split("..")
        s2_z = s2[2].split("..")
        min_x = min(min_x, int(s2_x[0][2:]))
        max_x = max(max_x, int(s2_x[1]))
        min_y = min(min_y, int(s2_y[0][2:]))
        max_y = max(max_y, int(s2_y[1]))
        min_z = min(min_z, int(s2_z[0][2:]))
        max_z = max(max_z, int(s2_z[1]))
        record = {
            "state": s[0],
            "x_region": (int(s2_x[0][2:]), int(s2_x[1])),
            "y_region": (int(s2_y[0][2:]), int(s2_y[1])),
            "z_region": (int(s2_z[0][2:]), int(s2_z[1]))
        }
        list_inst.append(record)

    print(f"X [{min_x}, {max_x}] Y [{min_y},{max_y}] Z [{min_z},{max_z}]")
    return list_inst


def main():
    content_example = parse(read_file("day22/input_example"))
    content_example_p2 = parse(read_file("day22/input_example_p2"))
    content = parse(read_file("day22/input"))

    print("-------------- Part 1 ------------------")
    part1(deepcopy(content_example), 39, should_print=True)
    part1(deepcopy(content), should_print=False)

    print("-------------- Part 2 ------------------")

    part2(deepcopy(content_example_p2), 2758514936282235, should_print=True)
    part2(deepcopy(content), should_print=False)


if __name__ == "__main__":
    main()
