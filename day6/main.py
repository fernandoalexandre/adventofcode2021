import math

input_example = [3,4,3,1,2]
input = [5,1,1,5,4,2,1,2,1,2,2,1,1,1,4,2,2,4,1,1,1,1,1,4,1,1,1,1,1,5,3,1,4,1,1,1,1,1,4,1,5,1,1,1,4,1,2,2,3,1,5,1,1,5,1,1,5,4,1,1,1,4,3,1,1,1,3,1,5,5,1,1,1,1,5,3,2,1,2,3,1,5,1,1,4,1,1,2,1,5,1,1,1,1,5,4,5,1,3,1,3,3,5,5,1,3,1,5,3,1,1,4,2,3,3,1,2,4,1,1,1,1,1,1,1,2,1,1,4,1,3,2,5,2,1,1,1,4,2,1,1,1,4,2,4,1,1,1,1,4,1,3,5,5,1,2,1,3,1,1,4,1,1,1,1,2,1,1,4,2,3,1,1,1,1,1,1,1,4,5,1,1,3,1,1,2,1,1,1,5,1,1,1,1,1,3,2,1,2,4,5,1,5,4,1,1,3,1,1,5,5,1,3,1,1,1,1,4,4,2,1,2,1,1,5,1,1,4,5,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,4,2,1,1,1,2,5,1,4,1,1,1,4,1,1,5,4,4,3,1,1,4,5,1,1,3,5,3,1,2,5,3,4,1,3,5,4,1,3,1,5,1,4,1,1,4,2,1,1,1,3,2,1,1,4]


aux = 0
def main():
    fishes = input
    fish_grouping = [0,0,0,0,0,0,0,0,0]
    fish_grouping_next = [0,0,0,0,0,0,0,0,0]

    for fish in fishes:
        fish_grouping[fish] += 1
    
    for i in range(0, 256):
        fish_grouping_next[8] = fish_grouping[0]
        fish_grouping_next[7] = fish_grouping[8]
        fish_grouping_next[6] = fish_grouping[7] + fish_grouping[0]
        fish_grouping_next[5] = fish_grouping[6]
        fish_grouping_next[4] = fish_grouping[5]
        fish_grouping_next[3] = fish_grouping[4]
        fish_grouping_next[2] = fish_grouping[3]
        fish_grouping_next[1] = fish_grouping[2]
        fish_grouping_next[0] = fish_grouping[1]

        fish_grouping = fish_grouping_next
        fish_grouping_next = [0,0,0,0,0,0,0,0,0]

    total = 0
    for fish in fish_grouping:
        total += fish
    
    print(total)
       
if __name__ == "__main__":
    main()