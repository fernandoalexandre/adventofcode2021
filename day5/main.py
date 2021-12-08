def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()

seg_map = {}

def main():
    inst = read_file("day5/input")

    for instruction in inst:
        src, dst = instruction.rstrip("\n").split(" -> ")

        src_x, src_y = src.split(",")
        dst_x, dst_y = dst.split(",")

        src_x = int(src_x)
        src_y = int(src_y)
        dst_x = int(dst_x)
        dst_y = int(dst_y)

        curr_x = src_x
        curr_y = src_y
        while curr_x != dst_x or curr_y != dst_y:
            key =  f"{curr_x},{curr_y}"
            if key in seg_map:
                seg_map[key] += 1
            else:
                seg_map[key] = 1
            
            if curr_x > dst_x:
                curr_x -=1
            elif curr_x < dst_x:    
                curr_x +=1
            
            if curr_y > dst_y:
                curr_y -=1
            elif curr_y < dst_y:
                curr_y +=1
        
        key =  f"{curr_x},{curr_y}"
        if key in seg_map:
            seg_map[key] += 1
        else:
            seg_map[key] = 1
        
    print(len([x for x in seg_map.values() if x > 1]))
       
if __name__ == "__main__":
    main()