
ImpactStatement is a python script that autosums duration times of multiple different video codecs into one figure. 

This script adds together video durations from several video codecs placed in the same directory. The purpose of this script is to help prosecutors paint an accurate picture of how many seconds/minutes/hours  of video footage exist. It is especially usefull in voyeurism and child exploitation cases. Using the mediainfo module, it supports a wide range of formats (mpeg, mp4, asf, etc.) 

MediaInfoDLL must be placed in the python library for this script to work. Obtain this script from https://mediaarea.net/en/MediaInfo/Download/Windows. 

To begin, place all evidence "findings" in a directory. Start the script and enter the directory. Ensure the directory ends with a \ (i.e. C:\Users\Me\Desktop\Evidence\ ). A compiled time will be printed in Debug in the H/M/S form.

Warning: This script may not provide time from carved videos where the duration timestamp is missing. 

