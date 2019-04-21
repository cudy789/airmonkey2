#!/usr/bin/python

from subprocess import check_output



try:
    try:
        ifconfigList = check_output(["/sbin/ifconfig"]).decode("utf-8").strip().split("\n")
    except:
        None
    availableInterfaces = []
    for i in ifconfigList:
        if (i.find("wlan")>=0):
            if i[i.find("wlan")+5] == ":":
                availableInterfaces.append(i[0:5])
                # print("appending " + i[0:5])
    print("[")
    for i in availableInterfaces:
        iwconfig = ""
        try:
            iwconfig = (check_output(["/sbin/iwconfig", i]).decode("utf-8"))
        except:
#             print("iwconfig error")

        if (iwconfig.decode("utf-8").find("ESSID:")) >= 0:
            interfaceStatus = iwconfig.decode("utf-8").split("ESSID:")[1].split(" ")[0]
            if  interfaceStatus!= "off/any":
                print("{\"interface\": \"" + i + "\",\"connection\": \"" + interfaceStatus.split("\"")[1] + "\"}")
            else:

                print("{\"interface\": \"" + i + "\",\"connection\": \"not connected\"}")
except:
    print("error running findInterfaces.py...")
