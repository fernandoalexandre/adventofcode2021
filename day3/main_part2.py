def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()

def main():
    content = read_file("day3/input")
    current_values_oxygen = content.copy()
    current_values_co2 = content.copy()
    oxygen = 0
    co2 = 0

    for j in range(0, len(current_values_oxygen[0].rstrip("\n"))):
        zero_counter = 0
        one_counter = 0
        for i in range(0, len(current_values_oxygen)):
            zero_counter += 1 if current_values_oxygen[i][j] == "0" else 0
            one_counter += 1  if current_values_oxygen[i][j] == "1" else 0
        
        if zero_counter > one_counter:
            current_values_oxygen = [x for x in current_values_oxygen if x[j] == "0"]
        else:
            current_values_oxygen = [x for x in current_values_oxygen if x[j] == "1"]
        
        if len(current_values_oxygen) == 1:
            oxygen = int(current_values_oxygen[0], 2)
            break

    for j in range(0, len(current_values_co2[0].rstrip("\n"))):
        zero_counter = 0
        one_counter = 0
        for i in range(0, len(current_values_co2)):
            zero_counter += 1 if current_values_co2[i][j] == "0" else 0
            one_counter += 1  if current_values_co2[i][j] == "1" else 0
        
        if zero_counter > one_counter:
            current_values_co2 = [x for x in current_values_co2 if x[j] == "1"]
        else:
            current_values_co2 = [x for x in current_values_co2 if x[j] == "0"]
        
        if len(current_values_co2) == 1:
            co2 = int(current_values_co2[0], 2)
            break

    print(co2*oxygen)

if __name__ == "__main__":
    main()