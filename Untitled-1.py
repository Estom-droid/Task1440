def path(triangle):
    if not triangle:
        return 0
    
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):

            triangle[row][col] += min(
                triangle[row + 1][col], 
                triangle[row + 1][col + 1]
            )
    
    return triangle[0][0]
#Задайте Треугольник  
triangle = [ [2], [3, 4], [6, 5, 7], [4, 1, 8, 3], [5, 8, 9, 0, 6] ]
print(path(triangle))
