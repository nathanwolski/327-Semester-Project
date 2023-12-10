#@AUTHOR NATHANAEL WOLSKI
#@AUTHOR NOAH DANIELS
#methods in the containers that do work
from flask import Flask, request
import os

app = Flask(__name__)
#finds the users chosen search parameters in the input file
def pattern_match(text, pattern):
    matches = text.findall(pattern)
    return len(matches), matches
#counts the words in the input file
def word_count(text):
    words = text.split()
    return len(words)

@app.route('/process', methods=['POST'])
#receives request and performs pattern matching and word counting before writing the results to an output file
def processText():
    #gets text file from request
    segment = request.files['file']
    #reads text file
    with open('/app/pattern.txt', 'r') as file:
        pattern = file.read()
    numMatches, matches = pattern_match(segment, pattern) #method
    numWords = word_count(segment) #method
    #writes the results to an output file
    with open('/app/output.txt', 'w') as file:
        file.write(f"Number of matches: {numMatches}\n")
        file.write(f"Matches found: {matches}\n")
        file.write(f"Word count: {numWords}\n")

@app.route('/get_output', methods=['GET'])
#sends output out on request
def get_output():
    return Flask.send_file('/app/output.txt', as_attachment=True)

if __name__ == "__main__":
    port = int(os.getenv('SERVICE_PORT', '5000'))  # Default port is 8080 if not specified
    #listening on the port designated by docker composition file
    app.run(host='localhost', port=port)