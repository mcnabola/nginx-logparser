import time
import re
from datetime import datetime
import requests
import sys



date_format = "%d/%b/%Y:%H:%M:%S %z" 

def persist(ip, useragent, time, website):
    data = {
        'ipaddress': ip,
        'useragent': useragent,
        'time': time,
        'website':website,
        'response':'202'
    }
    response = requests.post('http://fypbackend-env.eba-srywycaj.eu-west-1.elasticbeanstalk.com/connections/add',data=data)
    return response

print(persist("11.34.33.234","Linux;Firefox","01/Apr/2021:04:17:34 +0000","https://johnbons.com/"))
