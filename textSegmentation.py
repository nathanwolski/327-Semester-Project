#@AUTHOR NATHANAEL WOLSKI
#@AUTHOR NOAH DANIELS
#split the text into segments
def textSegmentation():
    numProcesses = 4
    #read the text file
    with open('testText.txt', 'r') as file: #only access to the original text file
        text = file.read()
    segSize = len(text) // numProcesses
    segments =[]
    #split the text file into equal amounts and storing them in an arrray
    for i in range(numProcesses):
        start = i * segSize
        end = start + segSize if i < numProcesses - 1 else len(text)
        segments.append(text[start:end])
    #write the results into seperate text files
    for i, segment in enumerate(segments):
        filename = f'segment_{i}.txt'
        with open(filename, 'w') as file:
            file.write(segment)