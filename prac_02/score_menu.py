"""
CP1404 - Practical 02
Menu-based score status program
"""

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    """Get valid score, then print menu and get user input"""
    score = float(input("Score: "))
    print(MENU)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            #TODO get valid score
            pass
        elif choice == "P":
            #TODO print result
            pass
        elif choice == "S":
            #TODO print number of stars
            pass
        else:
            print("Invalid choice")
        print()
        print(MENU)
        choice = input("> ").upper()
    print("Farewell")


main()