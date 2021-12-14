
def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()

def part1(init_template,  template_list, steps):
    part1 = 0

    curr_template = init_template
    for step in range(0, steps):
        print(f"Step {step}")
        it_template = ""
        for i in range(0,  len(curr_template)-1):
            pair = curr_template[i:i+2]
            it_template += f"{curr_template[i]}{template_list[pair]}"
        it_template += curr_template[-1]
        curr_template = it_template

    hist = {}
    for i in curr_template:
        if i in hist:
            hist[i] += 1
        else:
            hist[i] = 1

    hist_res = sorted(hist.values())
    part1 = hist_res[-1] - hist_res[0]

    debug_hist = {}
    for i in range(0,  len(curr_template)-1):
        if curr_template[i:i+2] in debug_hist:
            debug_hist[curr_template[i:i+2]] += 1
        else:
            debug_hist[curr_template[i:i+2]] = 1

    print(f"Part 1: {part1}")

    return part1, debug_hist, curr_template

def part2(init_template,  template_list, steps):
    entry_histogram = {}
    hist_p2 = {}
    # Setup initial pair histogram and singleton histogram
    for i in range(0,  len(init_template)-1):
        if init_template[i:i+2] in entry_histogram:
            entry_histogram[init_template[i:i+2]] += 1
        else:
            entry_histogram[init_template[i:i+2]] = 1

        if init_template[i] in hist_p2: 
            hist_p2[init_template[i]] += 1
        else:
            hist_p2[init_template[i]] = 1
    
    if init_template[-1] in hist_p2: 
        hist_p2[init_template[-1]] += 1
    else:
        hist_p2[init_template[-1]] = 1

    hist_p2_10 = {"a": 0, "b": 1}

    curr_letters = ""

    curr_histogram = entry_histogram.copy()
    for step in range(0, steps):
        new_histogram = {}

        for key in curr_histogram.keys():
            target = template_list[key]
            number_occurrences = curr_histogram[key]

            if target in hist_p2:
                hist_p2[target] += number_occurrences
            else:
                hist_p2[target] = number_occurrences

            first = f"{key[0]}{target}"
            second = f"{target}{key[1]}"

            curr_letters = f"{curr_letters}{key[0]}{target}"
            
            if first in new_histogram:
                new_histogram[first] += number_occurrences
            else:
                new_histogram[first] = number_occurrences

            if second in new_histogram:
                new_histogram[second] += number_occurrences
            else:
                new_histogram[second] = number_occurrences
        
        if step == 9:
            hist_p2_10 = hist_p2.copy()
        curr_histogram = new_histogram

    hist_res = sorted(hist_p2.values())
    part2 = hist_res[-1] - hist_res[0]

    hist_res_10 = sorted(hist_p2_10.values())
    part2_10 = hist_res_10[-1] - hist_res_10[0]

    print(f"Part 2: {part2}")
    return part2_10, part2, curr_histogram, curr_letters

def main():
    content = read_file("day14/input")

    init_template = content[0].rstrip("\n")
    template_list = {}

    for i in range(2, len(content)):
        content[i] = content[i].rstrip("\n")
        src, rst = content[i].split(" -> ")
        template_list[src]  = rst

    print("-------------- Part 1 ------------------")

    p1 = part1(init_template, template_list, 10)

    print("-------------- Part 2 ------------------")

    p2_10 = part2(init_template, template_list, 40)

    if p2_10 == p1:
        print("Correct Value!")
    else:
        print(f"Invalid Value! p1 {p1} != p2_10 {p2_10}")

if __name__ == "__main__":
    main()