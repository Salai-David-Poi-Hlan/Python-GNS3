from texttable import Texttable
from rich import print as rprint
from restart import restart_ACL
from acl__inventory import R1_STATUS,R2_STATUS

def status_ACL():
    R1 = Texttable()
    R1.add_rows([['', 'Access-PC3' , 'Access-PC4'], ['R1', R1_STATUS[0]["PC3"], R1_STATUS[0]["PC4"]], ])
    R2 = Texttable()
    R2.add_rows([['', 'Access-PC1' , 'Access-PC2'], ['R2', R2_STATUS[0]["PC1"], R2_STATUS[0]["PC1"]], ])
    rprint(f"--------------------- Status ---------------------")
    rprint(R1.draw())
    rprint(f"---------------------  ---------------------")
    rprint(R2.draw())


status_ACL()

R1_STATUS[0]["PC3"] = "denied"
R1_STATUS[0]["PC4"] = "denied"

status_ACL()


rprint(R1_STATUS)



rprint("1. Permit.")
rprint("2. Deny.")
rprint("3. Close the program.")
input_action = "1"
while input_action!=3:
    print("lee")
    while input_action!="1" or input_action!="2" or input_action!="3" :
            rprint("invalid input! Please try again!")
            rprint("1. Permit.")
            rprint("2. Deny.")
            rprint("3. Close the program.")
            input_action = input("Choose 1 or 2: ")