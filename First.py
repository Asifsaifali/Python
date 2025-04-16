
# fs = open("Student.dat","wb")
# x = ["python",1,2.4]
# pickle.dump(x,fs)
# print("file ctreated successfully")
# fs.close()

# fs = open("Student.dat","rb")
# data = pickle.load(fs)
# for i in data:
#     print(i)

def write():
   import pickle
   student = []
   fs = open("Student.dat","wb")
   for i in range(2):
      name = input("Enter the name of student:")
      roll = int(input("Enter the roll of student:"))
      marks = int(input("Enter the marks of student:"))
      data = [name,roll,marks]
      student.append(data) #Student[[name,roll,marks],[name,roll,marks]]
      pickle.dump(student,fs)
      print("Data inserted successfully")
# write()

def read():
   import pickle
   fs = open("Student.dat","rb")
   data = pickle.load(fs)
   print(data)

read()