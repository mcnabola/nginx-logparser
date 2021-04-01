import time
import re
from datetime import datetime

lineformat = re.compile(r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.1")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (?P<refferer>-|"([^"]+)") (["](?P<useragent>[^"]+)["])""", re.IGNORECASE)

def parse(line):
    data = re.search(lineformat, line)
    if data:
        datadict = data.groupdict()
        print("before NEW")
        return datadict
    else:
        return None


def persist():
    print("persist")

def watch(fn, words):
    fp = open(fn, 'r')
    while True:
        new = fp.readline()
        # Once all lines are read this just returns (empty - none - false) - how if new is able to work
        # until the file changes and a new line appears

        if new:
            print(new)
            datadict = parse(new)
            if datadict is not None:
                for key, value in datadict.items():
                    print(key,value)

                #convert datestring to datetime obj 
            for word in words:###this can be the check here to see if the line is new
                if word in new:
                    yield (word, new)
        else:
            print("SLEEP")
            time.sleep(4)

fn = 'accesslog.txt'
words = ['word']
for hit_word, hit_sentence in watch(fn, words):
    print ("Found %r in line: %r" % (hit_word, hit_sentence))

