#UI

from dockerController import startDocker
from textSegmentation import textSegmentation

numProcesses = input('How many segmentations would you like?')
segments = textSegmentation(numProcesses)
startDocker(segments)

