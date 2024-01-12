# Snapchat_datetime


Prerequisites:
Python 3.X
[Exiftool](https://exiftool.org/install.html)
This python script uses images and videos downloaded from Snapchat Memories (https://github.com/ToTheMax/Snapchat-All-Memories-Downloader).

First, the script parses the date and time info from the filename where the name follows the format:


  year-month-date_hour-minute-time (example: 2014-01-10_19-38-28.jpg).

Then, the date/time tags are embedded. Note that .mp4 files require exiftool to be installed in order to have the date/time tags re-written onto the files.
