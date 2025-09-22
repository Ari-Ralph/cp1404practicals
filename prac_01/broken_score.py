"""
CP1404 - Practical 1
by Ari Ralph
Created: 13/09/25
Last Edited: 16/09/2025
Broken program to determine score status
"""

score = float(input("Enter score: "))

if 100 < score or score < 0:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
