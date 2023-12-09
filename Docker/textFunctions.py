#methods in the containers that do work
import re

def pattern_match(text, pattern):
    matches = re.findall(pattern, text)
    return len(matches), matches

def word_count(text):
    words = text.split()
    return len(words)

if __name__ is "__main__":
    with open('/app/input.txt', 'r') as file:
        text = file.read()
    with open('/app/pattern.txt', 'r') as file:
        pattern = file.read()

    numMatches, matches = pattern_match(text, pattern)
    numWords = word_count(text)

    with open('/app/output.txt', 'w') as file:
        file.write(f"Number of matches: {numMatches}\n")
        file.write(f"Matches found: {matches}\n")
        file.write(f"Word count: {numWords}\n")