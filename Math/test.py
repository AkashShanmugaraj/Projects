from math import factorial, floor

print("Enter the Natural Number which is to be converted to a Factorial Form")
givennumber = int(input(""))

conval = ""
conval2 = 0
def last_num(n1):
    for num in range(1,100000000000000):
        if n1 - factorial(num) < 0:
            print("Conversion Error!\nCheck to given Number properly")
            print("The member of factorial series that is nearby to the given number is", factorial((num-1)))
            print("which is "+str(num-1)+"!")
            break
for num in range(1,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
    a = factorial(num)
    aa = givennumber/a
    print(aa)
    print()
    if givennumber/a == 1:
        print("The number is", num)
        conval = "True"
        break
    elif givennumber/a < 0:
        last_num(givennumber)
        break
    
        
    