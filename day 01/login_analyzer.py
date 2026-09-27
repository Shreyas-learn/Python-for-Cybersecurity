logs = [
    "192.168.1.10 FAILED_LOGIN",
    "192.168.1.20 SUCCESS_LOGIN",
    "192.168.1.10 FAILED_LOGIN",
    "10.0.0.5 FAILED_LOGIN",
    "192.168.1.10 FAILED_LOGIN",
    "10.0.0.5 FAILED_LOGIN",
    "10.0.0.5 FAILED_LOGIN",
]
dlogs={}
brute={}
for log in logs:
    ip, event=log.split()
    if event=="FAILED_LOGIN":
        if ip in dlogs:
            dlogs[ip]+=1
        else:
            dlogs[ip]=1
for key,value in dlogs.items():
    print(f"{key}->{value}")
    if value>=3:
        brute[key]=value
print("Potential brute-force sources:")
for key, value in brute.items():
    print(key)