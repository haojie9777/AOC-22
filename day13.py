import functools

with open("./inputs/day13.txt", "r") as f:
    lines = f.read().splitlines()
    packets = []
    for line in lines:
        if len(line) > 0:
            packets.append(eval(line))
    
    def in_order(packet_1, packet_2):
        elements = zip(packet_1, packet_2)
        for a, b in elements:
            # both values are list
            if isinstance(a, list) and isinstance(b, list):   
                c = in_order(a,b) 
                if c == 1 or c == -1:
                    return c 
              
            # only left value is list, convert right side to list too
            elif isinstance(a, list) and not isinstance(b, list):
                b = [b]
                c = in_order(a, b)
                if c == 1 or c == -1:
                    return c  
            # only right value is list
            elif not isinstance(a, list) and isinstance(b, list):
                a = [a]
                c = in_order(a,b)
                if c == 1 or c == -1:
                    return c
            # both are integers
            else:
                c = basic_compare(a, b)
                if c == 1 or c == -1:
                    return c
                    
        # can't conclude after comparing all elements, need check length
        if len(packet_1) < len(packet_2):
            return 1
        elif len(packet_1) > len(packet_2):
            return -1
        else:
            return 0
     
    def basic_compare(a,b):
        if a < b:
            return 1
        elif a > b:
            return -1
        return 0
    
    def part_1():
        index = 1
        res = 0
        while len(packets) > 0:
            packet_1 = packets.pop(0)
            packet_2 = packets.pop(0)

            if in_order(packet_1, packet_2) >= 0:
                res += index
            index += 1
        return res
    
    def part_2():
        packets.append([[2]])
        packets.append([[6]])
        sorted_packets = sorted(packets, key=functools.cmp_to_key(in_order), reverse = True)
        index_1 = sorted_packets.index([[2]]) + 1
        index_2 = sorted_packets.index([[6]]) + 1
        return index_1 * index_2
     
    print("Part 1: {}".format(part_1()))
    print("Part 2: {}".format(part_2()))

    
            
    
        
    
    
        
    
        
        