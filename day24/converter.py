from math import floor
from multiprocessing import Pool


def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()


def _inp(input: list, registers: dict, params: list) -> tuple:
    print(f"registers['{params[0]}'] := input[0]")
    print("input = input[1:]")
    return registers, input[1:]


def _add(input: list, registers: dict, params: list) -> tuple:
    print(f"{params[0]} := {params[0]} + {params[1]}")
    return registers, input


def _mul(input: list, registers: dict, params: list) -> tuple:
    print(f"{params[0]} := {params[0]} * {params[1]}")
    return registers, input


def _div(input: list, registers: dict, params: list) -> tuple:
    print(f"{params[0]} := {params[0]} / {params[1]}")
    return registers, input


def _mod(input: list, registers: dict, params: list) -> tuple:
    print(f"{params[0]} := {params[0]} % {params[1]}")
    return registers, input


def _eql(input: list, registers: dict, params: list) -> tuple:
    print(f"{params[0]} := btou({params[0]} == {params[1]})")
    return registers, input


insts = {
    "inp": _inp,
    "add": _add,
    "mul": _mul,
    "div": _div,
    "mod": _mod,
    "eql": _eql,
}


def part1(inst_list: list, should_print: bool = True) -> None:
    input_val = list(map(int, str(00000000000000)))

    registers = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }

    for inst in inst_list:
        registers, input_val = insts[inst[0]](input_val, registers, inst[1:])



def part2(inst_list: list, num_inputs: int, should_print: bool = True) -> None:
    part2 = 0


    print(f"Part 2: {part2}")


def parse(content):
    inst_list = []

    for i in range(0, len(content)):
        params = content[i].rstrip('\n').split(" ")
        if params[0] != "inp":
            try:
                params[2] = int(params[2])
            except ValueError:
                pass
        inst_list.append(params)

    return inst_list


input = [8, 10]
input_example = [4, 8]


def main():
    print("-------------- Part 1 ------------------")
    # ex_1_inst, ex_1_inp = parse(read_file("day24/input_example"))
    # ex_2_inst, ex_2_inp = parse(read_file("day24/input_example_2"))
    # ex_3_inst, ex_3_inp = parse(read_file("day24/input_example_3"))
    inp_inst = parse(read_file("input"))

    # part1(ex_1_inst, ex_1_inp, should_print=True)
    # part1(ex_2_inst, ex_2_inp, should_print=True)
    # part1(ex_3_inst, ex_3_inp, should_print=True)
    part1(inp_inst, should_print=False)

    print("-------------- Part 2 ------------------")

    # part2(deepcopy(input_example), 444356092776315, should_print=True)

    # part2(deepcopy(input), should_print=False)

if __name__ == "__main__":
    main()
