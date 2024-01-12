#This is a tool for embedding date and time info into images and videos pulled from Snapchat's Memories using Snapchat's API.
#The script parses the date and time info from the filename where the name follows the format:
#year-month-date_hour-minute-time (example: 2014-01-10_19-38-28.jpg).
#The images and videos can be downloaded by following this guide:
#https://github.com/ToTheMax/Snapchat-All-Memories-Downloader
#Note that this requires an installation of ffmpeg in order to rewrite the image/video date/time tags

import os
import re
from datetime import datetime
import subprocess

# Specify the file path
file_path = '/Volumes/4TB/Photos Backups/Snapchat Exports/test'
ffmpegpath = '/Users/kellylab/audio-orchestrator-ffmpeg/bin/ffmpeg'
#file_path = input("Drag the folder here")
#file_path = file_path.strip('\'')

#Define a function with the input for file path which lists all the files in the directory while excluding hidden files
def list_visible_files_with_list_comprehension(file_path):
    visible_files = [file for file in os.listdir(file_path) if not file.startswith('.')]
    return visible_files

filenamelist = list_visible_files_with_list_comprehension(file_path)

for i in range(len(filenamelist)):
    #Extract the time from the filename using regex
    filename_string = re.search(r"(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})", filenamelist[i]).group(1)
    #Extract the time from the file info
    creation_time_string = datetime.fromtimestamp(os.stat(file_path+'/'+filenamelist[i]).st_birthtime).strftime("%Y-%m-%d_%H-%M-%S")
    date_obj = datetime.strptime(creation_time_string, '%Y-%m-%d_%H-%M-%S')

    if '.mp4' in filenamelist[i] and filename_string != creation_time_string:
        command1 = "'" + ffmpegpath + "' -i '" +  file_path + '/' + filenamelist[i] + "' -c copy -map 0 -metadata creation_time='" + date_obj.strftime('%Y-%m-%d %H:%M:%S') + "' '" + file_path + '/FIXED_' + filenamelist[i] + "'"
        command2 = 'SetFile -d "' + date_obj.strftime('%m/%d/%Y %H:%M:%S" ') + "'" + file_path + '/FIXED_' + filenamelist[i] + "'"
        process = subprocess.Popen("exec " + command1 + " ; " + command2, shell = True, stdout = subprocess.DEVNULL, stderr = subprocess.STDOUT)
        returncode = process.wait()
        process.kill()
        os.remove(file_path + '/' + filenamelist[i])
        print('Video ', filenamelist[i], ' was fixed!')
    elif filename_string != creation_time_string:
        os.utime(file_path + '/' + filenamelist[i], (date_obj.timestamp(), date_obj.timestamp()))
        command = 'SetFile -d "' + date_obj.strftime('%m/%d/%Y %H:%M:%S" ') + "'" + file_path + '/' + filenamelist[i] + "'"
        process = subprocess.Popen("exec " + command, shell = True, stdout = subprocess.DEVNULL, stderr = subprocess.STDOUT)
        returncode = process.wait()
        process.kill()
        print('Image ', filenamelist[i], ' was fixed')
    else:
        print(filenamelist[i], ' is fine')
        



for i in range(len(filenamelist)):
    #Extract the time from the filename using regex
    filename_string = re.search(r"(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})", filenamelist[i]).group(1)
    #Extract the time from the file info
    creation_time_string = datetime.fromtimestamp(os.stat(file_path+'/'+filenamelist[i]).st_birthtime).strftime("%Y-%m-%d_%H-%M-%S")
    date_obj = datetime.strptime(creation_time_string, '%Y-%m-%d_%H-%M-%S')

command1 = "'" + ffmpegpath + "' -i '" +  file_path + '/' + filenamelist[i] + "' -c copy -map 0 -metadata creation_time='" + date_obj.strftime('%Y-%m-%d %H:%M:%S') + "' '" + file_path + '/FIXED_' + filenamelist[i] + "'"
command2 = 'SetFile -d "' + date_obj.strftime('%m/%d/%Y %H:%M:%S" ') + "'" + file_path + '/FIXED_' + filenamelist[i] + "'"
process = subprocess.Popen("exec " + command1, shell = True, stdout = subprocess.DEVNULL, stderr = subprocess.STDOUT)
process.wait()
process.kill()

process = subprocess.Popen("exec " + command1, shell = True, stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
returncode = process.wait()
process.kill()