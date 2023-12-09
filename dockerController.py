#create containers
import subprocess

def startDocker(segments):
    for i, segment in enumerate(segments):
        subprocess.run(f"docker run -d --name container_{i} --network mynetwork -v shared_data:/data text-processing", shell = True, check = True)
        subprocess.run(f"docker exec container_{i} sh -c 'echo \"{segment}\" > /app/input.txt'", shell = True, check = True)