#split the text
def textSegmentation(numProcesses):
    #need to change file
    with open('file.txt', 'r') as file:
        text = file.read()
    segSize = len(text) // numProcesses
    segments =[]
    for i in range(numProcesses):
        start = i * segSize
        end = start + segSize if i < numProcesses - 1 else len(text)
        segments.append(text[start:end])
    return segments