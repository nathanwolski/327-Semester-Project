#split the text
def textSegmentation(numProcesses):
    with open('testText.txt', 'r') as file: #only access to the original text file
        text = file.read()
    segSize = len(text) // numProcesses
    segments =[]
    for i in range(numProcesses):
        start = i * segSize
        end = start + segSize if i < numProcesses - 1 else len(text)
        segments.append(text[start:end])
    return segments