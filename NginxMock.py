import random 
from  datetime import datetime
import time

demo = '178.16.199.149 - - [05/Jan/2021:22:04:55 +0000] "GET /trackingFile.css HTTP/1.1" 200 34 "https://rocketry.neocities.org/" "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0" /"-"'

list_ips = ["178.16.199.149","156.255.5.24", "178.67.54.222", "54.33.67.4"]

print(len(list_ips))

for i in range(10):
    ip = list_ips[random.randint(0, len(list_ips)-1 )]

    #date generation to match the format of that - already done this datetime strformatting before
    date_current = datetime.now()
    date =date_current.strftime("%d/%b/%Y:%H:%M:%S %z")
    queriedContent = '"GET /trackingFile.css HTTP/1.1"'

    response = "200 34"

    website = '"https://rocketry.neocities.org"'

    useragent = '"Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko Firefox"'

    proxy = '"-"'


    outputString = ip + " - - " + "[" + date + "] " + queriedContent + " " + response + " " + website + " " + useragent + " " + proxy   
    print(outputString)
    time.sleep(6)



#accessLog = open("nginxLog.txt","a")#a-append
#accessLog.write()
#accessLog.close()
