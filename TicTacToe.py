board = [" " for _ in range(9)]

def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False

def game():
    player = "X"
    moves = 0

    while True:
        print_board()
        choice = int(input(f"Player {player}, choose position (1-9): ")) - 1

        if board[choice] != " ":
            print("Position already taken! Try again.")
            continue

        board[choice] = player
        moves += 1

        if check_winner(player):
            print_board()
            print(f"🎉 Player {player} wins!")
            break

        if moves == 9:
            print_board()
            print("😐 It's a Draw.")
            break

        player = "O" if player == "X" else "X"

game()