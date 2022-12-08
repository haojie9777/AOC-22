import collections
with open("./inputs/day7.txt") as f:
    lines = f.read().splitlines()
    
    nodes = collections.defaultdict(int)
    '''
    stores file size about a directory
    key: unique path "./a/c"
    value:
    file size
    '''
    cur_path =[]
    for line in lines:
        tokens = line.split(" ")
        
        if tokens[0] == "$":
             # update current path
            if tokens[1] == "cd":
                if tokens[2] != "..":
                    cur_path.append(tokens[2])
                else:
                    cur_path.pop()
            
        # is a file
        if tokens[0].isnumeric():
            temp = list(cur_path)
            # add file size to current dir and its parents
            while len(temp) > 0:
                path_key = " ".join(temp)
                nodes[path_key] += int(tokens[0])
                temp.pop()
    res = 0
    for value in nodes.values():
        if value <= 100000:
            res += value 
    print(res)
    free_size = 70000000 - nodes["/"]
    size_to_be_free = 30000000 - free_size
    to_delete = float("inf")
    for value in nodes.values():
        if value >= size_to_be_free:
            to_delete = min(value, to_delete)
    print(to_delete)
            
        
    
        
        
        
            
       
                
                    
                
            
        
        
    
    