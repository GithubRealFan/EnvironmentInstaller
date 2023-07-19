import subprocess

def run_bito(input_text):
    command = ['bito']
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate(input_text.encode())
    output = stdout.decode().strip()
    return output

# Example usage
input_prompt = input("InputText: ")
output = run_bito(input_prompt)
print(output)
