# created by Vaclav Nekuza
import os
from VNekuza_log_script import Log_management

"""
Main function
"""


def Main(path='/var/log/'):
    log = Log_management(path)
    logs = log.find_logs()
    log.gzip_logs(logs)
    archive = list(filter(lambda x: x[-2:] == 'gz', os.listdir(path)))
    log.archive(archive)


Main()

# /var/log/
