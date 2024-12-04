#Solution1
def solution1(matrix):
    sol1=0
    rows = len(matrix)
    cols = len(matrix[0])
    
    #iterate over grid
    for r in range(rows):
        for c in range(cols):
            if c+3<cols and matrix[r][c]=='X' and matrix[r][c+1]=='M' and matrix[r][c+2]=='A' and matrix[r][c+3]=='S':
                sol1 += 1
            if r+3<rows and matrix[r][c]=='X' and matrix[r+1][c]=='M' and matrix[r+2][c]=='A' and matrix[r+3][c]=='S':
                sol1 += 1
            if r+3<rows and c+3<cols and matrix[r][c]=='X' and matrix[r+1][c+1]=='M' and matrix[r+2][c+2]=='A' and matrix[r+3][c+3]=='S':
                sol1 += 1
            if c+3<cols and matrix[r][c]=='S' and matrix[r][c+1]=='A' and matrix[r][c+2]=='M' and matrix[r][c+3]=='X':
                sol1 += 1
            if r+3<rows and matrix[r][c]=='S' and matrix[r+1][c]=='A' and matrix[r+2][c]=='M' and matrix[r+3][c]=='X':
                sol1 += 1
            if r+3<rows and c+3<cols and matrix[r][c]=='S' and matrix[r+1][c+1]=='A' and matrix[r+2][c+2]=='M' and matrix[r+3][c+3]=='X':
                sol1 += 1
            if r-3>=0 and c+3<cols and matrix[r][c]=='S' and matrix[r-1][c+1]=='A' and matrix[r-2][c+2]=='M' and matrix[r-3][c+3]=='X':
                sol1 += 1
            if r-3>=0 and c+3<cols and matrix[r][c]=='X' and matrix[r-1][c+1]=='M' and matrix[r-2][c+2]=='A' and matrix[r-3][c+3]=='S':
                sol1 += 1

    return sol1

#solution2
def solution2(matrix):
    sol2=0
    rows = len(matrix)
    cols = len(matrix[0])
    
    #iterate over grid
    for r in range(rows):
        for c in range(cols):
            if r+2<rows and c+2<cols and matrix[r][c]=='M' and matrix[r+1][c+1]=='A' and matrix[r+2][c+2]=='S' and matrix[r+2][c]=='M' and matrix[r][c+2]=='S':
                sol2 += 1
            if r+2<rows and c+2<cols and matrix[r][c]=='M' and matrix[r+1][c+1]=='A' and matrix[r+2][c+2]=='S' and matrix[r+2][c]=='S' and matrix[r][c+2]=='M':
                sol2 += 1
            if r+2<rows and c+2<cols and matrix[r][c]=='S' and matrix[r+1][c+1]=='A' and matrix[r+2][c+2]=='M' and matrix[r+2][c]=='M' and matrix[r][c+2]=='S':
                sol2 += 1
            if r+2<rows and c+2<cols and matrix[r][c]=='S' and matrix[r+1][c+1]=='A' and matrix[r+2][c+2]=='M' and matrix[r+2][c]=='S' and matrix[r][c+2]=='M':
                sol2 += 1
    return sol2

filename="./input_sample.txt"
with open(filename) as filehandler:
    lines = filehandler.readlines()
    char_matrix = [list(line.strip()) for line in lines]
    #print(char_matrix)

    print(solution1(char_matrix))
    print(solution2(char_matrix))

    

