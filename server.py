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
subprocess.run('docker-compose up -d --scale worker=4', shell=True)
for i, worker in enumerate(workers):
    port = subprocess.run(f'docker port {worker}', shell=True, capture_output=True, text=True)
    if port.returncode == 0:
        port = port.stdout.splitlines()
        portString = port[0]
        portIndex = portString.find(':')
        port = portString[(portIndex + 1):]
        print(port)
    with open(f'segment_{i+1}.txt', 'rb') as file:
        file = {'file' : file}
        try:
            response = requests.post(f'http://localhost:{port}/process', files=file, timeout=10)  # Adjust timeout value as needed
        # Process the response...
        except requests.exceptions.Timeout:
            print("Request timed out. Check the server's responsiveness.")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

            output_response = requests.get(f'http://localhost:{port}/get_output')
            if output_response.status_code == 200:
                with open('received_output.txt', 'wb') as output_file:
                    output_file.write(output_response.content)
                print("Output file received successfully")
            else:
                print("Failed to receive output file")
    
#subprocess.run('docker-compose down -d')