"""
CP1404 - Practical 1
by Ari Ralph
Created: 13/09/25
Last Edited: 16/09/2025
Menus
"""

MENU = """(H)ello
(G)oodbye
(Q)uit"""

name = input("Enter name: ")

print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()

print("Finished.")
