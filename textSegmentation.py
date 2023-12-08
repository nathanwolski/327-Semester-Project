#split the text
with open('/app/xxxxxx', 'r') as file:
    text = file.read()
numProcesses = 4
segSize = len(text) // numProcesses
segments =[]
for i in range(numProcesses):
    start = i * segSize
    end = start + segSize if i < numProcesses - 1 else len(text)
    segments.append(text[start:end])