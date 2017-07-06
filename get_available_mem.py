import re
import urllib2

http = urllib2.urlopen(
    "http://172.18.0.5:8088/jmx?get=Hadoop:service=ResourceManager,name=RMNMInfo::LiveNodeManagers").read()
matches = re.findall(r"UsedMemoryMB\\\":(\d+)", http)
for match in matches:
    print str((int(match) + 1023) / 1024) + "GB"
