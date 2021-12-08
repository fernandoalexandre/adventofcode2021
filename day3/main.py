def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()

def main():
    content = read_file("day3/input")
    gamma = ""
    epsilon = ""
    for j in range(0, len(content[0].rstrip("\n"))):
        zero_counter = 0
        one_counter = 0
        for i in range(0, len(content)):
            zero_counter += 1 if content[i][j] == "0" else 0
            one_counter += 1  if content[i][j] == "1" else 0
        
        if zero_counter > one_counter:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    print(int(gamma,2)*int(epsilon,2))

if __name__ == "__main__":
    main()