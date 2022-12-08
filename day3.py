

def part_1():
    file = open("./inputs/day3.txt")
    # get each rucksack
    sum_priority = 0
    for rucksack in file.readlines():
        mid_index = len(rucksack)//2
        first_half = set(rucksack[0:mid_index])
        second_half = set(rucksack[mid_index:])
        common_item_type = first_half.intersection(second_half)
        sum_priority += getPriority(common_item_type.pop())
    print(sum_priority)

def part_2():
    file = open("./inputs/day3.txt")
    sum_priority = 0
    
    # get each rucksack
    rucksacks = file.readlines()
        
    cur_group = []
    for rucksack in rucksacks:
        cur_group.append(rucksack)
        if len(cur_group) == 3:
            set_1 = set(cur_group[0])
            set_2 = set(cur_group[1])
            set_3 = set(cur_group[2])
            badge = set_1.intersection(set_2.intersection(set_3)) 
            if "\n" in badge:
                badge.remove("\n")
            sum_priority += getPriority(badge.pop())
            cur_group = []
    
    print(sum_priority)

        
        
def getPriority(letter):
    ascii = ord(letter)
    # small letter
    if ascii >= 97:
        return ascii -96
    else:
        return ascii - 38
    
#part_1()
part_2()