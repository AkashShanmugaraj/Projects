print("Welcome to Arithmetic Progression Calculator")
print("We will ask you to enter values of First Term(a), Number of terms(n), Common Difference(d)")
a = int(input("Enter value of a\n"))
d = int(input("Enter value of d\n"))
n = int(input("Enter value of n\n"))

print("The sequence generated from the given data is")
print(a)
for i in range(1,n):
    val = a + i*d
    print(val)

sum = (n/2)*(2*a + (n - 1)*d)
print("Sum of the above sequence is")
print(sum)