# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import numpy as np
from matplotlib import pyplot as plt

import serial
import io
import sys
import time
from serial.tools import list_ports

if __name__ == "__main__":
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.timeout = 0.1
    ports = list_ports.comports()
    devices = []
    for info in ports:
        devices.append(info.device)
  
    if len(devices) == 0:
        print("error: device not found")
        sys.exit(0)
    elif len(devices) == 1:
        ser.port = devices[0]
    else:
        for i in range(len(devices)):
            print("input " + str(i)+":\topen " + devices[i])
        print("input number of target port\n>> ", end="")
        num = int(input())
        ser.port = devices[num]
      
        try:
            ser.open()
            print("open " + ser.port)
        except:
            print("can't open" + ser.port)
            sys.exit(0)
        sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
        t = np.zeros(100)
        y = np.zeros(100)
        
        plt.xlabel("time[s]")
        plt.ylabel("light value")
        plt.ylim(0, 100)
        count = 0
        data = []
        while ser.is_open:
            ss = sio.readline().rstrip('\n')
            data = ss.split(' ')
            if len(data) >= 1:
                print(data)
            elif len(data) >= 2:
                t = np.append(t, int(data[0]))
                t = np.delete(t, 0)
                y = np.append(y, int(data[1]))
                y = np.delete(y, 0)
                if count > 20:
                    plt.plot(t,y)
                    plt.xlim(min(t)-1000, max(t)+1000)
                    plt.pause(0.001)
                    count = 0
            count+=1

# if __name__ == "__main__":
#     ser = serial.Serial()
#     ser.baudrate = 9600
#     ser.timeout = 0.1
#     ports = list_ports.comports()
#     devices = []
#     for info in ports:
#         devices.append(info.device)
#   
#     if len(devices) == 0:
#         print("error: device not found")
#         sys.exit(0)
#     elif len(devices) == 1:
#         ser.port = devices[0]
#     else:
#         for i in range(len(devices)):
#             print("input " + str(i)+":\topen " + devices[i])
#         print("input number of target port\n>> ", end="")
#         num = int(input())
#         ser.port = devices[num]
#       
#         try:
#             ser.open()
#             print("open " + ser.port)
#         except:
#             print("can't open" + ser.port)
#             sys.exit(0)
#         sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
#         fig, ax = plt.subplots(1,1)
#         while ser.is_open:
#             s = sio.readline()
#             s.rstrip("\n")
#             ss = s.split(" ")
#             print(ss) 
#             if len(ss) >= 2:
#                 pause_plot(ss[0], ss[1])

# if __name__ == "__main__":
#     x = 0.1
#     value = 0.2*x
#     t = np.zeros(100)
#     y = np.zeros(100)
#     plt.ylim(0, 100)
#     plt.xlabel("time[s]")
#     plt.ylabel("light value")
#
#     while True:
#         t = np.append(t, float(x))
#         t = np.delete(t, 0)
#         y = np.append(y, float(value))
#         y = np.delete(y, 0)
#         plt.plot(t,y)
#         plt.xlim(min(t), max(t))
#         # plt.draw()
#         plt.pause(0.001)
#         x += 0.1
#         value = 0.2*x


