
def conversion():
    from math import factorial, floor
    from tkinter import BooleanVar
    try:
        print("Enter the Natural Number which is to be converted to a Factorial Form")
        givennumber = int(input(""))
    
        conval = ""
        conval2 = 0
        def last_num(n1):
            for num in range(1,100000000000000):
                if n1 - factorial(num) < 0:
                    print("The member of factorial series that is nearby to the given number is", factorial((num-1)))
                    print("which is "+str(num-1)+"!")
                    break
        for num in range(1,10001):
            a = factorial(num)
            if floor(a/givennumber) == 1:
                print("The number is", num)
                conval = "True"
                break
            elif conval != "True":
                print("Conversion Error!\nCheck to given Number properly")
                conval2 = 0
                last_num(givennumber)
                break
            elif conval2 == 0:
                last_num(givennumber)
    except ValueError:
        print()
    except OverflowError:
        print("Conversion Error!\nCheck to given Number properly")
        
conversion()