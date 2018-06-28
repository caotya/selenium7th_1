import csv
class CsvFile:
    @classmethod
    def csvfile(cls):
        path = r'C:\Users\14045\PycharmProjects\selenium_Day1\Date\test_data.csv'
        file =  open(path,'r')
        filetext = csv.reader(file)
        for item in filetext:
            print(item)

if __name__ =='__main__':
    CsvFile.csvfile()