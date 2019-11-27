# created by Vaclav Nekuza
import os
import unittest
import VNekuza_log_script


class Test_Log_management(unittest.TestCase):
    path = os.getcwd() + "/test_files"

    def test_init(self):
        log = VNekuza_log_script.Log_management(Test_Log_management.path)
        self.assertIsInstance(log, VNekuza_log_script.Log_management)

    def test_find_logs(self):
        cmp_list = ["alternatives.log", "alternatives.log.1", "alternatives.log.1.gz", "apport.log", "apport.log.2.gz"]
        log = VNekuza_log_script.Log_management(Test_Log_management.path)
        act_list = log.find_logs()
        for filename in act_list:
            self.assertIn(filename, cmp_list)

    def test_gzip_and_rename(self):
        cmp_list = ["alternatives.log.1.gz", "alternatives.log.2.gz", "alternatives.log.3.gz",
                    "apport.log.1.gz", "apport.log.2.gz", "backuplogs"]
        log = VNekuza_log_script.Log_management(Test_Log_management.path)
        act_list = log.find_logs()
        log.gzip_logs(act_list)
        gziped_list = os.listdir(Test_Log_management.path)
        for filename in gziped_list:
            self.assertIn(filename, cmp_list)
        self.cleanup()      # helps to renew the testing directory for another test

    def cleanup(self):
        os.chdir(Test_Log_management.path)
        old_files = os.listdir(Test_Log_management.path)
        for file in old_files:
            if os.path.isfile(file):
                os.system("rm " + file)
        new_files = os.listdir(Test_Log_management.path + "/backuplogs")
        for nfile in new_files:
            os.system("cp " + Test_Log_management.path + "/backuplogs/" + nfile + " " + Test_Log_management.path)


if __name__ == '__main__':
    unittest.main()
