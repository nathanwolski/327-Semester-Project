#methods in the containers that do work
from flask import Flask, request
import os

app = Flask(__name__)

def pattern_match(text, pattern):
    matches = text.findall(pattern)
    return len(matches), matches

def word_count(text):
    words = text.split()
    return len(words)

@app.route('/process', methods=['POST'])
def processText():
    segment = request.files['file']
    with open('/app/pattern.txt', 'r') as file:
        pattern = file.read()
    numMatches, matches = pattern_match(segment, pattern)
    numWords = word_count(segment)
    with open('/app/output.txt', 'w') as file:
        file.write(f"Number of matches: {numMatches}\n")
        file.write(f"Matches found: {matches}\n")
        file.write(f"Word count: {numWords}\n")

@app.route('/get_output', methods=['GET'])
def get_output():
    return Flask.send_file('/app/output.txt', as_attachment=True)

if __name__ == "__main__":
    port = int(os.getenv('SERVICE_PORT', '5000'))  # Default port is 8080 if not specified
    app.run(host='localhost', port=port)