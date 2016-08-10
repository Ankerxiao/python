#!/bin/python
import json
import urllib2
def requestUrl(url):
    try:
        data = urllib2.urlopen(url).read()
        return data
    except Exception,e:
        print e

def write2File(jsonData):
    file = open("/json.txt","w")
    file.write(jsonData)
    file.close()

def parseJson(jsonData):
    value = json.loads(jsonData)
    print value

if __name__ == "__main__":
    data = requestUrl("")
    parseJson(requestUrl("http://127.0.0.1/mcmp1605/data_enter.php?method=home_info"))
