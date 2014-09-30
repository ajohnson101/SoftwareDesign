# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 23:50:08 2014

@author: anders
"""
import matplotlib.pyplot as plt
f = open("yoloTester.txt")
d = {}

# manually sort dictionary because I could not plot a clean graph
#d2 = {19:6, 20:15, 21:12, 22:10, 23:5, 24:7, 25:14, 26:13}

# converted time in dictionary to time after data collection began (m)
d2 = {1:6, 2:15, 3:12, 4:10, 5:5, 6:7, 7:14, 8:13}

for line in f:
    if line[0:3] == "Mon": # sorts out everything but the time stamps
        colon = line.index(':')
        minutes = line[colon+1:colon+3] # grab the minutes after the colon
        #print minutes
        
        # make a dictionary
        try: 
            d[minutes] += 1
        except:
            d[minutes] = 1


# make the plot
x = []
y = []        
for minu in d2.keys():
    x.append(minu)
    y.append(d2[minu])

# plot stuff!    
plt.plot(x,y,'ro')
plt.plot(x,y,'b')
plt.xlabel('Time After Start of Data Collection (m)')
plt.ylabel('Number of Tweets Gathered')
plt.title('Number of Times #yolo was Tweeted over Time')
plt.show()