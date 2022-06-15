
import time
from datetime import datetime as dt



localhost="127.0.0.1"
appblock_list=["www.facebook.com","facebook.com","www.instagram.com","instagram.com"]
start_time="09:0:0"
hostpath="C:\Windows\System32\drivers\etc\hosts"
end_time="18:0:0"

now=dt.now()
current_time=now.strftime("%H:%M:%S")
print(current_time)
while True:
    if start_time<=current_time and current_time<=end_time:
        print("Working Hours")
        with open(hostpath,"r+")as file:
            content=file.read()
            for website in  appblock_list:
                if website in content :
                    pass
                else:
                    file.write(localhost+" "+website+"\n")
     
    else:
        print("Non working hours")
        with open(hostpath,"r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in appblock_list):
                        file.write(line)
                file.truncate()
                
    time.sleep(10)            
                