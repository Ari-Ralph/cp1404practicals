"""
CP1404 - Practical 05
Email Program
Estimate: 30 minutes
Actual: 23 minutes
"""


def main():
    """Store emails and names in a dictionary and print dictionary items once loop is complete."""
    email = input("Email: ")
    email_to_name = {}
    while email != "":
        name = determine_name_from_email(email)
        is_name_correct = input(f"Is your name {name}? (Y/n) ").upper()
        if is_name_correct != "Y" and is_name_correct != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def determine_name_from_email(email):
    """Determine a possible name from the name in the email address."""
    name = " ".join(email.split('@')[0].title().split('.'))
    return name


main()
