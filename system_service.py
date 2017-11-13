from flask import Flask
import time
import json
import os

app = Flask(__name__)



@app.route("/time")
def dateinfo():
    now = int(time.time())
    dic = {'time' : now }
    datetime = json.dumps(dic)
    return datetime

@app.route("/ram")
def raminfo():
    dic = {}
    with open('/proc/meminfo') as f:
        for line in f:
            key = line.split(':')[0].strip()
            value = line.split(':')[1].strip()
            if(key == "MemTotal"):
                dic["Total"] = int(int(value[:-2])/1024)
            if(key == "MemFree"):
                valuetotal = dic["Total"]
                valuefree = int(int(value[:-2])/1024)
                value = valuetotal-valuefree
                dic["Used"] = value
    ram = json.dumps(dic)
    return ram 

@app.route("/hdd")
def hddinfo():
    dic = {}
    statvfs = os.statvfs('/')
    total_disk_space = int(statvfs.f_frsize * statvfs.f_blocks/1024/1024)
    free_disk_space = int(statvfs.f_frsize * statvfs.f_bfree/1024/1024)
    dic["Total"] = total_disk_space
    dic["Used"] = free_disk_space
    hdd = json.dumps(dic)
    return hdd

if __name__ == "__main__":
    app.run(port = 3000)
