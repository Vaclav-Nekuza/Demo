# Python log manager script for linux
This script focuses on compressing actual logs in directory /var/log/ using gzip and achiving them acording to date.
It is necessary for the script to function on linux based system, using python3 with root access.

## Files
'Main.py', this files merely executes code of 'VNekuza\_log\_script.py',
'VNekuza\_log\_script.py' file contains the functional code, specifically class 'Log\_management',
'test\_VNekuza\_log\_script.py' tests the functional code on testing files
'test\_files' directory that contains examples of logs for testing and their backup

### class Log\_management
Constructor: When creating new instance it needs to initialize with a path to a directory to be managed.

'find\_logs': Searches given directory for files that are not yet compressed using gzip and returns list of file names for compression.

'gzip\_logs': Compresses files with names received as a argument in directory specified during initialization using format gzip, and for each file calls method 'rename\_file'

'rename\_file': Renames files to vacate names for new logs to avoid collision. Also renames older files to keep proper order of files, that means the oldest log is the one with highest number.

'archive': To keep logs reasonably organized, this method archives older logs that are already compressed using gzip to a new folder archive to the corresponding folders according to date.

### Testing
each method tests part of the program using testing logs in directory 'test\_files' corresponding to the name, except for method 'cleanup' 

'cleanup': Removes already used files and copy new ones from a backup directory.

## Cron startup
For this scipt to be initialize in regular intervals use cron (root access needed).

With command 'sudo crontab -e' you access cron scheduler. 

By adding line '0 5 1 * * \<absolute path to python3 interpreter> \<absolute path to the script>' script will initialize first day every month at 5:00 AM.

## Authors
* **Václav Nekuža** - assigned by **KAJOT**
'
