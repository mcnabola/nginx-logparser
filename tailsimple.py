import time
import re
from datetime import datetime

lineformat = re.compile(r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.1")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (?P<refferer>-|"([^"]+)") (["](?P<useragent>[^"]+)["])""", re.IGNORECASE)

date_format = "%d/%b/%Y:%H:%M:%S %z" 


raw_date = "01/Apr/2021:04:17:59 +0000"
date = datetime.strptime(raw_date, date_format)

def parse(line):
    data = re.search(lineformat, line)
    if data:
        datadict = data.groupdict()
        return datadict
    else:
        return None


def persist():
    print("persist")

def watch(fn, words):
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
                if tempDate > date:
                    print("In d hoi")
                    date = tempDate#this should probably be done later like after the request has sent so we know that we can actually mark this off as being complete

                #convert datestring to datetime obj 
            for word in words:###this can be the check here to see if the line is new
                if word in new:
                    yield (word, new)
        else:
            print("SLEEP")
            time.sleep(4)

fn = 'accesslog.txt'
words = ['word']

#hardcoded datetime to start the persisting from
#this raw data could be recovered from a textfile or passed in as param
# - now at the top 


for hit_word, hit_sentence in watch(fn, words):
    print ("Found %r in line: %r" % (hit_word, hit_sentence))

