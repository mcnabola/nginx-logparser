#!/usr/bin/env python
import gzip
import os
import sys
import re

##run with command line argument on whether you want the date outputted to a python localdate

#https://gist.github.com/hreeder/f1ffe1408d296ce0591d

##this also converts all of the logs in a folder

#last 15 mins of log data

INPUT_DIR = "nginx-logs"

#lineformat = re.compile(r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.1")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (["](?P<refferer>(\-)|(.+))["]) (["](?P<useragent>.+)["])""", re.IGNORECASE)

lineformat = re.compile(r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.1")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (?P<refferer>-|"([^"]+)") (["](?P<useragent>[^"]+)["])""", re.IGNORECASE)
#for f in os.listdir(INPUT_DIR):
#if f.endswith(".gz"):
    #logfile = gzip.open(os.path.join(INPUT_DIR, f))
#else:
    #logfile = open(os.path.join(INPUT_DIR, f))

logfile=open("logData1.txt","r")

for l in logfile.readlines():
    data = re.search(lineformat, l)
    if data:
        datadict = data.groupdict()
        ip = datadict["ipaddress"]
        datetimestring = datadict["dateandtime"]
        url = datadict["url"]
        bytessent = datadict["bytessent"]
        referrer = datadict["refferer"]
        useragent = datadict["useragent"]
        status = datadict["statuscode"]
        method = data.group(6)

        print (ip)
        print(datetimestring)
        print(url)
        print(bytessent)
        print(referrer)
        print(useragent)
        print(status)
        print(method)

logfile.close()
