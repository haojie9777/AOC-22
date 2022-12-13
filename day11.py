import re
class Monkey:

    '''
    inspect all items monkey currently holding
    returns list of tuples (monkey, item_to_add_to_inventory)
    '''
    def __init__(self):
        self.index = None
        self.items = []
        self.divide_test = None
        self.operation_operand = None
        self.operation_value = None
        self.outcome_true = None
        self.outcome_false = None
        self.inspect_count = 0
        
    def inspect_items(self, divisor):
        result = []
        for item in self.items:
            cur_item = item
            # stage 1
            if self.operation_operand == "*":
                if self.operation_value:
                    cur_item *= self.operation_value
                else:
                    cur_item *= cur_item
            else:
                if self.operation_value:
                    cur_item += self.operation_value
                else:
                    cur_item += cur_item
            # stage 2
            if divisor: # part 2
                cur_item %= divisor
            else: # part 1
                cur_item //= 3
            # stage 3
            if cur_item%self.divide_test == 0:
                result.append((self.outcome_true, cur_item))
            else:
                result.append((self.outcome_false, cur_item))
            self.inspect_count += 1
        # thrown everything to other monkeys
        self.items = []
        return result
                
    def add_item(self, item):
        self.items.append(item)
    
    def print_monkey(self):
        print(self.index)
        print(self.items)
        print(self.divide_test)
        print(self.operation_operand)
        print(self.operation_value)
        print(self.outcome_true)
        print(self.outcome_false)
        print(self.inspect_count)
    
monkeys = dict()

def parse_monkey():
    with open("./inputs/day11.txt", "r") as f:
        lines = f.read().splitlines()
        cur_monkey = Monkey()
        # parse monkeys
        for line in lines:
            tokens = line.split()
            if len(tokens) == 0:
                continue
            # get monkey index 
            elif tokens[0] == "Monkey": 
                cur_monkey.index = int(tokens[1][0])
            # starting items
            elif tokens[0] == "Starting":
                numbers = re.findall("[0-9]+", str(tokens))
                for number in numbers:
                    cur_monkey.add_item(int(number))
            elif tokens[0] == "Operation:":
                for token in tokens:
                    if token == "+":
                        cur_monkey.operation_operand = "+"
                    elif token == "*":
                        cur_monkey.operation_operand = "*"
                    elif token.isnumeric():
                        cur_monkey.operation_value = int(token)
                # edge case
                if token[-1] == "old":
                    cur_monkey.operation_value = None
                    
            elif tokens[0] == "Test:":
                for token in tokens:
                    if token.isnumeric():
                        cur_monkey.divide_test = int(token)
            elif tokens[0] == "If" and tokens[1] == "true:":
                for token in tokens:
                    if token.isnumeric():
                        cur_monkey.outcome_true = int(token)
            elif tokens[0] == "If" and tokens[1] == "false:":
                for token in tokens:
                    if token.isnumeric():
                        cur_monkey.outcome_false = int(token)
                # save monkey
                monkeys[cur_monkey.index] = cur_monkey
                cur_monkey = Monkey()
    
            
parse_monkey()

# get the factors 
divisor = 1
for m in monkeys.values():
    divisor *= m.divide_test
    
# simulation
for round in range(10000):
    for monkey in monkeys.values():
        result = monkey.inspect_items(divisor)
        if result:
            for r in result:
                monkeys[r[0]].add_item(r[1])
        

count = []
for m in monkeys.values():
    count.append(m.inspect_count)

count.sort()
print(count[-1] * count[-2])

        
            
                    
            
            

