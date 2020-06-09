from csv import DictReader

with open('csv/file.csv','r') as f:
  csv_reader=DictReader(f,delimiter='|')
  for row in csv_reader:
    print(row['age'])
