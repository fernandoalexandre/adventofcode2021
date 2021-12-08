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

result_dict = {}
for character in ["a", "b", "c", "d", "e", "f", "g"]:
    curr_value = []
    for idx, values in enumerate(dictionary):
        if character in values:
            curr_value.append(len(values))

    
    result_dict[character] = sorted(curr_value)
    total = 0
    for idx, val in enumerate(sorted(curr_value)):
        total += idx+1*val
    



for key in result_dict.keys():
    print(f"{key} = {result_dict[key]}")