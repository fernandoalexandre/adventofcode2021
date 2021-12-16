
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
    #print(f"Processing: {packet}")

    version = int(packet[0:3], 2)
    packet = packet[3:]
    ptype = int(packet[0:3], 2)
    packet = packet[3:]

    values = []
    final_value = 0

    if ptype == 4:
        prefix = packet[0]
        packet = packet[1:]
        actual_value = ''
        while prefix != '-1':
            actual_value = f"{actual_value}{packet[0:4]}"
            packet = packet[4:]

            if prefix == '0':
                prefix = '-1'
            else:
                prefix = packet[0]
                packet = packet[1:]

        #print(f"Found packet: version: {version} | type = {ptype} | value = {int(actual_value, 2)} ({actual_value})")
        final_value = int(actual_value, 2)
    else:
        length_type_id = packet[0]
        packet = packet[1:]
        len_value_len = 15 if length_type_id == '0' else 11

        if length_type_id == '1':
            # number of packets
            num_packets = packet[:len_value_len]
            packet = packet[len_value_len:]
            
            #print(f"Found packet: version: {version} | type = {ptype} | num_packets = {int(num_packets, 2)} ({num_packets})")
            
            for _ in range(0, int(num_packets, 2)):
                value, packet = parse_packet_p2(packet)
                values.append(value)
        else:
            # length of the packet
            length = packet[:len_value_len]
            packet = packet[len_value_len:]

            #print(f"Found packet: version: {version} | type = {ptype} | num_packets = {int(length, 2)} ({length})")

            consumed_length = 0
            while consumed_length < int(length, 2):
                initial_len = len(packet)
                value, packet = parse_packet_p2(packet)
                values.append(value)
                consumed_length += initial_len - len(packet)
        
        if ptype == 0:
            # sum
            final_value = 0
            #print("sum")
            #print(*values)
            for val in values:
                final_value += val

        elif ptype == 1:
            # product
            final_value = 1
            #print(f"product")
            #print(*values)
            for val in values:
                final_value *= val

        elif ptype == 2:
            # minimum
            #print("min")
            #print(*values)
            final_value = min(values)
        
        elif ptype == 3:
            # maximum
            #print("max")
            #print(*values)
            final_value = max(values)
        
        elif ptype == 5:
            # greater than
            #print("greater")
            #print(*values)

            final_value = 1 if values[0] > values[1] else 0 
        elif ptype == 6:
            # less than
            #print("less")
            #print(*values)

            final_value = 1 if values[0] < values[1] else 0 
        elif ptype == 7:
            # equal to
            #print("eq")
            #print(*values)
            final_value = 1 if values[0] == values[1] else 0 
    
    return final_value, packet

def parse_packet_p1(packet):
    #print(f"Processing: {packet}")

    version = int(packet[0:3], 2)
    pversion_sum = int(packet[0:3], 2)
    packet = packet[3:]
    ptype = int(packet[0:3], 2)
    packet = packet[3:]

    if ptype == 4:
        prefix = packet[0]
        packet = packet[1:]
        actual_value = ''
        while prefix != '-1':
            actual_value = f"{actual_value}{packet[0:4]}"
            packet = packet[4:]

            if prefix == '0':
                prefix = '-1'
            else:
                prefix = packet[0]
                packet = packet[1:]

        #print(f"Found packet: version: {version} | type = {ptype} | value = {int(actual_value, 2)} ({actual_value})")
        actual_value = int(actual_value, 2)
    else:
        length_type_id = packet[0]
        packet = packet[1:]
        len_value_len = 15 if length_type_id == '0' else 11

        if length_type_id == '1':
            # number of packets
            num_packets = packet[:len_value_len]
            packet = packet[len_value_len:]
            
            #print(f"Found packet: version: {version} | type = {ptype} | num_packets = {int(num_packets, 2)} ({num_packets})")
            
            for _ in range(0, int(num_packets, 2)):
                p_v_sum, packet = parse_packet_p1(packet)
                pversion_sum += p_v_sum
        else:
            # length of the packet
            length = packet[:len_value_len]
            packet = packet[len_value_len:]

            #print(f"Found packet: version: {version} | type = {ptype} | num_packets = {int(length, 2)} ({length})")

            consumed_length = 0
            while consumed_length < int(length, 2):
                initial_len = len(packet)
                #print(f"{consumed_length} < {int(length, 2)}")
                p_v_sum, packet = parse_packet_p1(packet)
                pversion_sum += p_v_sum
                consumed_length += initial_len - len(packet)
    
    return pversion_sum, packet

def part1(packets):
    part1 = 0

    # Tests
    print("--- Part 1 Test #1 ---")
    val, _ = parse_packet_p1(bin(int('1'+"D2FE28", 16))[3:])
    print(f"D2FE28 => {val}")
    print("--- Part 1 Test #2 ---")
    val, _ = parse_packet_p1(bin(int('1'+"38006F45291200", 16))[3:])
    print(f"38006F45291200 => {val}")
    print("--- Part 1 Test #3 ---")
    val, _ = parse_packet_p1(bin(int('1'+"EE00D40C823060", 16))[3:])
    print(f"EE00D40C823060 => {val}")

    print("--- Part 1 Ship-it ---")
    for packet in packets:
        part1, _ = parse_packet_p1(packet)
        print(f"Part 1: {part1}")

    return part1

def part2(packets):
    part2 = 0

    print("--- Part 1 Ship-it ---")
    for packet in packets:
        part2, _ = parse_packet_p2(packet)
        print(f"Part 2: {part2}")

    return part2

def main():
    content = read_file("day16/input")

    packets = []
    for line in content:
        packets.append(bin(int('1'+line.rstrip("\n"), 16))[3:])

    print("-------------- Part 1 ------------------")

    p1 = part1(packets)

    print("-------------- Part 2 ------------------")

    p2 = part2(packets)

if __name__ == "__main__":
    main()