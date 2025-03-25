import hashlib
import os

flag = os.environ.get("FLAG")

def is_secret_input(user_input):
    secret_hash = "0917b13a9091915d54b6336f45909539cce452b3661b21f386418a257883b30a"
    return hashlib.sha256(user_input.encode()).hexdigest() == secret_hash

def display_board(board):
    print(" | ".join(board[0:3]) + "      " + "1|2|3")
    print(" | ".join(board[3:6]) + "      " + "4|5|6")
    print(" | ".join(board[6:9]) + "      " + "7|8|9")
    print()

def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != "-":
            return board[a]
    return None

def player_move(board, player):
    move = input(f"Player {player}, choose position (1-9): ").strip()
    while not (move.isdigit() and int(move) in range(1, 10) and board[int(move)-1] == "-"):
        move = input("Invalid move. Choose a free position (1-9): ").strip()
    board[int(move)-1] = player

def minimax(board, depth, is_maximizing, comp, human):
    winner = check_winner(board)
    if winner == comp:
        return 1
    elif winner == human:
        return -1
    elif "-" not in board:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == "-":
                board[i] = comp
                score = minimax(board, depth + 1, False, comp, human)
                board[i] = "-"
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == "-":
                board[i] = human
                score = minimax(board, depth + 1, True, comp, human)
                board[i] = "-"
                best_score = min(score, best_score)
        return best_score

def computer_move(board, comp, human):
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == "-":
            board[i] = comp
            score = minimax(board, 0, False, comp, human)
            board[i] = "-"
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = comp
    print(f"Computer chose position {best_move + 1}")

def play_normal_mode():
    board = ["-"] * 9
    user_input = input("Choose your symbol (X or O) or ask for help (HELP): ").upper().strip()
    if is_secret_input(user_input):
        play_secret_mode()
        return

    while user_input not in ("X", "O"):
        if user_input == "HELP":
            print(f"In Satan's grasp, the lost must tread,\nWhere hollow paths leave SECRETs unsaid.\nBut seal the cracks, let none remain,\nAnd glimpse what writhes beyond the flame.\n")
            user_input = input("Choose your symbol (X or O) or ask for help (HELP): ").upper().strip()
        else:
            user_input = input("Invalid input. Please choose X or O: ").upper().strip()
    player = user_input
    comp = "O" if player == "X" else "X"
    print(f"You are {player}. Computer is {comp}.\n")
    display_board(board)

    if player == "O":
        computer_move(board, comp, player)
        display_board(board)

    while True:
        player_move(board, player)
        display_board(board)
        if (winner := check_winner(board)):
            if winner == player:
                print("Congratulations, you won!")
            else:
                print("Computer wins!")
            break
        if "-" not in board:
            print("It's a tie!")
            break

        computer_move(board, comp, player)
        display_board(board)
        if (winner := check_winner(board)):
            if winner == player:
                print("Congratulations, you won!")
            else:
                print("Computer wins!")
            break
        if "-" not in board:
            print("It's a tie!")
            break

def play_secret_mode():
    board = ["-"] * 9
    print("\nSecret Mode Activated!")
    symbol = input("Choose your symbol (X or O): ").upper().strip()
    while symbol not in ("X", "O"):
        symbol = input("Invalid input. Please choose X or O: ").upper().strip()
    
    print("Player1 is " +  symbol + ", Player2 is " + ("O" if symbol == "X" else "X"))
    display_board(board)
    
    while True:
        moves = input("Player " + symbol + ", enter cell numbers (or type 'exit' to quit): ").strip()
        if moves.lower() == "exit":
            print("Exiting secret mode.")
            break
        
        for move in moves.split():
            if move.isdigit() and int(move) in range(1, 10):
                idx = int(move) - 1
                if board[idx] == "-":
                    board[idx] = symbol
                else:
                    print(f"Cell {move} is already filled.")
            else:
                print(f"Invalid input: {move}")
        display_board(board)
        
        if all(cell == symbol for cell in board):
            try:
                print("Congratulations, here is your flag: " + flag)
            except Exception as e:
                print("Error reading flag.")
            break
        elif all(cell != "-" for cell in board):
            print("Well... Now what?")
            break

        symbol = "X" if symbol == "O" else "O"

def main():
    print(f"This wasn't how I imagined hell to be... oh well, at least we can play something!\n")
    play_normal_mode()

if __name__ == "__main__":
    main()
