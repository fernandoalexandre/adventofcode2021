
def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()

def is_valid(i, j, n, m):
    return 0 <= i <= n and 0 <= j <= m

def parse_type4_packet(packet):
    values = packet[7:]
    actual_value = ''
    for index in range(0, len(values), 5):
        prefix = values[index]
        
        actual_value = f"{actual_value}{values[index+1:index+5]}"

        if prefix == 0:
            break
    
    return int(actual_value, 2)

def parse_packet_p2(packet):
    pversion_sum = int(packet[0:3], 2)
    ptype = int(packet[3:7], 2)

    match ptype:
        case 4:
            values = packet[7:]
            actual_value = ''
            for index in range(0, len(values), 5):
                prefix = values[index]
                
                actual_value = f"{actual_value}{values[index+1:index+5]}"

                if prefix == 0:
                    break
            
            actual_value = int(actual_value, 2)
        case _:
            length_type_id = packet[7]
            len_value_len = 15 if length_type_id == 0 else 11

            if length_type_id == 1:
                # number of packets
                for i in range(0, int(packet[7:7+len_value_len])):
                    p_v_sum = parse_packet_p1(packet[7+len_value_len:])
                    pversion_sum += p_v_sum
            else:
                # length of the 
                print("lol")
    
    return pversion_sum

def parse_packet_p1(packet):
    version = int(packet[0:3], 2)
    pversion_sum = int(packet[0:3], 2)
    packet = packet[3:]
    ptype = int(packet[0:3], 2)
    packet = packet[3:]

    match ptype:
        case 4:
            prefix = packet[0]
            packet = packet[1:]
            actual_value = ''
            while prefix != '-1':
                actual_value = f"{actual_value}{packet[0:4]}"
                packet = packet[5:]

                if prefix == '0':
                    prefix = '-1'
                else:
                    prefix = packet[0]

            print(f"Found packet: version: {version} | type = {ptype} | value = {int(actual_value, 2)} ({actual_value})")
            actual_value = int(actual_value, 2)
        case _:
            length_type_id = packet[7]
            len_value_len = 15 if length_type_id == 0 else 11

            if length_type_id == 1:
                # number of packets
                remainder = packet[7+len_value_len:]
                num_packets = packet[7:7+len_value_len]
                for i in range(0, int(num_packets, 2)):
                    p_v_sum, remainder = parse_packet_p1(remainder)
                    pversion_sum += p_v_sum
            else:
                # length of the 
                print("lol")
    
    return pversion_sum





def part1(packet):
    part1 = 0

    # Tests
    print("Part 1 Tests")
    parse_packet_p1(bin(int('1'+"D2FE28", 16))[3:])

    print(f"Part 1: {part1}")

    return part1

def part2(packet):
    part2 = 0

    print(f"Part 2: {part2}")

    return part2

def main():
    content = read_file("day16/input_example")

    packet = bin(int('1'+content[0].rstrip("\n"), 16))[3:]

    print("-------------- Part 1 ------------------")

    p1 = part1(packet)

    print("-------------- Part 2 ------------------")

    p2 = part2(packet)

if __name__ == "__main__":
    main()