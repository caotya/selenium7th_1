import csv
import unittest


class FileRead(unittest.TestCase):
    def test_fileread(self):
        path = r'C:\Users\14045\PycharmProjects\selenium_Day1\Date\test_data.csv'
        file = open(path,'r')
        filetext = csv.reader(file)
        try:
            for item in filetext:
                print(item)
        finally:
            file.close()
if __name__ == '__main__':
    unittest.main()