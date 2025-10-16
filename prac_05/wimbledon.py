"""
CP1404 - Practical 05
Wimbledon Program
Estimate: 1 hour
Actual:
"""
FILENAME = "wimbledon.csv"


def main():
    """Load and process Wimbledon champion data."""
    champion_data = load_champion_data()
    champion_name_to_number_of_wins = generate_champion_name_to_win_count(champion_data)
    winner_countries = determine_countries_of_winners(champion_data)
    print("Wimbledon Champions:")
    for name, number_of_wins in champion_name_to_number_of_wins.items():
        print(name, number_of_wins)
    print()
    print(f"These {len(winner_countries)} countries have won Wimbledon:")
    print(", ".join(sorted(winner_countries)))


def load_champion_data():
    """Read csv file to create nested list of champion data."""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        champion_data = []
        in_file.readline()  # skip header
        for line in in_file:
            champion_country_and_name = line.strip().split(',')[1:3]
            champion_data.append(champion_country_and_name)
    return champion_data


def generate_champion_name_to_win_count(champion_data):
    """Count number of wins for each player creating a dictionary."""
    champion_to_win_count = {}
    for champion in champion_data:
        champion_to_win_count[champion[1]] = champion_to_win_count.get(champion[1], 0) + 1
    return champion_to_win_count


def determine_countries_of_winners(champion_data):
    """Create set of countries whose players have been champion."""
    winner_countries = set()
    for champion in champion_data:
        winner_countries.add(champion[0])
    return winner_countries


main()
