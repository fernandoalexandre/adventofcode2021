
def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()

def is_on_target(point, tl, br):
    x,y = point
    tl_x, tl_y = tl
    br_x, br_y = br
    return tl_x <= x <= br_x and  br_y <= y <= tl_y 

def funct(x, y, vel_x, vel_y):
    x += vel_x
    y += vel_y

    if vel_x > 0:
        vel_x = 0 if vel_x - 1 < 0 else vel_x - 1 
    elif vel_x < 0: 
        vel_x = 0 if vel_x + 1 > 0 else vel_x + 1
    else:
        vel_x = 0

    vel_y -= 1

    return x, y, vel_x, vel_y

def shoot_p1(current_position, vector, target_tl, target_br):
    max_y = 0

    x,y = current_position
    vel_x, vel_y = vector

    while x <= target_br[0] and y >= target_br[1]:
        if is_on_target([x,y], target_tl, target_br):
            return max_y, True
        else:
            x, y, vel_x, vel_y = funct(x, y, vel_x, vel_y)

            max_y = max(max_y, y)
    return max_y, False

def part1(tl, br):
    part1 = 0
    print("--- Part 1 Ship-it ---")

    for vel_x in range(0,999):
        for vel_y in range(0,999):
            curr, is_valid = shoot_p1([0,0], [vel_x, vel_y], tl, br)
            if is_valid:
                part1 = max(part1, curr)
            

    print(f"Part 1: {part1}")

    return part1

def part2(tl, br):    
    print("--- Part 2 Ship-it ---")

    part2 = []

    for vel_x in range(0,999):
        for vel_y in range(-999,999):
            curr, is_valid = shoot_p1([0,0], [vel_x, vel_y], tl, br)
            if is_valid:
                part2.append([vel_x, vel_y])

    print(*part2)
    print(f"Part 2: {len(part2)}")

    return part2

def main():
    content = read_file("day17/input")

    p = content[0].rstrip("\n").lstrip("target area: ")
    target_x, target_y = p.split(", ")

    target_x = target_x.lstrip("x=").split("..")
    target_y = target_y.lstrip("y=").split("..")

    tl = [int(target_x[0]), int(target_y[1])]
    br = [int(target_x[1]), int(target_y[0])]

    print("-------------- Part 1 ------------------")

    p1 = part1(tl, br)

    print("-------------- Part 2 ------------------")

    p2 = part2(tl, br)

if __name__ == "__main__":
    main()