def bingo_check(board):
    for row in board:
        if all(cell == "x" for cell in row):
            return True
    
    for col in range(5):
        if all(board[row][col] == "x" for row in range(5)):
            return True
    
    if all(board[i][i] == "x" for i in range(5)):
        return True
    
    if all(board[i][4-i] == "x" for i in range(5)):
        return True
    
    return False


if __name__ == "__main__":
    test1 = [
        [45, "x", 31, 74, 87],
        [64, "x", 47, 32, 90],
        [37, "x", 68, 83, 54],
        [67, "x", 98, 39, 44],
        [21, "x", 24, 30, 52]
    ]
    print(f"Test 1 (Vertical): {bingo_check(test1)}")
    
    test2 = [
        ["x", 43, 31, 74, 87],
        [64, "x", 47, 32, 90],
        [37, 65, "x", 83, 54],
        [67, 98, 39, "x", 44],
        [21, 59, 24, 30, "x"]
    ]
    print(f"Test 2 (Diagonal): {bingo_check(test2)}")
    
    test3 = [
        ["x", "x", "x", "x", "x"],
        [64, 12, 47, 32, 90],
        [37, 16, 68, 83, 54],
        [67, 19, 98, 39, 44],
        [21, 75, 24, 30, 52]
    ]
    print(f"Test 3 (Horizontal): {bingo_check(test3)}")
    
    test4 = [
        [45, "x", 31, 74, 87],
        [64, 78, 47, "x", 90],
        [37, "x", 68, 83, 54],
        [67, "x", 98, "x", 44],
        [21, "x", 24, 30, 52]
    ]
    print(f"Test 4 (No Bingo): {bingo_check(test4)}")
