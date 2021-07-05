import os
import datetime
from pydub import AudioSegment
from pydub.playback import play
import time
import serial
from time import sleep

ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate = 9600

Activities = []
Time = []
Day = []

Name = input("\nActivity Name: ")
Activities.append(Name)
hmTime = input("Time (hh:mm): ")
Time.append([int(x) for x in hmTime.split(":")])
dmyTime = input("Day (dd,mm,yyyy) ")
Day.append([int(x) for x in dmyTime.split(",")])

cond = True
while cond:
    delete = False
    idDel = 0
    for i in range(len(Activities)):
        if(datetime.datetime.now().day == int(Day[i][0]) and
           datetime.datetime.now().month == int(Day[i][1]) and
           datetime.datetime.now().year == int(Day[i][2]) and
           datetime.datetime.now().hour == int(Time[i][0]) and
           datetime.datetime.now().minute == int(Time[i][1])):
           print("Alarm: ")
           print(Activities[i])
           msg = 'u\r\n'
           ser.write(msg)
           sleep(0.5)
           song = AudioSegment.from_wav("Alarm.wav")
           play(song)
           time.sleep(1)
           idDel = i
           delete = True
    if delete:
        del Activities[idDel]
        del Day[idDel]
        del Time[idDel]
    if Activities == []:
        cond = False
print("Alarms End")