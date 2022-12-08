import re

def part_1():
    file = open("./inputs/day4.txt")
    lines = file.read().splitlines()
    
    fully_contain_count = 0
    for pair in lines:
        # get range of first and second elves
        numbers = re.findall('[0-9]+', pair)
        # need to cast to int, else will get wrong answer!!
        first_elf = [int(numbers[0]), int(numbers[1])]
        second_elf = [int(numbers[2]), int(numbers[3])]
        
        if first_elf[0] <= second_elf[0] and first_elf[1] >= second_elf[1]:
            fully_contain_count += 1
        elif second_elf[0] <= first_elf[0] and second_elf[1] >= first_elf[1]:
            fully_contain_count +=1
    print(fully_contain_count)
    
def part_2():
    file = open("./inputs/day4.txt")
    lines = file.read().splitlines()
    
    partial_contain_count = 0
    for pair in lines:
        # get range of first and second elves
        numbers = re.findall('[0-9]+', pair)
        first_range = range(int(numbers[0]), int(numbers[1])+1)
        second_range = range(int(numbers[2]), int(numbers[3])+1)
        
        if len(set(first_range).intersection(set(second_range))) > 0:
            partial_contain_count += 1
    print(partial_contain_count)
    
#part_1()
part_2()

    

