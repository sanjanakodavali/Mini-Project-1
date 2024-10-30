ROWS = 6
COLUMNS = 7

def resetBoard():
    return [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]

def printBoard(board):
    for row in range(ROWS):
        print(f"| {6 - row} |", end="")
        for col in range(COLUMNS):
            print(f" {board[row][col]} |", end="")
        print()
        print("-" * 34)
    print("|R/C| a | b | c | d | e | f | g |")
    print("-" * 34)

def validateEntry(board, col):
    if col < 0 or col >= COLUMNS or board[0][col] != " ":
        return False
    return True

def availablePosition(board, col):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            return row
    return -1

def checkFull(board):
    for row in board:
        if " " in row:
            return False
    return True

def checkWin(board, row, col, token):
    count = 0
    for c in range(max(0, col - 3), min(COLUMNS, col + 4)):
        if board[row][c] == token:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    count = 0
    for r in range(max(0, row - 3), min(ROWS, row + 4)):
        if board[r][col] == token:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    count = 0
    for i in range(-3, 4):
        r = row + i
        c = col + i
        if 0 <= r < ROWS and 0 <= c < COLUMNS:
            if board[r][c] == token:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    count = 0
    for i in range(-3, 4):
        r = row + i
        c = col - i
        if 0 <= r < ROWS and 0 <= c < COLUMNS:
            if board[r][c] == token:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    return False

def checkEnd(board, row, col, token):
    if checkWin(board, row, col, token):
        print(f"\n{token} IS THE WINNER!!!")
        printBoard(board)
        return True
    elif checkFull(board):
        print("The game is a draw.")
        return True
    return False

def playConnectFour():
    repeat = "yes"
    while repeat[0].lower() == "y":
        board = resetBoard()
        current_player = 'X'
        game_over = False

        print("New game: X goes first.\n")
        printBoard(board)

        while not game_over:
            print(f"\n{current_player}'s turn.")
            print(f"Where do you want your {current_player} played?")

            available_positions = []
            for col in range(COLUMNS):
                row = availablePosition(board, col)
                if row != -1:
                    available_positions.append(chr(97 + col) + str(ROWS - row))

            print(f"Available positions are: {available_positions}")

            col_input = input(f"\nPlease enter column-letter and row-number (e.g., a1): ").strip().lower()

            if len(col_input) != 2 or col_input[0] not in "abcdefg" or not col_input[1].isdigit():
                print("Invalid input. Please enter a valid position like 'a1'.")
                continue

            col = ord(col_input[0]) - ord('a')
            row = ROWS - int(col_input[1])

            if not validateEntry(board, col):
                print("Invalid move. Column is full or out of range.")
                continue

            row = availablePosition(board, col)
            board[row][col] = current_player
            print("Thank you for your selection.")

            game_over = checkEnd(board, row, col, current_player)

            if not game_over:
                printBoard(board)

            if not game_over:
                current_player = 'O' if current_player == 'X' else 'X'

        repeat = input("Another game (y/n)? ")
    print("Thank you for playing!")

playConnectFour()
