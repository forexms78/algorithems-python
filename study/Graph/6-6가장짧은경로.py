from collections import deque

def shortestPathBinaryMatrix(grid):
    shortest_path_len = -1
    # row = 5
    row = len(grid)
    # col = 7
    col = len(grid[0])

    if grid[0][0] != 0 and  grid[row-1][col-1] != 0:
        return shortest_path_len


    visited = [[False] * col for _ in range(row)]

    direction = [(1,0), (-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True

    while queue:
        current_row, current_col, current_len = queue.popleft() 
        
        if current_row == row -1 and current_col == col -1:
            shortest_path_len = current_len
            break


        for direction_row, direction_col in direction:
            next_row = current_row + direction_row
            next_col = current_col + direction_col
            if next_row >= 0 and next_row < row and next_col >= 0 and next_col < col:
                if grid[next_row][next_col] == 0 and not visited[next_row][next_col]:
                    queue.append((next_row,next_col,current_len + 1))
                    visited[next_row][next_col] = True



    return shortest_path_len


queue = deque()


print(shortestPathBinaryMatrix(grid=[
    [0,0,0,1,0,0,0],
    [0,1,1,1,0,1,0],
    [0,1,0,0,0,1,0],
    [0,0,0,1,1,1,0],
    [0,1,0,0,0,0,0]
]))