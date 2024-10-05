from netmiko import ConnectHandler, exceptions
from rich import print as rprint
from pprint import pprint
from projj.acl__inventory import ACL_INVENTORY

print(f"---------------------{ACL_INVENTORY[1]['host']}-------------------")
connection = ConnectHandler(
        device_type = ACL_INVENTORY[1]["device_type"],
        host = ACL_INVENTORY[1]["host"],
        username = ACL_INVENTORY[1]["user"],
        password = ACL_INVENTORY[1]["password"],
        secret = ACL_INVENTORY[1]["secret"],
        port = ACL_INVENTORY[1]["port"]
        
    )
connection.enable()
connection.config_mode()
which_prompt = connection.find_prompt()
print(which_prompt)

output = connection.send_config_from_file(config_file="R2-PC2.txt")
    
    
    
rprint(output)


connection.disconnect()





