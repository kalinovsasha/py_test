import paramiko
import datetime

# --- Настройки подключения ---
hosts = ['192.168.1.1', '192.168.1.2'] # example
username = 'user'  # Замените на ваше имя пользователя
passw = 'pass'

# --- Файлы ---
remote_path = '/test.rsc'  # Полный путь к файлу на сервере
remote_path_bck = '/test.backup'


def scp_downloader(host: str, user: str, password: str, remote: str, local: str):

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(
            hostname=host,
            port=22,
            username=user,
            password=password
        )

        scp_client = ssh_client.open_sftp()
    # 3. Скачиваем файл
        scp_client.get(remote, local)
    except paramiko.AuthenticationException:
        print("Ошибка аутентификации.")
    except paramiko.SSHException as e:
        print(f"Ошибка SSH-соединения: {e}")
    except FileNotFoundError:
        print(f"Файл {remote} не найден на сервере.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
    finally:
        # Закрываем соединение в любом случае
        if 'ssh_client' in locals() and ssh_client:
            ssh_client.close()


for ip in hosts:
    date = datetime.date.today()
    ip_addr = ip.replace(".", "_")
    local = f"{ip_addr}_{date}"+".txt"
    local_bcp = local.replace(".txt", ".backup")
    scp_downloader(ip, username, passw, remote_path, local)
    scp_downloader(ip, username, passw, remote_path_bck, local_bcp)
