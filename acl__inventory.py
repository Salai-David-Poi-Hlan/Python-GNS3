ACL_DENIED_INVENTORY = [
    #R1-PC3
    {"host": "192.168.198.131",  "denied_host":"192.168.20.100", "conf_file": './denied_texts/R1-PC3.txt' },
    #R1-PC4
    {"host": "192.168.198.131",  "denied_host":"192.168.10.101", "conf_file": './denied_texts/R1-PC4.txt' },
    #R2-PC1
    {"host": "192.168.198.141",  "denied_host":"192.168.10.100", "conf_file": './denied_texts/R2-PC1.txt' },
    #R2-PC2
    {"host": "192.168.198.141",  "denied_host":"192.168.10.101", "conf_file": './denied_texts/R2-PC2.txt' },
]

ACL_PERMITTED_INVENTORY = [
    #R1-PC3
    {"host": "192.168.198.131",  "denied_host":"192.168.20.100", "conf_file": './permitted_texts/R1-PC3-cancel.txt' },
    #R1-PC4
    {"host": "192.168.198.131",  "denied_host":"192.168.10.101", "conf_file": './permitted_texts/R1-PC4-cancel.txt' },
    #R2-PC1
    {"host": "192.168.198.141",  "denied_host":"192.168.10.100", "conf_file": './permitted_texts/R2-PC1-cancel.txt' },
    #R2-PC2
    {"host": "192.168.198.141",  "denied_host":"192.168.10.101", "conf_file": './permitted_texts/R2-PC2-cancel.txt' },
]

R1_STATUS = [
    {"PC3": "permitted", "PC4": "permitted"}
]
R2_STATUS = [
    {"PC1": "permitted", "PC2": "permitted"}
]