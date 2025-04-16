import csv

# with open("Demo.csv","w") as fobj:
#     fs = csv.writer(fobj)
#     fs.writerow(["Id","Name","Roll"])
#     a = ['1','A','100']
#     fs.writerow(a)
#     print("File created!")

with open("Demo.csv","r") as f:
    data = csv.reader(f)
    print(data)