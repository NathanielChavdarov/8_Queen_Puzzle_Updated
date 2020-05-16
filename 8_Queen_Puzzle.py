table = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]
         ]

# Create a function to check if the row and column is safe


def isSafe(row, col, place):
    # Check that the row is safe
    for i in range(0, 8):
        if place[row][i] == 1:
            print("Unsafe")

    # Check that the column is safe
    for l in range(0, 8):
        if place[l][col] == 1:
            print("Unsafe")

    # Check that the diagonals are safe
    for z in range(0, 8):
      if place[row+z][col+z] == 1:
        print("Unsafe")


def solver(current_col, place):

    # Counts the amount of queens
    Counter = 0

    # Adding first queen
    # Ensuring we start at 0, 0
    current_col = 0

    # First queen being added
    for i in range(0, 8):
        place[i][current_col] = "Q"
        isSafe(i, current_col, place)
        current_col += 1

        # Add restraint for current_col
        if current_col > 7:
          print("No more moves")

    print(table)

solver(0, table)
