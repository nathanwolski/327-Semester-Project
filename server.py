#UI
import subprocess
from dockerController import startDocker
from textSegmentation import textSegmentation

numProcesses = input('How many segmentations would you like?')
segments = textSegmentation(numProcesses)
pattern = input('What would you like to search for? (enter a word or phrase)')
with open('pattern.txt', 'w') as file:
    file.write(f"{pattern}\n")
startDocker(segments)
for i in range(segments):
    subprocess.run(f"docker exec container_{i} python3 textFunctions.py")
print
