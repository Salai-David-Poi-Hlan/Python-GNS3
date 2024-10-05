from netmiko import ConnectHandler, exceptions
from rich import print as rprint
from acl__inventory  import ACL_PERMITTED_INVENTORY,ACL_DENIED_INVENTORY,R1_STATUS,R2_STATUS
from texttable import Texttable

def status_ACL():
    R1 = Texttable()
    R1.add_rows([['', 'Access-PC3' , 'Access-PC4'], ['R1', R1_STATUS[0]["PC3"], R1_STATUS[0]["PC4"]], ])
    R2 = Texttable()
    R2.add_rows([['', 'Access-PC1' , 'Access-PC2'], ['R2', R2_STATUS[0]["PC1"], R2_STATUS[0]["PC2"]], ])
    rprint(f"--------------------- Status ---------------------")
    print(R1.draw())
    rprint(f"---------------------  ---------------------")
    print(R2.draw())


def restart_ACL():
    
    for each_PC in ACL_PERMITTED_INVENTORY:
        connection = ConnectHandler(
                device_type = "cisco_ios",
                host = each_PC["host"],
                username = 'hello',
                password = 'hello',
                secret = 'hello',
                port = 22
                
            )
        
        connection.enable()
        connection.config_mode()
        which_prompt = connection.find_prompt()
        rprint(f"--------------------- Restarting ---------------------")

        output = connection.send_config_from_file(config_file=each_PC["conf_file"])


    rprint(f"--------------------- Restarted ---------------------")



    connection.disconnect()

def restart_R1():
    connection = ConnectHandler(
                device_type = "cisco_ios",
                host = "192.168.198.131",
                username = 'hello',
                password = 'hello',
                secret = 'hello',
                port = 22
                
            )
        
    connection.enable()
    connection.config_mode()
    which_prompt = connection.find_prompt()

    output = connection.send_config_from_file(config_file=ACL_PERMITTED_INVENTORY[1]["conf_file"])
    connection.disconnect()

def restart_R2():
    connection = ConnectHandler(
                device_type = "cisco_ios",
                host = "192.168.198.141",
                username = 'hello',
                password = 'hello',
                secret = 'hello',
                port = 22
                
            )
        
    connection.enable()
    connection.config_mode()
    which_prompt = connection.find_prompt()

    output = connection.send_config_from_file(config_file=ACL_PERMITTED_INVENTORY[2]["conf_file"])
    connection.disconnect()



