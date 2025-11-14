from netmiko import ConnectHandler

device = {
    'device_type': 'mikrotik_routeros',
    'host': '192.168.89.1',
    'username': 'user', 
    'password': '1234',
    'port': 22,
}

connection = ConnectHandler(**device)
output = connection.send_command('/system resource print')
print(output)
connection.disconnect()