#UI
import requests
import subprocess
import json
from output import getOutput
from textSegmentation import textSegmentation

segments = textSegmentation()
workers = ['327-semester-project-worker-1','327-semester-project-worker-2','327-semester-project-worker-3','327-semester-project-worker-4']
pattern = input('What would you like to search for? (enter a word or phrase)')
with open('pattern.txt', 'w') as file:
    file.write(f"{pattern}\n")
subprocess.run('docker-compose up -d --scale worker=4', shell=True)
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
for i, worker in enumerate(workers):
    port = subprocess.run(f'docker port {worker}', shell=True, capture_output=True, text=True)
    if port.returncode == 0:
        port = port.stdout.splitlines()
        portString = port[0]
        portIndex = portString.find(':')
        port = portString[(portIndex + 1):]

    with open(f'segment_{i}.txt', 'rb') as file:
        file = {'file' : file}
        try:
            response = requests.post(f'http://{ip_addresses[3-i]}:{port}/process', files=file, timeout=20)  # Adjust timeout value as needed
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
    
