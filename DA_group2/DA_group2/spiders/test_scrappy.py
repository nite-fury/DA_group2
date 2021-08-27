import unittest
import os
class Testrecon(unittest.TestCase):
    def test(self):
        os.system("C:\\Users\\lenno\\Desktop\\DA_group2\\DA_group2\\DA_group2\\spiders\\Browser.py")

class Testresponse(unittest.TestCase):
    def test(self):
        os.system("C:\\Users\\lenno\\Desktop\\DA_group2\\DA_group2\\DA_group2\\spiders\\scrapindex.py")

class Testimage(unittest.TestCase):
    def test(self):
        os.system("C:\\Users\\lenno\\Desktop\\DA_group2\\DA_group2\\DA_group2\\spiders\\scrapimage.py")
if __name__ == '__main__':
    unittest.main()
