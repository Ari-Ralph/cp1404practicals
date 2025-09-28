"""
CP1404 - Practical 02
Ari Ralph
Program to determine score status.
"""
import random


def main():
    """Print result from an inputted score and a random score."""
    inputted_score = float(input("Enter score: "))
    inputted_score_result = get_result(inputted_score)
    print(f"The result for a score of {inputted_score} is {inputted_score_result}.")
    random_score = random.uniform(0, 100)
    random_score_result = get_result(random_score)
    print(f"The result for a random score of {random_score:.2f} is {random_score_result}.")


def get_result(score: float) -> str:
    """Determine the result from a given score."""
    if score < 0 or score > 100:
        return "invalid"
    elif score >= 90:
        return "excellent"
    elif score >= 50:
        return "passable"
    else:
        return "bad"


main()
