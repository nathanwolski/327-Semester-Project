#UI
import requests
import subprocess
from output import getOutput
from textSegmentation import textSegmentation

segments = textSegmentation()
workers = ['327-semester-project-worker-1','327-semester-project-worker-2','327-semester-project-worker-3','327-semester-project-worker-4']
pattern = input('What would you like to search for? (enter a word or phrase)')
with open('pattern.txt', 'w') as file:
    file.write(f"{pattern}\n")
subprocess.run('docker-compose up --scale worker=4', shell=True)
for i, worker in enumerate(workers):
    with open(f'segment_{i+1}.txt', 'rb') as file:
        file = {'file' : file}
        response = requests.post(f'http://{worker}:80/process', files=file)

        if response.status_code == 200:
            print("File sent successfully")
            output_response = requests.get(f'{worker}/get_output')
            if output_response.status_code == 200:
                with open('received_output.txt', 'wb') as output_file:
                    output_file.write(output_response.content)
                print("Output file received successfully")
            else:
                print("Failed to receive output file")
        else:
            print("Failed to send file")
    
