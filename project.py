from netmiko import ConnectHandler, exceptions
from rich import print as rprint
from acl__inventory  import ACL_PERMITTED_INVENTORY,ACL_DENIED_INVENTORY,R1_STATUS,R2_STATUS
from restart import restart_ACL,status_ACL,restart_R1,restart_R2
from texttable import Texttable


restart_R1()
restart_R2()
rprint(f"--------------------- Restarted ---------------------")
status_ACL()

rprint("1. Permit.")
rprint("2. Deny.")
rprint("3. Close the program.")
input_action = input("Choose 1 or 2: ")

while input_action != "3":


    while input_action!="1" and input_action!="2" and input_action!="3" :
        rprint("invalid input! Please try again!")
        rprint("1. Permit.")
        rprint("2. Deny.")
        rprint("3. Close the program.")
        input_action = input("Choose 1 or 2: ")
    rprint(f"---------------------  ---------------------")
    if input_action == "1":
        rprint("1. Permit Router - R1 access to PC3.")
        rprint("2. Permit Router - R1 access to PC4.")
        rprint("3. Permit Router - R2 access to PC1.")
        rprint("4. Permit Router - R2 access to PC2.")
        rprint("5. back.")
        input_action_catagory = input("Choose a number: ")
        while input_action_catagory!="1" and input_action_catagory!="2" and input_action_catagory!="3" and input_action_catagory!="4" and input_action_catagory!="5" :
            rprint("invalid input! Please try again!")
            rprint("1. Permit Router - R1 access to PC3.")
            rprint("2. Permit Router - R1 access to PC4.")
            rprint("3. Permit Router - R2 access to PC1.")
            rprint("4. Permit Router - R2 access to PC2.")
            rprint("5. back.")
            input_action_catagory = input("Choose a number: ")

        if input_action_catagory == "5":
            print()
        else:
            input_action_catagory = int(input_action_catagory)
            connection = ConnectHandler(
                        device_type = "cisco_ios",
                        host = ACL_PERMITTED_INVENTORY[input_action_catagory-1]["host"],
                        username = 'hello',
                        password = 'hello',
                        secret = 'hello',
                        port = 22
                        
                    )
                
            connection.enable()
            connection.config_mode()
            which_prompt = connection.find_prompt()
            print(which_prompt)
            if input_action_catagory == 1 and R1_STATUS[0]["PC4"] == "denied":
                restart_R1()
                output = connection.send_config_from_file(config_file=ACL_DENIED_INVENTORY[input_action_catagory]["conf_file"])
            elif input_action_catagory == 2 and R1_STATUS[0]["PC3"] == "denied":
                restart_R1()
                output = connection.send_config_from_file(config_file=ACL_DENIED_INVENTORY[input_action_catagory-2]["conf_file"])
            elif input_action_catagory == 3 and R2_STATUS[0]["PC2"] == "denied":
                restart_R2()
                output = connection.send_config_from_file(config_file=ACL_DENIED_INVENTORY[input_action_catagory]["conf_file"])
            elif input_action_catagory == 4 and R2_STATUS[0]["PC1"] == "denied":
                restart_R2()
                output = connection.send_config_from_file(config_file=ACL_DENIED_INVENTORY[input_action_catagory-2]["conf_file"])
            else:
                output = connection.send_config_from_file(config_file=ACL_PERMITTED_INVENTORY[input_action_catagory-1]["conf_file"])
            print("hello1")
            connection.disconnect()

            if input_action_catagory == 1:
                R1_STATUS[0]["PC3"] = "permitted"
            elif input_action_catagory == 2:
                R1_STATUS[0]["PC4"] = "permitted"
            elif input_action_catagory == 3:
                R2_STATUS[0]["PC1"] = "permitted"
            elif input_action_catagory == 4:
                R2_STATUS[0]["PC2"] = "permitted"

    elif input_action == "2":
        rprint("1. Deny Router - R1 access to PC3.")
        rprint("2. Deny Router - R1 access to PC4.")
        rprint("3. Deny Router - R2 access to PC1.")
        rprint("4. Deny Router - R2 access to PC2.")
        rprint("5. back.")
        input_action_catagory = input("Choose a number: ")
        while input_action_catagory!="1" and input_action_catagory!="2" and input_action_catagory!="3" and input_action_catagory!="4" and input_action_catagory!="5" :
            rprint("invalid input! Please try again!")
            rprint("1. Deny Router - R1 access to PC3.")
            rprint("2. Deny Router - R1 access to PC4.")
            rprint("3. Deny Router - R2 access to PC1.")
            rprint("4. Deny Router - R2 access to PC2.")
            rprint("5. back.")
            input_action_catagory = input("Choose a number: ")
        
        if input_action_catagory == 5:
            print()
        else:
            
            input_action_catagory = int(input_action_catagory)
            connection = ConnectHandler(
                        device_type = "cisco_ios",
                        host = ACL_DENIED_INVENTORY[input_action_catagory-1]["host"],
                        username = 'hello',
                        password = 'hello',
                        secret = 'hello',
                        port = 22
                        
                    )
                
            connection.enable()
            connection.config_mode()
            which_prompt = connection.find_prompt()
            print(which_prompt)
            
            if input_action_catagory == 1 and R1_STATUS[0]["PC4"] == "denied":
                restart_R1()
                output = connection.send_config_from_file(config_file="./denied_texts/R1-all.txt")
            elif input_action_catagory == 2 and R1_STATUS[0]["PC3"] == "denied":
                restart_R1()
                output = connection.send_config_from_file(config_file="./denied_texts/R1-all.txt")
            elif input_action_catagory == 3 and R2_STATUS[0]["PC2"] == "denied":
                restart_R2()
                output = connection.send_config_from_file(config_file="./denied_texts/R2-all.txt")
            elif input_action_catagory == 4 and R2_STATUS[0]["PC1"] == "denied":
                restart_R2()
                output = connection.send_config_from_file(config_file="./denied_texts/R2-all.txt")
            else:
                output = connection.send_config_from_file(config_file=ACL_DENIED_INVENTORY[input_action_catagory-1]["conf_file"])
            rprint(output)
            connection.disconnect()
            

            
            if input_action_catagory == 1:
                R1_STATUS[0]["PC3"] = "denied"
                print(R1_STATUS)
            elif input_action_catagory == 2:
                R1_STATUS[0]["PC4"] = "denied"
                print(R1_STATUS)
            elif input_action_catagory == 3:
                R2_STATUS[0]["PC1"] = "denied"
                print(R2_STATUS)
            elif input_action_catagory == 4:
                R2_STATUS[0]["PC2"] = "denied"
                print(R2_STATUS)

    elif input_action == "3":
        rprint(" ")


    rprint(f"---------------------  ---------------------")
    status_ACL()

    rprint("1. Permit.")
    rprint("2. Deny.")
    rprint("3. Close the program.")
    input_action = input("Choose 1 or 2: ")

rprint(f"--------------------- Thank you for using the system. ---------------------")