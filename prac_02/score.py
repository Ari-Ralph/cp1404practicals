"""
CP1404 - Practical 02
Ari Ralph
Program to determine score status
"""


def main():
    """Print result from an inputted score"""
    score = float(input("Enter score: "))
    result = get_result(score)
    print(f"The result for a score of {score} is {result}")


def get_result(score: float) -> str:
    """Determine the result from a given score"""
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
