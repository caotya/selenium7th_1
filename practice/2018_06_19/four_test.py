#这是一个获取文件内容的方法
import csv
import unittest


class FileRead(unittest.TestCase):
    @classmethod
    def test_01(self):
        path = r'C:\Users\14045\PycharmProjects\selenium_Day1\Date\test_data.csv'
        file = open(path,'r')
        readfile = csv.reader(file)
        try:
            for item in readfile:
                print(item)
        finally:
            file.close()
if __name__=='__main__':
    unittest.main()