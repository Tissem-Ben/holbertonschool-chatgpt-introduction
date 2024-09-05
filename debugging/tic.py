#!/usr/bin/python3

def print_board(board):
    """
    Print the current state of the board.
    
    Parameters:
    board (list): A 2D list representing the Tic Tac Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there is a winner in the current board state.
    
    Parameters:
    board (list): A 2D list representing the Tic Tac Toe board.
    
    Returns:
    bool: True if there is a winner, otherwise False.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """
    Check if the game is a draw (no empty spaces left).
    
    Parameters:
    board (list): A 2D list representing the Tic Tac Toe board.
    
    Returns:
    bool: True if the game is a draw, otherwise False.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to run the Tic Tac Toe game.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        # Input validation for row and column
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Row and column must be 0, 1, or 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        # Check if the spot is available
        if board[row][col] == " ":
            board[row][col] = player
            # Check for winner after placing the mark
            if check_winner(board):
                print_board(board)
                print("Player " + player + " wins!")
                break
            # Check for draw
            if check_draw(board):
                print_board(board)
                print("The game is a draw!")
                break
            # Switch player
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

tic_tac_toe()