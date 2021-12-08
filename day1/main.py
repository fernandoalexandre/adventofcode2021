def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()

def main():
    content = read_file("day1/input_example")

    number_increased = 0
    curr_value = int(content[0]) + int(content[1]) + int(content[2])
    prev_value = None

    for i in range(2, len(content)):
        curr_value = int(content[i-2]) + int(content[i-1]) + int(content[i])

        if prev_value != None:
            if curr_value > prev_value:
                number_increased += 1
        
        prev_value = curr_value


    print(number_increased)

if __name__ == "__main__":
    main()