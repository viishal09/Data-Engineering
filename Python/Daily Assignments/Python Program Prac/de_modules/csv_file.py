
import csv

rows = []
with open("Salary_Data.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print("header is: ","\n")
print(header,"\n")
print(rows)

#using readlines

# with open('Salary_Data.csv') as file2:
#     content = file2.readlines()
# header2 = content[:1]
# rows2 = content[1:]
# print(header2)
# print(rows2)

# file3 =  open('Salary_Data.csv', 'r')
# reader = csv.DictReader(file3)
# for row in reader:
#     print(row)  
    
# writing data into text files using csv writer()

# header = ['Name', 'M1 Score', 'M2 Score']
# data_columns = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]

# file_name = 'Marks_data.csv'
# with open(file_name,"w",newline="") as file4:
#     csv_writer = csv.writer(file4)
#     csv_writer.writerow(header)
#     csv_writer.writerows(data_columns)
    
# file4 = open("Marks_data.csv","r")
# open = file4.read()
# print(open)

# converting csv file into list

with open('de_modules\Salary_Data.csv','r') as read_obj:
    reader_csv = csv.reader(read_obj)
    list_csv = list(reader_csv)
    print(list_csv)


