import paramiko
import time
from tqdm import tqdm

myusername = 'endless'
portnumber = '4200'
mypassword = 'endless1234'
rebootwaittime = 600

def execute_command(ssh, command):
    print(command)
    stdin, stdout, stderr = ssh.exec_command(command, get_pty=True)
    total_size = None
    pbar = None

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

if __name__ == '__main__':

    myusername = input("username : ")
    portnumber = input('portnumber : ')
    mypassword = input("password : ")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#install drivers
    ssh.connect('162.157.113.207', port = int(portnumber), username=myusername, password=mypassword)
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S apt update')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S apt upgrade')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S apt install nvidia-driver-525')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S modprobe -r nvidia_drm')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S modprobe -r nvidia_modeset')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S modprobe -r nvidia_uvm')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S modprobe -r nvidia')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S modprobe nvidia')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S modprobe nvidia_uvm')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S modprobe nvidia_modeset')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S modprobe nvidia_drm')
    
 
    execute_command(ssh, 'wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600')
    execute_command(ssh, 'wget https://developer.download.nvidia.com/compute/cuda/12.1.1/local_installers/cuda-repo-ubuntu2204-12-1-local_12.1.1-530.30.02-1_amd64.deb')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S dpkg -i cuda-repo-ubuntu2204-12-1-local_12.1.1-530.30.02-1_amd64.deb')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S cp /var/cuda-repo-ubuntu2204-12-1-local/cuda-*-keyring.gpg /usr/share/keyrings/')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S apt-get update')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S apt-get -y install cuda')
    execute_command(ssh, 'source ~/.bashrc')

    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S apt update')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S apt install npm -y')
    execute_command(ssh, 'npm install pm2 -g')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S  -u endless env PATH=$PATH:/usr/local/cuda/bin CUDA_HOME=/usr/local/cuda pip install git+https://github.com/opentensor/cubit.git@v1.1.2')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S apt install python3')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S apt update')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S apt install python3-pip -y')

    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S apt update')
    execute_command(ssh, 'git clone https://github.com/commune-ai/commune.git')
    execute_command(ssh, 'cd commune/')
    execute_command(ssh, 'pip install -e .')
    execute_command(ssh, 'commune sync')
    execute_command(ssh, 'cd ..')

    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S apt update')
    execute_command(ssh, 'pip install bittensor')

    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S apt update')
    execute_command(ssh, 'sudo -u ' + myusername + ' env PATH=$PATH:/usr/local/cuda/bin CUDA_HOME=/usr/local/cuda pip install git+https://github.com/GithubRealFan/cubit.git')
    execute_command(ssh, 'echo "' + mypassword + '" | sudo -S reboot')

    ssh.close()

input("Done!, Press Enter to Exit......")