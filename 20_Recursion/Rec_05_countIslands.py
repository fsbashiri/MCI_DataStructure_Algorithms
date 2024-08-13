# Find the number of islands in a 2D matrix. An island is a group of connected 0s to 
# the north, south, east, and west, and surrounded by 1s. Don't count 0s that are at 
# the edge of the matrix.

def islandFinder(arr):
    counter = 0
    visited = set()
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[0])-1):
            if arr[i][j] == 0 and (i,j) not in visited:
                counter += 1
                dfs(arr, i, j, visited)
    
    return counter

# depth first traverse algorithm
def dfs(arr, i, j, visited):
    # print(i, j)
    if i < 0 or i >= len(arr) or j < 0 or j >= len(arr[0]) or arr[i][j] == 1 or (i,j) in visited:
        return
    visited.add((i,j))
    dfs(arr, i+1, j, visited)  # down
    dfs(arr, i-1, j, visited)  # up
    dfs(arr, i, j+1, visited)  # right
    dfs(arr, i, j-1, visited)  # left


arr = [[1,1,1,1,1,1,1,0],
       [1,0,0,0,0,1,1,0],
       [1,0,1,0,1,1,1,0],
       [1,0,0,0,0,1,0,1],
       [1,1,1,1,1,1,1,0]]
print(islandFinder(arr))
