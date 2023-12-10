#split the text
def textSegmentation():
    numProcesses = 4
    with open('testText.txt', 'r') as file: #only access to the original text file
        text = file.read()
    segSize = len(text) // numProcesses
    segments =[]
    for i in range(numProcesses):
        start = i * segSize
        end = start + segSize if i < numProcesses - 1 else len(text)
        segments.append(text[start:end])

    for i, segment in enumerate(segments):
        filename = f'segment_{i}.txt'
        with open(filename, 'w') as file:
            file.write(segment)