#@AUTHOR NATHANAEL WOLSKI
#@AUTHOR NOAH DANIELS
#UI
import requests
import subprocess
import json
from textSegmentation import textSegmentation

segments = textSegmentation()
workers = ['327-semester-project-worker-1','327-semester-project-worker-2','327-semester-project-worker-3','327-semester-project-worker-4']
pattern = input('What would you like to search for? (enter a word or phrase)')
#write the user's chosen search to a text file
with open('pattern.txt', 'w') as file:
    file.write(f"{pattern}\n")
#start the containers that will process the text file
subprocess.run('docker-compose up -d --scale worker=4', shell=True)
#get the ip range of the containers
ip = subprocess.run('docker network inspect 327-semester-project_my_network', shell=True, capture_output=True, text=True)
json_data = json.loads(ip.stdout)
ip_addresses =[]
# Search for IP addresses within the dictionary
for network in json_data:
    # Access 'Containers' or 'IPAM' fields where IP addresses might be stored
    containers = network.get('Containers', {})
    for container_id, container_info in containers.items():
        # Extract IP addresses associated with containers
        ipv4_address = container_info.get('IPv4Address', "")
        if ipv4_address:
            ip_addresses.append(ipv4_address)
    
print(ip_addresses)
#loop through list of container names
for i, worker in enumerate(workers):
    #get the exposed port of each container
    port = subprocess.run(f'docker port {worker}', shell=True, capture_output=True, text=True)
    #check if the command executed successfully
    if port.returncode == 0:
        port = port.stdout.splitlines()
        portString = port[0]
        portIndex = portString.find(':')
        port = portString[(portIndex + 1):]
    #read each file containing a segment of the original text file
    with open(f'segment_{i}.txt', 'rb') as file:
        file = {'file' : file}
        try:
            #send a request to the containers
            response = requests.post(f'http://{ip_addresses[3-i]}:{port}/process', files=file, timeout=20)  # Adjust timeout value as needed
        # Process the response...
        except requests.exceptions.Timeout:
            print("Request timed out. Check the server's responsiveness.")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            #request results from the containers
            output_response = requests.get(f'http://localhost:{port}/get_output')
            #check for a successful request
            if output_response.status_code == 200:
                with open('received_output.txt', 'wb') as output_file:
                    output_file.write(output_response.content)
                print("Output file received successfully")
            else:
                print("Failed to receive output file")
    
