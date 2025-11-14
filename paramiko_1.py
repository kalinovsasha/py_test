import paramiko

ssh: paramiko.SSHClient = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

resp: str = ''
#подключается по ssh
ssh.connect("192.168.89.1", 
        username='', 
        password='',
        look_for_keys=False,
        allow_agent=False,
        timeout=10)
# вводит команду и и cохраняет stdin, stdout, stderr
stdin, stdout, stderr = ssh.exec_command('/system resource print')
resp = stdout.read().decode('utf-8', errors='ignore')
ssh.close()

print(resp)