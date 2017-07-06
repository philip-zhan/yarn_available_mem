import urllib2

content = urllib2.urlopen("http://172.18.0.5:8088/jmx?get=Hadoop:service=ResourceManager,name=RMNMInfo::LiveNodeManagers").read()

