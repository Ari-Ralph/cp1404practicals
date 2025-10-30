"""
CP1404 - Practical 05
Word Occurrences
Estimate: 40 minutes
Actual: 9 minutes 26 seconds
"""

text_words = sorted(input("Text: ").lower().split())
word_to_count = {}
for word in text_words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

word_spacing = max(len(word) for word in text_words)
for word in word_to_count:
    print(f"{word:{word_spacing}} : {word_to_count[word]}")
