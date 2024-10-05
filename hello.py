from netmiko import ConnectHandler, exceptions
from rich import print as rprint
from pprint import pprint
from invertory import INVENTORY

device_list = [
        {
            "device_type":'cisco_ios',
            "host":'192.168.198.131',
            "username":'hello',
            "password":'hello',
            "port":'22',
            "secret":'hello'
        },
        {
            "device_type":'cisco_ios',
            "host":'192.168.198.141',
            "username":'hello',
            "password":'hello',
            "port":'22',
            "secret":'hello'
        }
    
    ]


for each_device in INVENTORY:
    print(f"---------------------{each_device['host']}-------------------")
    connection = ConnectHandler(
        device_type = each_device["device_type"],
        host = each_device["host"],
        username = each_device["user"],
        password = each_device["password"],
        secret = each_device["secret"],
        port = each_device["port"]
    )
    connection.enable()
    connection.config_mode()
    which_prompt = connection.find_prompt()
    print(which_prompt)

    output = connection.send_command("do sh ip int br")
    
    
    
    rprint(output)
    
    
    

connection.disconnect()



