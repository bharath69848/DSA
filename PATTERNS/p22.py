for i in range(1, 11):
    for j in range(1, 11):
        # Calculate distances to each edge
        top = i
        bottom = 11 - i # Distance from the bottom edge (row 10)
        left = j
        right = 11 - j # Distance from the right edge (column 10)
        
        # The value for the cell is the minimum of these distances
        print(min(top, bottom, left, right), end=" ")
    print()