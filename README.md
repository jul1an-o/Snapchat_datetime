# Snapchat date/time embedder


## **Prerequisites**

Python 3.X

[Exiftool](https://exiftool.org/install.html)

## **Description**

**This was written on MAC, Windows may handle date/time tags differently - so this is not guaranteed to work for PC.**__

This python script uses images and videos downloaded from Snapchat Memories (https://github.com/ToTheMax/Snapchat-All-Memories-Downloader).

First, the script parses the date and time info from the filename where the name follows the format: `year-month-date_hour-minute-time (example: 2014-01-10_19-38-28.jpg)`

### Images

The parsed date and time information is then embedded back onto the parent image as metadata.

### Videos
For .mp4 files, exiftool does not allow overwriting the parent video file. Instead, a new file with the prefix "FIXED_" is created with the appropriate metadata. The original file is then removed.

The line to remove the files `os.remove(file_path + '/' + filenamelist[i])` can be ignored if you don't want to delete the original video files.
