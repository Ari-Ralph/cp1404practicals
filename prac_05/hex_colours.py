"""
CP1404 - Practical 05
Colour names to hex codes in a dictionary
"""

NAMES_TO_HEX_CODES = {"cerulean": "	#007ba7", "chartreuse": "#7fff00", "vermillion": "#e34234", "zomp": "#39a78e",
                      "viridian": "#40826d", "ultramarine": "#3f00ff", "tyrian purple": "#66023c",
                      "timberwolf": "#dbd7d2", "tumbleweed": "#deaa88", "volt": "#ceff00"}

name = input("Enter colour name: ").lower()
while name != "":
    try:
        print(NAMES_TO_HEX_CODES[name])
    except KeyError:
        print("Invalid colour name")
    name = input("Enter colour name: ").lower()
