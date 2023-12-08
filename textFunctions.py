#methods that do work
import re

def pattern_match(text, pattern):
    matches = re.findall(pattern, text)
    return len(matches), matches

def word_count(text):
    words = text.split()
    return len(words)

if __name__ is "__main__":
    with open('/app/xxxxxx', 'r') as file:
        text = file.read()

    pattern = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'
    numMatches, matches = pattern_match(text, pattern)
    numWords = word_count(text)

    with open('/app/xxxxxxx', 'w') as file:
        file.write(f"Number of matches: {numMatches}\n")
        file.write(f"Matches found: {matches}\n")
        file.write(f"Word count: {word_count}\n")