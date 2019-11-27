# created by Vaclav Nekuza
import os
import datetime


class Log_management:

    """
    Constructor
    path - path to file with logs to be cleaned up
    all_files = list of all files and directories pointed at by the path
    """
    def __init__(self, path):
        self.path = path
        os.chdir(path)
        self.all_files = os.listdir(self.path)

    """
    find_logs returns names of the files for method gzip_logs to be gziped.
    ()
    """
    def find_logs(self):
        logs_to_change = []
        for file in self.all_files:
            if file[-2:] != 'gz' and os.path.isfile(self.path + '/' + file):
                logs_to_change.append(file)
        return sorted(logs_to_change, reverse=True)     # sorting prevents issues with renaming the files

    """
    gzip_logs uses gzip function of linux system, compresses the files from find_logs and 
    sends them to be renamed to vacate space for new logs.
    """
    def gzip_logs(self, logs):
        for filename in logs:
            os.system('gzip ' + filename)
            self.rename_file(filename + '.gz')

    """
    rename_file receives file name to be renamed to vacate space for new logs, checks if there are not 
    any duplicates and recursively changes names of duplicated files so the order of the files 
    stays the same(log with the highest number is oldest).
    """
    def rename_file(self, filename):
        work_filename = filename.split('.')
        if work_filename[-2].isdigit():
            work_filename[-2] = str(int(work_filename[-2]) + 1)
            new_filename = '.'.join(work_filename)
        else:
            work_filename.append('gz')
            work_filename[-2] = '1'
            new_filename = '.'.join(work_filename)
        if new_filename in self.all_files:
            self.rename_file(new_filename)          #recursion to keep the proper order of files
        os.system('mv ' + filename + ' ' + new_filename)

    """
    archive creates new folder called archive and inside two other layers of folders corresponding to year and month 
    of executing this script for better management of logs. 
    """
    def archive(self, files_to_archive):
        work_path = self.path
        date = datetime.datetime.now()
        year = str(date.year)
        month = str(date.month)
        for infile in ["archive", year, month]:
            if infile not in os.listdir(work_path):
                os.system("mkdir " + infile)
            work_path = work_path + "/" + infile
            os.chdir(work_path)
        os.chdir(self.path)
        for filename in files_to_archive:
            os.system("mv " + filename + " " + work_path)