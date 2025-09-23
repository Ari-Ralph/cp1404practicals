"""
CP1404 - Practical 02
Menu-based score status program
"""

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Get valid score, then print menu and get user input"""
    score = get_valid_score()
    print(MENU)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            # TODO print result
            pass
        elif choice == "S":
            # TODO print number of stars
            pass
        else:
            print("Invalid choice")
        print()
        print(MENU)
        choice = input("> ").upper()
    print("Farewell")


def get_valid_score():
    score = float(input("Score: "))
    while 0 > score or score > 100:
        print("Invalid score")
        score = float(input("Score: "))
    return score


main()
