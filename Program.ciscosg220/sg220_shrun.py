from netmiko import ConnectHandler
core = {
    "device_type": "cisco_s200",
    "host": "192.168.97.45",
    "username": "cisco",
    "password": "Ciscoweb2019!"
}
net_connect = ConnectHandler(**core)
output= net_connect.send_command("show run")
print(output)
net_connect.disconnect()