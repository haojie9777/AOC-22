with open("./inputs/day9.txt", "r") as f:
  lines = f.read().splitlines()

  pos_count = 1

  # track positions that the tail has visited
  visited = set()
  visited.add((0,0))
  
  knots = [(0,0) for i in range(9)]
  
  def new_head(cur_head, direction):
      new_head = None
	  # find new head position
      if direction == "R":
        new_head = (cur_head[0], cur_head[1] + 1)
      elif direction == "L":
        new_head = (cur_head[0], cur_head[1] - 1)
      elif direction == "U":
        new_head = (cur_head[0] - 1, cur_head[1])
      else:
        new_head =(cur_head[0] + 1, cur_head[1])
      return new_head

      


  def advance(cur_head, new_head, cur_tail):
    new_tail = None
  
    # check if new head is touching tail, then tail don't need to move
    # same row    
    if cur_tail[0] == new_head[0] and 0 <= abs(cur_tail[1] - new_head[1]) <= 1:
        return [new_head, cur_tail]
    # same column
    if cur_tail[1] == new_head[1] and 0 <= abs(cur_tail[0] - new_head[0]) <= 1:
        return [new_head, cur_tail]
    # check if touching diagonally
    if abs(cur_tail[0] - new_head[0]) == 1 and abs(cur_tail[1] - new_head[1]) == 1:
      return [new_head, cur_tail]
    
    # tail needs to move
    # scenario 1: tail follow head in a single plane
    # same row
    if cur_tail[0] == new_head[0]:
        if direction == "R":
            new_tail = (cur_tail[0], cur_tail[1] + 1)
        else:
             new_tail = (cur_tail[0], cur_tail[1] - 1)
    # same column
    elif cur_tail[1] == new_head[1]:
        if direction == "U":
            new_tail = (cur_tail[0] - 1, cur_tail[1])
        else:
             new_tail = (cur_tail[0] + 1, cur_tail[1])
    # scenario 2: tail jumps to head prev position from diagonal arrangement
    else:
       new_tail = cur_head
    return [new_head, new_tail]
    

  for line in lines:
    tokens = line.split(" ")
    direction, steps = tokens[0], int(tokens[1])
    for i in range(steps):
        for j in range(8):
            old_head = knots[j]
            if j == 0:
               knots[j] = new_head(knots[j], direction)
            knots[j], knots[j+1] = advance(old_head, knots[j], knots[j+1])
                
        print(knots,i)
        if knots[-1] not in visited:
            visited.add(knots[-1])
            pos_count += 1
print(pos_count)