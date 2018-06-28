#1.获取cvs文件的位置：r'C:\Users\14045\PycharmProjects\selenium_Day1\Date\test_data.csv'
import csv

class CsvFile:
    @classmethod
    def CsvFile1(self):
        path = r'C:\Users\14045\PycharmProjects\selenium_Day1\Date\test_data.csv'
        #2.打开文件
        file = open(path,'r')
        #3.读取文件内容
        try:
            text_csv = csv.reader(file)
        #4.输出文件内容
            for item in text_csv:
                print(item)
        finally:
            file.close()
if __name__ == '__main__':
    CsvFile.CsvFile1()