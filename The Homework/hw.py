from datetime import datetime
import os

filename = str(datetime.now().date())

print("Today's Date - "+ filename)
allfiles = os.listdir()



print("Enter homework for \nEnglish")
eng = input("")
print("Mathematics")
mat = input("")
print("Physics")
phy = input("")
print("Computer Science")
csc = input("")
print("Chemistry")
che = input("")

def hwsave():
    file = open(filename+".txt", "w")
    file.write("Homework for " + filename + "\n")
    file.write("English - " + eng + "\n")
    file.write("Mathematics - " + mat + "\n")
    file.write("Physics - " + phy + "\n")
    file.write("Computer Science - " + csc + "\n")
    file.write("Chemistry - " + che + "\n")
    file.close()

def hwsaveexists():
    file.write("\nHomework for " + filename + "\n")
    file.write("English - " + eng + "\n")
    file.write("Mathematics - " + mat + "\n")
    file.write("Physics - " + phy + "\n")
    file.write("Computer Science - " + csc + "\n")
    file.write("Chemistry - " + che + "\n")
    file.close()


if filename+".txt" in allfiles:
    file = open(filename+".txt", "a")
    print("Homework Already recorded")
    print("The input data will be recorded under \"EDIT\" subdivision in the same file")
    file.write("EDIT\nat " + str(datetime.now()))
    hwsaveexists()
else:
    hwsave() 

#want any changes?
#contact at akashthelezend@gmail.com
