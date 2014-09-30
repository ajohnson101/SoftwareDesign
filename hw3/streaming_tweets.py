# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 20:40:23 2014

@author: anders
"""

from pattern.web import *

# gather data for #yolo and write it to a .txt document
def yoloSwag():

    f = open("yoloTester.txt", "w")
    yolo = Twitter(language='en').stream('#yolo')
    
    last_yolo=''
    
    for i in range(480):
        time.sleep(1)
        yolo.update(bytes=1024)
        if yolo and yolo[-1].text!=last_yolo:
            last_yolo=yolo[-1].text
            print last_yolo
            print time.ctime()
            f.write(last_yolo + "\n"+ str(time.ctime()) + "\n")
    
    f.close()
    
# gather data for #smh and write it to a .txt document
def shakeItOff():

    f = open("shakeTester.txt", "w")
    smh = Twitter(language='en').stream('#smh')
    
    last_smh=''
    
    for i in range(480):
        time.sleep(1)
        smh.update(bytes=1024)
        if smh and smh[-1].text!=last_smh:
            last_smh=smh[-1].text
            print last_smh
            print time.ctime()
            f.write(last_smh + "\n"+ str(time.ctime()) + "\n")
    
    f.close()
    
# gather data for #ftw and write it to a .txt document
def winning():

    f = open("winningTester.txt", "w")
    ftw = Twitter(language='en').stream('#ftw')
    
    last_ftw=''
    
    for i in range(480):
        time.sleep(1)
        ftw.update(bytes=1024)
        if ftw and ftw[-1].text!=last_ftw:
            last_ftw=ftw[-1].text
            print last_ftw
            print time.ctime()
            f.write(last_ftw + "\n"+ str(time.ctime()) + "\n")
    
    f.close()
    
    
    
yoloSwag() 
shakeItOff()   
winning()   