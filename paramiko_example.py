import paramiko
ssh: paramiko.SSHClient = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ips: list[str]  = ["192.168.89.1"]
resp: list[str] = []
for ip in ips:
    #подключается по ssh
    ssh.connect(ip, 
           username='user', 
           password='1234',
           look_for_keys=False,
           allow_agent=False,
           timeout=10)
    # вводит команду и иохраняет stdin, stdout, stderr
    stdin, stdout, stderr = ssh.exec_command('/system resource print')
    resp.append(stdout.read().decode('utf-8', errors='ignore'))
    ssh.close()

for i in resp:
    print(i)