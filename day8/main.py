import copy

dictionary = [
    ["a", "b", "c", "e", "f", "g"],     #0 -- count 6
    ["c", "f"],                         #1 -- count 2
    ["a", "c", "d", "e", "g"],          #2 -- count 5
    ["a", "c", "d", "f", "g"],          #3 -- count 5
    ["b", "c", "d", "f"],               #4 -- count 4
    ["a", "b", "d", "f", "g"],          #5 -- count 5
    ["a", "b", "d", "e", "f", "g"],     #6 -- count 6
    ["a", "c", "f"],                    #7 -- count 3
    ["a", "b", "c", "d", "e", "f", "g"],#8 -- count 7
    ["a", "b", "c", "d", "f", "g"]      #9 -- count 6
]

def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()

def get_common_dict(signals, should_reverse = False) -> list:
    # returns a dict with 3_5_5_5_6_6_6_7 => a
    new_dict = {}
    result_dict = {}
    for character in ["a", "b", "c", "d", "e", "f", "g"]:
        curr_value = []
        for values in signals:
            if character in values:
                curr_value.append(len(values))
        result_dict[character] = sorted(curr_value)

    for key in result_dict.keys():
        if should_reverse:
            new_dict[key] = "_".join(map(str,result_dict[key]))
        else:
            new_dict["_".join(map(str,result_dict[key]))] = key
    
    return new_dict

def main():
    content = read_file("day8/input")

    print("Calculate known dict")
    known_dict = get_common_dict(dictionary)

    histogram = [0,0,0,0,0,0,0,0,0,0]

    total_sum = 0
    for line in content:
        line = line.rstrip("\n")
        signals, output_display = line.split(" | ")
        signals_list = []
        for signal in signals.split(" "):
            signals_list.append(sorted(signal))

        converted_dict = get_common_dict(signals_list, True)

        print("== Display Output ==")
        
        curr_num = ""
        for signal in output_display.split(" "):
            translate = []
            
            for char in signal:
                translate.append(known_dict[converted_dict[char]])
                
            
            for idx, val in enumerate(dictionary):
                if "".join(map(str,val)) == "".join(map(str,sorted(translate))):
                    histogram[idx] += 1
                    curr_num += str(idx)
                    print(f"{idx}")
            
        total_sum += int(curr_num)
        
        print("== Histogram ==")
        for idx, val in enumerate(histogram):
            print(f"{idx} = {val}")

        print(f"Part 1: {histogram[1] + histogram[4] + histogram[7] + histogram[8]}")
        print(f"Part 2: {total_sum}")



if __name__ == "__main__":
    main()