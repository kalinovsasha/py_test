import paramiko

#  Настройки
USERNAME = 'user'
PASSWORD = 'password'
COMMAND_backup = 'system backup save dont-encrypt=yes name=test'
COMMAND_rsc = 'export file=test'
# Массив Микротиков
ROUTERS = ['192.168.1.1', '192.168.1.2']


def create_backup(ip: str, username, password, comand):
    #  Подключение
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, username=username, password=password, timeout=15)
        _, stdout, _ = ssh.exec_command(comand)
        # Если не нужно логировать вывод из консоли
        # output = stdout.read().decode().strip()
    except paramiko.AuthenticationException:
        print("Ошибка аутентификации. Проверьте учетные данные.")
    except Exception as e:
        print(f"Ошибка соединения или выполнения: {e}")
    finally:
        # 4. Закрытие соединения
        if 'ssh' in locals():
            ssh.close()
            print("Соединение закрыто.")


# Создание бекапа в формате бекапа
for ip in ROUTERS:
    create_backup(ip, USERNAME, PASSWORD, COMMAND_backup)

# Создание бекапа в формате rsc
for ip in ROUTERS:
    create_backup(ip, USERNAME, PASSWORD, COMMAND_rsc)
