import paramiko
import time
import socket
from tqdm import tqdm

myusername = 'endless'
portnumber = '4200'
mypassword = 'endless1234'
rebootwaittime = 600


def execute_command(ssh, command, password=None, temp_dir=None):
    if temp_dir is not None:
        command = f'TMPDIR={temp_dir} {command}'
    print(command)
    stdin, stdout, stderr = ssh.exec_command(command, get_pty=True)
    total_size = None
    pbar = None

    if password is not None:
        stdin.write(password + '\n')
        stdin.flush()

    while not stdout.channel.exit_status_ready():
        if stdout.channel.recv_ready():
            output = stdout.channel.recv(1024).decode('utf-8')
            print(output, end='')

        if stderr.channel.recv_stderr_ready():
            error = stderr.channel.recv_stderr(1024).decode('utf-8')
            print(error, end='')

    if pbar is not None:
        pbar.close()

    print('\n')

def connect_ssh(host, port, username, password, timeout=10):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    while True:
        try:
            ssh.connect(host, port=port, username=username, password=password, timeout=timeout)
            print("SSH connection established.")
            break
        except (paramiko.SSHException, socket.timeout, paramiko.ssh_exception.NoValidConnectionsError, TimeoutError) as e:
            print("SSH connection failed. Retrying in 30 seconds...")
            time.sleep(30)

    return ssh


if __name__ == '__main__':

    myusername = input("User Name : ")
    myip = input("IP Address: ")
    portnumber = input('Port : ')
    mypassword = input("Password : ")

    ssh = connect_ssh(myip, int(portnumber), myusername, mypassword)
#install drivers
    ssh.connect(myip, port = int(portnumber), username=myusername, password=mypassword)
    execute_command(ssh, 'sudo -S apt -y update', mypassword)
    execute_command(ssh, 'sudo -S apt -y upgrade', mypassword)
    execute_command(ssh, 'sudo -S apt install nvidia-driver-470', mypassword)
    execute_command(ssh, 'sudo -S reboot', mypassword)
    ssh = connect_ssh(myip, int(portnumber), myusername, mypassword)
 
    execute_command(ssh, 'sudo -S wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin', mypassword)
    execute_command(ssh, 'sudo -S mv cuda-ubuntu2004.pin /etc/apt/preferences.duda-repository-pin-600', mypassword)

    file_url="https://developer.download.nvidia.com/compute/cuda/12.1.1/local_installers/cuda-repo-ubuntu2004-12-1-local_12.1.1-530.30.02-1_amd64.deb"
    file_name="cuda-repo-ubuntu2004-12-1-local_12.1.1-530.30.02-1_amd64.deb"
    execute_command(ssh, f'[ ! -f "{file_name}" ] &&  sudo -S wget "{file_url}" || echo "File {file_name} already exists. Skipping download."', mypassword)

    execute_command(ssh, 'sudo -S dpkg -i cuda-repo-ubuntu2004-12-1-local_12.1.1-530.30.02-1_amd64.deb', mypassword)
    execute_command(ssh, 'sudo -S cp /var/cudapo-ubuntu2004-12-1-local/cuda-*-keyring.gpg /usr/share/keyrings/', mypassword)
    execute_command(ssh, 'sudo -S apt-get -y update', mypassword)
    execute_command(ssh, 'sudo -S apt-get -y install cuda', mypassword)
    execute_command(ssh, 'sudo -S reboot', mypassword)
    ssh = connect_ssh(myip, int(portnumber), myusername, mypassword)

    execute_command(ssh, 'sudo -S apt update', mypassword)
    execute_command(ssh, 'sudo -S apt install npm -y', mypassword)
    execute_command(ssh, 'sudo -S npm install pm2 -', mypassword)
    execute_command(ssh, 'sudo -S  -u endless env PATH=$PATH:/usr/local/cuda/bin CUDA_HOME=/usr/local/cuda pip install git+https://github.com/opentensor/cubit.git@v1.1.2', mypassword)
    execute_command(ssh, 'sudo -S apt install python3', mypassword)
    execute_command(ssh, 'sudo -S apt update', mypassword)
    execute_command(ssh, 'sudo -S apt install python3-pip -y', mypassword)

    execute_command(ssh, 'sudo -S apt update', mypassword)
    execute_command(ssh, 'git clone https://github.com/commune-ai/commune.git')
    execute_command(ssh, 'cd commune/')
    execute_command(ssh, 'sudo -S make install', mypassword)
    execute_command(ssh, 'commune sync')
    execute_command(ssh, 'cd ..')

    execute_command(ssh, 'sudo -S apt update', mypassword)
    file_url="https://files.pythonhosted.org/packages/6b/0e/c640bda79e61766896fe16dfe0a3ab12b06ad50cf8814950518896dec0a5/torch-1.13.1-cp38-cp38-manylinux1_x86_64.whl"
    file_name="torch-1.13.1-cp38-cp38-manylinux1_x86_64.whl"
    execute_command(ssh, f'[ ! -f "{file_name}" ] &&  sudo -S wget "{file_url}" || echo "File {file_name} already exists. Skipping download."', mypassword)

    execute_command(ssh, 'pip install torch-1.13.1-cp38-cp38-manylinux1_x86_64.whl')
    execute_command(ssh, 'pip install bittensor')

    execute_command(ssh, 'sudo -S apt update', mypassword)
    execute_command(ssh, 'sudo -u ' + myusername + ' env PATH=$PATH:/usr/local/cuda/bin CUDA_HOME=/usr/local/cuda pip install git+https://github.com/GithubRealFan/simple.git', mypassword)
    execute_command(ssh, 'sudo -S reboot', mypassword)

    ssh.close()

input("Done!, Press Enter to Exit......")