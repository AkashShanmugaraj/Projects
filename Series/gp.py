print("Welcome to Geometric Progression Calculator")
print("We will ask you to enter values of First Term(a), Number of terms(n), Common Ratio(d)")
a = int(input("Enter value of a\n"))
r = int(input("Enter value of r\n"))
n = int(input("Enter value of n\n"))

print("The sequence generated from the given data is")
print(a)
c = a
for i in range(1,n):
    val = a * r**i
    print(val)
    c += val

print("Sum of the above sequence is")
print(c)
