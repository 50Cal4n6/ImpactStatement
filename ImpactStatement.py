# ImpactStatement.py : Video Duration Autosum Script
# Ver 1.0
# 17 Jun 2018
# Author: J. Barrett

# Welcome to ImpactStatement. This script adds together video durations from several video codecs placed in the same directory.
# The purpose of this script is to help prosecutors paint an accurate picture of how many seconds/minutes/hours 
# of video footage exist. It is especially usefull in voyeurism and child exploitation cases. Using the mediainfo
# module, it supports a wide range of formats (mpeg, mp4, asf, etc.) 

# MediaInfoDLL must be placed in the python library for this script to work. Obtain this script from 
# https://mediaarea.net/en/MediaInfo/Download/Windows. 

# To begin, place all evidence "findings" in a directory. Start the script and enter the directory. Ensure the 
# directory ends with a \ (i.e. C:\Users\Me\Desktop\Evidence\). A compiled time will be printed in Debug in the H/M/S form.

# Warning: This script may not provide time from carved videos where the duration timestamp is missing. 


import logging
import os
import time

print 'Welcome to ImpactStatement'
print 'Author:  Jacob Barrett'
print 'Date:    27 June 18'
print 'Version: 1.0'
print 'This script autosums durations from several different videos/codecs into one figure\n'

# Basic logging portion begins here

logging.basicConfig(filename='fileScan.log',level=logging.DEBUG,format='%(asctime)s %(message)s') #Creates a log

startTime = time.time() #Start time of log

logging.info('Welcome to ImpactStatement'+ ' New Scan Started') # Record the Welcome Message

endTime = time.time() #Records the end time and 

duration = endTime - startTime #Calculates the duration


#Entry portion begins here

path = raw_input('Please enter a directory and ensure it ends with a \:') #Provides a raw input area         

  
#Main Script Begins Here

os.chdir(os.environ["PROGRAMFILES"] + "\\mediainfo")

from MediaInfoDLL import MediaInfo, Stream #Imports MediaInfo from the Lib

MI = MediaInfo() #Defines MI as the python script MediaInfo 

def get_lengths_in_milliseconds_of_directory(prefix):
    
    for f in os.listdir(path): # For each file in the directory
        
        MI.Open(path + f) #Opens each file
        
        duration_string = MI.Get(Stream.Video, 0, "Duration") #Defines duration_string
        
        try:
            
            duration = int(duration_string) #Gets the duration from metadata

            yield duration
            
            logging.info(duration) #Logs duration of each file found in ms
            
        except ValueError: 
            
            print("{} Not a video file or missing duration stamp\n".format(f)) 
            #This line prints whenever a non-video is detected in the directory or a video lacks duration stamp     
            
            logging.info('Non-video or missing duration stamp detected') 
            #Logs whenever a non-video is detected but does not stop the script 
            
        MI.Close() #Closes MediaInfo
        
# Time consolidation portion begins here
        
totalms = sum(get_lengths_in_milliseconds_of_directory(path)) 
#Obtains total time in ms, which is mediainfo's default time standard

print time.strftime("TOTAL TIME in Hours/Minutes/Seconds: %H:%M:%S", time.gmtime(totalms/1000.00)) 
#Coverts ms to H/M/S by dividing ms by 1000

logging.info('Program Terminated Normally') #End of log