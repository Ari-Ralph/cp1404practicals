"""
CP1404 - Practical 02
Ari Ralph
Menu-based score status program
"""

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Score program with menu function"""
    score = get_valid_score()
    print(MENU)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"The result for a score of {score} is {result}.")
        elif choice == "S":
            print_asterisks(score)
        else:
            print("Invalid choice")
        print()
        print(MENU)
        choice = input("> ").upper()
    print("Farewell")


def get_valid_score():
    """Get a score between 0 and 100"""
    score = float(input("Score: "))
    while 0 > score or score > 100:
        print("Invalid score")
        score = float(input("Score: "))
    return score


def determine_result(score: float) -> str:
    """Determine the result from a given score"""
    if score >= 90:
        return "excellent"
    elif score >= 50:
        return "passable"
    else:
        return "bad"


def print_asterisks(length: float) -> None:
    """Print line of asterisks equal to length, rounded down"""
    print("*" * int(length))


main()
