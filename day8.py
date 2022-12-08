def is_blocked(row, col, matrix):
    # check if outer edges
    if row == 0 or row == len(matrix) - 1 or col == 0 or col == len(matrix[0]) -1:
        return False
    
    is_blocked = False
    
    height = matrix[row][col]
    # check 4 directions
    top = row - 1
    while top >= 0:
        if matrix[top][col] >= height:
            is_blocked = True
        top -= 1
    if not is_blocked:
        return False
    
    is_blocked = False
    bottom = row + 1
    while bottom <= len(matrix) - 1:
        if matrix[bottom][col] >= height:
            is_blocked = True
        bottom += 1
    if not is_blocked:
        return False
    
    is_blocked = False
    left = col - 1
    while left >= 0:
        if matrix[row][left] >= height:
            is_blocked = True
        left -= 1
    if not is_blocked:
        return False
    
    is_blocked = False
    right = col + 1
    while right <= len(matrix[0]) - 1:
        if matrix[row][right] >= height:
            is_blocked = True
        right += 1
    if not is_blocked:
        return False
    
    return True

def count_score(row, col, matrix):
    if row == 0 or row == len(matrix) - 1 or col == 0 or col == len(matrix[0]) -1:
        return 0
    
    height = matrix[row][col]
    
    top = row - 1
    top_score = 0
    while top >= 0:
        if height > matrix[top][col]:
            top_score += 1
        else:
            top_score += 1 
            break
        top -= 1
        
    bot_score = 0
    bottom = row + 1
    while bottom <= len(matrix) - 1:
        if height > matrix[bottom][col]:
            bot_score += 1
        else:
            bot_score += 1 
            break
        bottom += 1
        
    left_score = 0
    left = col - 1
    while left >= 0:
        if height > matrix[row][left]:
            left_score += 1
        else:            
            left_score += 1 
            break
        left -= 1
    
    
    right_score = 0
    right = col + 1
    while right <= len(matrix[0]) - 1:
        if height > matrix[row][right]:
            right_score += 1
        else:
            right_score += 1
            break
        right += 1
    return top_score * bot_score * left_score * right_score
   
    


def main():
    with open("./inputs/day8.txt") as f:
        lines = f.read().splitlines()
        
        # reconstruct matrix
        matrix = []
        for line in lines:
            col = list(line)
            matrix.append(col)
                
        visible_count = 0
        highest_score = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not is_blocked(i,j,matrix):
                    visible_count += 1
                highest_score = max(highest_score, count_score(i,j,matrix))
        print(visible_count) 
        print(highest_score)  

main()
                
 


        
    
    
    
