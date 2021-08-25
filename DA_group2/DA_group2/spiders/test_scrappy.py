import unittest
import Browser
import requests
import os

class TestBrowser(unittest.TestCase):
    def test_startreq(self):
        rh = requests.get(Script.url)

print("User Agent:")
print(Script.rh.text)

headers = {
    'User-Agent': 'Mobile'
}

print("User Agent:")
print(Script.rh.text)

class TestAllProgram(unittest.TestCase):
    def test(self):
        os.system("C:\\Users\\lenno\\Desktop\\DA_group2\\DA_group2\\DA_group2\\spiders\\Browser.py")
        os.system("C:\\Users\\lenno\\Desktop\\DA_group2\\DA_group2\\DA_group2\\spiders\\scrapimage.py")
        os.system("C:\\Users\\lenno\\Desktop\\DA_group2\\DA_group2\\DA_group2\\spiders\\scrapindex.py")

if __name__ == '__main__':
    unittest.main()
