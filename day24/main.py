from multiprocessing import Pool


def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()


def _inp(input: list, registers: dict, params: list) -> tuple:
    registers[params[0]] = input[0]
    return registers, input[1:]


def _add(input: list, registers: dict, params: list) -> tuple:
    if isinstance(params[1], int):
        registers[params[0]] += int(params[1])
    else:
        registers[params[0]] += registers[params[1]]
    return registers, input


def _mul(input: list, registers: dict, params: list) -> tuple:
    if isinstance(params[1], int):
        registers[params[0]] *= int(params[1])
    else:
        registers[params[0]] *= registers[params[1]]
    return registers, input


def _div(input: list, registers: dict, params: list) -> tuple:
    if isinstance(params[1], int):
        registers[params[0]] = int(registers[params[0]] / int(params[1]))
    else:
        registers[params[0]] = int(registers[params[0]] / registers[params[1]])
    return registers, input


def _mod(input: list, registers: dict, params: list) -> tuple:
    if isinstance(params[1], int):
        registers[params[0]] = registers[params[0]] % int(params[1])
    else:
        registers[params[0]] = registers[params[0]] % registers[params[1]]
    return registers, input


def _eql(input: list, registers: dict, params: list) -> tuple:
    if isinstance(params[1], int):
        registers[params[0]] = int(registers[params[0]] == int(params[1]))
    else:
        registers[params[0]] = int(registers[params[0]] == registers[params[1]])
    return registers, input


insts = {
    "inp": _inp,
    "add": _add,
    "mul": _mul,
    "div": _div,
    "mod": _mod,
    "eql": _eql,
}


def validate_model_p1(inst_list, model_num: int) -> bool:
    input_val = list(map(int, str(model_num)))

    if 0 in input_val:
        return False

    registers = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }

    for inst in inst_list:
        registers, input_val = insts[inst[0]](input_val, registers, inst[1:])

    return registers['z'] == 0


def validate_model_hardcoded(input_val: list) -> bool:
    w = 0
    z = 0

    z = input_val[0] + 16
    z = (z * 26) + input_val[1] + 3
    z = (z * 26) + input_val[2] + 2
    z = (z * 26) + input_val[3] + 7
    w = input_val[4]
    z = int(z / 26)
    if ((z % 26) - 10) != w:
        z = (z * 26) + w + 13
    w = input_val[5]
    if ((z % 26) + 15) != w:
        z = (z * 26) + w + 6
    w = input_val[6]
    z = int(z / 26)
    if ((z % 26) - 14) != w:
        z = (z * 26) + w + 10
    w = input_val[7]
    if ((z % 26) + 10) != w:
        z = (z * 26) + w + 11
    w = input_val[8]
    z = int(z / 26)
    if ((z % 26) - 4) != w:
        z = (z * 26) + w + 6
    w = input_val[9]
    z = int(z / 26)
    if ((z % 26) - 3) != w:
        z = (z * 26) + w + 5
    w = input_val[10]
    if ((z % 26) + 13) != w:
        z = (z * 26) + w + 11
    w = input_val[11]
    z = int(z / 26)
    if ((z % 26) - 3) != w:
        z = (z * 26) + w + 4
    w = input_val[12]
    z = int(z / 26)
    if ((z % 26) - 9) != w:
        z = (z * 26) + w + 4
    w = input_val[13]
    z = int(z / 26)
    if ((z % 26) - 12) != w:
        z = (z * 26) + w + 6

    return z == 0


def part1_threaded(first):
    for m in range(1, 10):
        for l in range(1, 10):
            for k in range(1, 10):
                for j in range(1, 10):
                    for i in range(1, 10):
                        print(f"i = {i}")
                        for h in range(1, 10):
                            for g in range(1, 10):
                                for f in range(1, 10):
                                    for e in range(1, 10):
                                        for d in range(1, 10):
                                            for c in range(1, 10):
                                                for b in range(1, 10):
                                                    for a in range(1, 10):
                                                        value = [first, a, b, c, d, e, f, g, h, i, j, k, l, m]
                                                        if validate_model_hardcoded(value):
                                                            print(f"Part 1: {value}")
                                                            break


def part1(inst_list: list, num_inputs: int, should_print: bool = True) -> None:
    with Pool(9) as p:
        p.map(part1_threaded, [9, 8, 7, 6, 5, 4, 3, 2, 1])



def part2(inst_list: list, num_inputs: int, should_print: bool = True) -> None:
    part2 = 0

    print(f"Part 2: {part2}")


def parse(content):
    inst_list = []
    num_input = 0

    for i in range(0, len(content)):
        params = content[i].rstrip('\n').split(" ")
        if params[0] != "inp":
            try:
                params[2] = int(params[2])
            except ValueError:
                pass
        num_input += 1 * (params[0] == "inp")  # hooray branchless programming
        inst_list.append(params)

    return inst_list, num_input


def main():
    print("-------------- Part 1 ------------------")
    inp_inst, inp_inp = parse(read_file("day24/input"))

    part1(inp_inst, inp_inp, should_print=False)

    print("-------------- Part 2 ------------------")

    # part2(deepcopy(input_example), 444356092776315, should_print=True)

    # part2(deepcopy(input), should_print=False)


if __name__ == "__main__":
    main()
