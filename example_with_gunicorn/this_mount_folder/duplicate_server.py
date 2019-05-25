import datetime
import os, sys
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_PATH)
import time
import paramiko
from scripts.main import main


server = {}
with open(os.path.join(PROJECT_PATH, 'server_parameters.txt')) as f:
    for line in f:
       (key, val) = line[:-1].split(';')
       server[key] = val


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(server['host'], username=server['username'], password=server['key_phrase'], key_filename=server['private_key'])

while True:
    try:
        _, stdout, _ = ssh.exec_command('ps -ef | grep python')
        processes_python = stdout.readlines()

        _, stdout, _ = ssh.exec_command('cat /home/dmitryhse/AutoSelfie_bot/data/PID.txt')
        PID = stdout.readlines()[0]
        all_PID = [" ".join(process.split()).split(' ')[1] for process in processes_python]
        if PID in all_PID:
            time.sleep(5)
        else:
            raise Exception
    except:
        print('Process or Server died!', datetime.datetime.now())
        break
ssh.close()
main()



