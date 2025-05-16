def print_zigzag(s: str, numRows: int):
    if numRows == 1 or numRows >= len(s):
        print(s)
        return

    # Create a matrix to hold the zigzag pattern
    zigzag = [[' ' for _ in range(len(s))] for _ in range(numRows)]
    row, col = 0, 0
    down = True

    for char in s:
        zigzag[row][col] = char
        if down:
            if row < numRows - 1:
                row += 1
            else:
                down = False
                row -= 1
                col += 1
        else:
            if row > 0:
                row -= 1
                col += 1
            else:
                down = True
                row += 1

    # Print the zigzag pattern
    for r in zigzag:
        print(''.join(r))

# Example usage:
a=input(" enter a text : ")
b=int(input(" enter num of lines : "))
print_zigzag(a, b)
