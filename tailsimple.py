import time
import re
from datetime import datetime
import requests
import sys


lineformat = re.compile(r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.1")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (?P<refferer>-|"([^"]+)") (["](?P<useragent>[^"]+)["])""", re.IGNORECASE)

date_format = "%d/%b/%Y:%H:%M:%S %z" 


#raw_date = "01/Apr/2021:04:17:59 +0000"#this can be copied from here into progress.txt for testing

#initialise global variable date
#date = datetime.now()

def parse(line):
    data = re.search(lineformat, line)
    if data:
        datadict = data.groupdict()
        return datadict
    else:
        return None


def persist(ip, useragent, time, website, response):
    data = {
        'ipaddress': ip,
        'useragent': useragent,
        'time': time,
        'website':website,
        'response': response
    }
    response = requests.post('http://fypbackend-env.eba-srywycaj.eu-west-1.elasticbeanstalk.com/connections/add',data=data)
    return response


def saveProgress(datestr):#feel like it could be easier to pass in the date obj but then again the raw str version is available at all times
    with open("progress.txt","w") as f:
        f.write(datestr)

def printDates(date1, date2):
    print(date1.strftime(date_format) + " 2 " + date2.strftime(date_format) )


def watch(fn):
    global date
    fp = open(fn, 'r')
    while True:
        new = fp.readline()
        # Once all lines are read this just returns (empty - none - false) - how if new is able to work
        # until the file changes and a new line appears

        if new:
            print(new)
            datadict = parse(new)
            if datadict is not None:
                tempDate = datetime.strptime(datadict["dateandtime"], date_format)
                printDates(tempDate, date)
                if tempDate > date:
                    response = persist(datadict["ipaddress"], datadict["useragent"], datadict["dateandtime"], datadict["refferer"], datadict["status"])
                    print(response)
                    if response=="<Response [200]>":
                        date = tempDate#this is done after we verify that the data actually was received by server otherwise why bother log it as complete
                        saveProgress(datadict["dateandtime"])
        else:
            print("SLEEP")
            time.sleep(4)


def loadProgress():
    #global date
    with open("progress.txt","r") as f:
             date = datetime.strptime(f.readline(), date_format)
             print(type(date))
             return date
    #take in value from log file and assign to global var date
    

fn = 'accesslog.txt'


#hardcoded datetime to start the persisting from
#this raw data could be recovered from a textfile or passed in as param
# - now at the top 


#command line args
#sys.argv - index0 = name of program 


date = loadProgress()
print(type(date))
watch(fn)
#for hit_word, hit_sentence in watch(fn, words):
    #print ("Found %r in line: %r" % (hit_word, hit_sentence))

