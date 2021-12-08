def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()

def main():
    inst = read_file("day2/input_example")
    horizontal = 0
    depth = 0
    aim = 0

    for instruction in inst:
        cmd = instruction.rstrip("\n").split(" ")

        match cmd[0]:
            case "forward":
                horizontal += int(cmd[1])
                depth += int(cmd[1]) * aim
            case "up":
                #depth -= int(cmd[1])
                aim -= int(cmd[1])
            case "down":
                #depth += int(cmd[1])
                aim += int(cmd[1])
            case _:
                raise Exception(f"Opps {cmd[0]} not valid")
        
    print(depth * horizontal)

if __name__ == "__main__":
    main()