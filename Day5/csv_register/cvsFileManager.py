import csv
import os


class csvfilemanager:
    def read(self,filename):
        list = []
        base_path = os.path.dirname(__file__)
        print(base_path)
        path = base_path.replace('Day5','Data/'+filename)
        print(path)
        with open(path ,'r') as file:
            data_table = csv.reader(file)
            for item in data_table:
                print(item)
                list.append(item)
        return list
if __name__ == '__main__':
    list = csvfilemanager().read('test_data.csv')