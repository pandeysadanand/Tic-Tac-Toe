"""
    @Author: SADANAND PANDEY
    @Date: 2022-06-17 19:30:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-17 19:35:00
    @Title : Add multiple Address Book to the System. Each Address Book has a unique Name

"""


def print_board(a):
    """
    printing game bord
    Args:
        a: list a

    Returns: none

    """
    print("", a[1], " │", a[2], " │ ", a[3], " ")
    print("────┼────┼────")
    print("", a[4], " │", a[5], " │ ", a[6], " ")
    print("────┼────┼────")
    print("", a[7], " │", a[8], " │ ", a[9], " ")


def print_instructions():
    """
    for display the instruction of game
    Returns:  flag

    """
    print("\n----------- WELCOME TO TIC TAC TOE ------------\n")
    print_board(pos)
    print()

    players[0] = input("Player 1 : ")
    players[1] = input("Player 2 : ")

    print(players[0], "you will using X")
    print(players[1], "you will using 0")

    print("Turn starts from", players[0])

    print("\nPotisions are like :-")
    print("  1 │  2 │ 3  ")
    print("────┼────┼────")
    print("  4 │  5 │ 6  ")
    print("────┼────┼────")
    print("  7 │  8 │ 9  ")

    print("Press S to start the game")
    flag = input()
    return flag


def start_game():
    """
        Here game is starting
    Returns: none

    """
    turn = 0
    for i in range(9):
        if turn % 2 == 0:
            print("\n", players[0], "Turn : ")
            p = int(input("Please Enter position : "))
            v = 'x'
            if pos[p] == ' ':
                pos[p] = v
                print(pos)
                print_board(pos)
                winner = check_win(v)
                if winner == "nobody":
                    turn = 1
                    continue
                else:
                    print("\n\n", players[0], "you win !!")
                    break
            else:
                print("Please select right position")
        else:
            print("\n", players[1], "turns : ")
            p = int(input("Please Enter position : "))
            v = '0'
            if pos[p] == ' ':
                pos[p] = v
                print(pos)
                print_board(pos)
                winner = check_win(v)
                if winner == "nobody":
                    turn = 0
                    continue
                else:
                    print("\n\n", players[1], "you win !!")
                    break
            else:
                print("Please select right position")
    else:
        print("\n\nGame is Tie")


def check_win(v):
    """
        checking for winner
    Args:
        v: this is position of player

    Returns: winner

    """
    for i in winning_conditions:
        if (pos[i[0]], pos[i[1]], pos[i[2]]) == (v, v, v):
            winner = players[0]
            break
        elif (pos[i[0]], pos[i[1]], pos[i[2]]) == (v, v, v):
            winner = players[1]
            break
    else:
        winner = "nobody"
    return winner


if __name__ == '__main__':
    # to save position of player
    pos = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    # to save player
    players = ['', '']

    # to check winning position
    winning_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

    # calling function to take player
    flag = print_instructions()
    if flag == 's' or flag == 'S':
        start_game()
    else:
        print("Invalid Entry")
