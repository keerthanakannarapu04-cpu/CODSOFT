import random

board = [" " for _ in range(9)]

def display():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False

while True:
    display()

    move = int(input("Enter position (0-8): "))

    if board[move] == " ":
        board[move] = "X"

    if winner("X"):
        display()
        print("You Win!")
        break

    available = [i for i in range(9) if board[i] == " "]

    if not available:
        print("Draw!")
        break

    ai_move = random.choice(available)
    board[ai_move] = "O"

    if winner("O"):
        display()
        print("AI Wins!")
        break
