#managing output
import subprocess

def getOutput():
    results = []
    for i in range(4):
        output = subprocess.check_output(f"docker exec container_{i} cat /app/xxxxxx", shell = True)
        results.append(output.decode().strip())
    return results