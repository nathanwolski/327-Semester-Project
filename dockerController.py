#create containers
import subprocess

numProcesses = 4
def startDocker(segments):
    for i, segment in enumerate(segments):
        subprocess.run(f"docker run -d --name container_{i} textProcessing", shell = True, check = True)
        subprocess.run(f"docker exec container_{i} sh -c 'echo \"segment\" > /app/xxxxxxx'", shell = True, check = True)