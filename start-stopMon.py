#!/usr/bin/python
from time import sleep
import sys
import os
import signal
import csv
from subprocess import check_call
import subprocess


def main():
    try:
        start_stop = (sys.argv[1])
        preMonInterface = sys.argv[2]
        waitTime = sys.argv[3]
    except: None
    FNULL = open(os.devnull, 'w')

    if(start_stop == "start"):
        # print("start interface...")
        try:
            check_call(["airmon-ng", "start", preMonInterface], stdout=FNULL, stderr=subprocess.STDOUT)
        except: print("airmon-ng error")


        # print("start dumping...")
        try:
            dump = subprocess.Popen(["airodump-ng", preMonInterface+"mon", "-w", "dump", "--output-format", "csv"], stdout=FNULL, stderr=subprocess.STDOUT,  preexec_fn =os.setsid)
            # for i in range(0, waitTime):
            #     print(i)
            #     sleep(1)
            sleep(float(waitTime))
            os.killpg(os.getpgid(dump.pid), signal.SIGTERM)
            sleep(1)
            os.killpg(os.getpgid(dump.pid), signal.SIGTERM)
            sleep(1)
            # print("stop interface...")
            # check_call(["airmon-ng", "stop", preMonInterface+"mon"], stdout=FNULL, stderr=subprocess.STDOUT)
            sleep(1)
            output = []
            with open('dump-01.csv', 'r') as csvfile:
                csvfile.next()
                reader = csv.DictReader(csvfile, delimiter=',')
                for row in reader:
                    if((row[' ESSID']) == " ") or ((row[' ESSID'])) == None:
                        None
                    elif(row[' ESSID'][1] == "\\"):
                        None
                    else:
                        output.append(row[' ESSID'].split(" ")[1] + " - " + row['BSSID'] + " - " + row[' channel'].strip())
            output = sorted(output, key=str.lower)
            for p in output:
                print(p)
            check_call(["rm", "dump-01.csv"], stdout=FNULL, stderr=subprocess.STDOUT)

        except:
            print("error dumping")
    elif(start_stop == "stop"):
        try:
            check_call(["airmon-ng", "stop", preMonInterface+"mon"], stdout=FNULL, stderr=subprocess.STDOUT)
        except: print("error stopping airmon-ng")



if __name__ == "__main__":
    main()