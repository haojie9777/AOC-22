
'''
At each cycle, get x value.
If cycle within x-value +- 1, set pixel at cycle position to 1
'''
with open("./inputs/day10.txt", "r") as f:
    sum_of_signal_strength = 0
    x = 1
    need_record = {20, 60, 100, 140, 180, 220}
    to_update = None
    skip_cycle = False
    
    crt_display = ["." for i in range(240)]
    
    def update_x_and_record(cycle, skip_cycle):
        global to_update,x, sum_of_signal_strength
        if to_update and not skip_cycle:
            x += to_update
            to_update = None
        # cycle is within x-value +/- 1, draw on crt
        # transpose cycle to between 1 and 40
        tranposed_cycle = cycle
        if 41 <= cycle <= 80:
            tranposed_cycle = cycle - 40
        elif 81 <= cycle <= 120:
            tranposed_cycle = cycle - 80
        elif 121 <= cycle <= 160:
            tranposed_cycle = cycle - 120
        elif 161 <= cycle <= 200:
            tranposed_cycle = cycle - 160
        elif 201 <= cycle <= 240:
            tranposed_cycle = cycle - 200
        if abs(tranposed_cycle - 1 - x) <= 1:
            position_drawn = cycle - 1
            crt_display[position_drawn] = "#" 
            
        if cycle in need_record:
            sum_of_signal_strength += cycle * x
        
    lines = f.read().splitlines()
    
    for cycle in range(1,300):   
        update_x_and_record(cycle,skip_cycle)
        if skip_cycle:
            skip_cycle = False
            continue
        
        if len(lines) == 0:
            break
        # get the next instruction
        instruction = lines.pop(0)
    
        tokens = instruction.split()     
        if tokens[0] == "noop":
            pass
        else:
            to_update = int(tokens[1])
            skip_cycle = True
            
    print(sum_of_signal_strength)
    print(crt_display[0:40])
    print(crt_display[40:80])
    print(crt_display[80:120])
    print(crt_display[120:160])
    print(crt_display[160:200])
    print(crt_display[200:240])
    
    
    

  
    
        
        
            
    
  
    

  
            
            
      
