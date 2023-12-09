#UI
import subprocess
from output import getOutput
from textSegmentation import textSegmentation

numProcesses = int(input('How many segmentations would you like?'))
segments = textSegmentation(numProcesses)
pattern = input('What would you like to search for? (enter a word or phrase)')
with open('pattern.txt', 'w') as file:
    file.write(f"{pattern}\n")
for i in range(segments):
    subprocess.run(f"docker exec container_{i} python3 textFunctions.py")
print(getOutput())
