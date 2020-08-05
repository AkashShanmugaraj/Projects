from datetime import datetime
import os

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

filename = str(datetime.now().date())
file = open(filename+".txt", "w")
file.write("Homework for " + filename + "\n")
file.write("English - " + eng + "\n")
file.write("Mathematics - " + eng + "\n")
file.write("Physics - " + eng + "\n")
file.write("Computer Science - " + eng + "\n")
file.write("Chemistry - " + eng + "\n")
file.close()