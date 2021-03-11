# Source Code 1
x,n = eval(input("Enter values of x and n seperated by commas: "))
print("The value of x to the power n is",x**n)

# Output 1
#Enter values of x and n seperated by commas: 4,9
#The value of x to the power n is 262144

#Source Code 2
p = int(input("Enter value of 'p': "))
n = int(input("Enter value of 'n': "))
r = float(input("Enter value of 'r': "))
si = (p*n*r)/100
print("Simple Intrest for the given vaules is",si)

#Output 2
#Enter value of 'p': 10000
#
#Enter value of 'n': 5
#
#Enter value of 'r': 8.3
#Simple Intrest for the given vaules is 4150.000000000001

#Source Code 3
n = int(input("Enter a number: "))
if n%2 == 0:
    print(n,"is a even number.")
elif n%2 != 0:
    print(n,"is a odd number.")

#Output 3 (1)
#Enter a number: 45
#45 is a odd number.

#Output 3 (2)
#Enter a number: 58
#58 is a even number.

#Source code 4
perc = float(input("Enter percentage of a student: "))
if perc > 91:
    print("The Grade of the student is A")
elif perc > 81:
    print("The Grade of the student is B")
elif perc > 71:
    print("The Grade of the student is C")
elif perc > 61:
    print("The Grade of the student is D")
elif perc > 51:
    print("The Grade of the student is E")
elif perc > 41:
    print("The Grade of the student is F")
    
#Output 4
#Enter percentage of a student: 92
#The Grade of the student is A


#Source Code 5
terma = 0
termb = 1

l = int(input("Enter limit: "))
print(terma, end = "  ")
for i in range(l-1):
    print(termb, end = "  ")
    a = terma + termb
    terma = int(termb)
    termb = a

#Output 5
#Enter limit: 10
#0  1  1  2  3  5  8  13  21  34


#Source Code 6
x = int(input("Enter Limit: "))
a = [2,3,5,7]
c = 0
for n in range(1,x+1):
  if n in a:
      print(n)
  if n%2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0:
      pass
  elif n%2 != 0 or n%3 != 0 or n%5 != 0 or n%7 != 0:
      print(n)

#Output 6
#Enter Limit: 20
#1
#2
#3
#5
#7
#11
#

#Source Code 7
n = input("Enter a 3 digit number: ")
s = (int(n[0])**3) + (int(n[1])**3) + (int(n[2])**3)
if s == int(n):
    print(n,"is an ArmStrong Number!")
else:
    print(n, "is not an ArmStrong Number!")

#Output 7
#Enter a 3 digit number: 371
#371
#371 is an ArmStrong Number!


#Source Code 8
n = int(input("Enter a number: "))
nums = list(range(1,n+1))
divisors = []
total = 0
for a in nums:
    if n%a == 0:
        divisors.append(a)
        total += a

if n in divisors:
    total -= n
if total == n:
    print("The given number is a perfect number")
else:
    print("The given number is not a perfect number")

#Output 8
#Enter a number: 28
#The given number is a perfect number
##Source Code 11
#a = input("Enter a string: ")
#if a == a[::-1]:
#    print(True)
#else:
#    print(False)
    
    
#Source Code 9
from math import factorial
l = int(input("Enter the limit: "))
x = int(input("Enter value of x: "))
s = 1
for i in range(1,l+1):
    term = (x**i)/(factorial(i))
    s += term
print("The sum is",s)

#Output 9
#Enter the limit: 8
#
#Enter value of x: 2
#The sum is 7.387301587301587
#

#Output 11
Enter a string: Mom
False

Enter a string: mom
True


#Source Code 12
a = input("Enter string: ")
alpha = 0
ualpha = 0
lalpha = 0
sp = 0
d = 0
for i in range(len(a)):
    if a[i].isupper():
        ualpha += 1
        alpha += 1
        print(a[i],"is an alphabet and uppercase")
    elif a[i].islower():
        lalpha += 1
        alpha += 1
        print(a[i], "is an alphabet and lowercase")
    elif a[i] == " ":
        sp += 1
        print(a[i], "is a blank/space character")
    elif a[i].isnumeric():
        d += 1
        print(a[i], "is a number")
    else:
        print(a[i], "is a special/invalid character")
print('There are',alpha,'Alphabet(s) of which',lalpha,'are lowercase',ualpha,'are uppercase',sp, 'spaces and',d,'digits')

#Output 12
Enter string: AbC @ 12
A is an alphabet and uppercase
b is an alphabet and lowercase
C is an alphabet and uppercase
  is a blank/space character
@ is a special/invalid character
  is a blank/space character
1 is a number
2 is a number
There are 3 Alphabet(s) of which 1 are lowercase 2 are uppercase 2 spaces and 2 digits


#Source Code 13
a = 'Welcome to the World of Artificial Intelligence'
lista = a.split()
llista = len(lista)
clist = []
for i in range(llista):
    wrd = lista[i]
    if wrd[0].isupper():
        clist.append(wrd)
for i in range(len(clist)):
    print(clist[i])

#Output 13
Welcome
World
Artificial
Intelligence


#Source Code 14
a = [10,11,12,13,14,15]
for i in a:
    if i%2 != 0:
        a.remove(i)
print("The final list is")
print(a)

#Output 14
The final list is
[10, 12, 14]


#Source Code 15
a = [20,11,12,13,14,15]
a.sort()
print("Second largest value is", a[len(a)-2])

#Output 15
Second largest value is 15


#Source Code 16
a = [5,4,8,2,3,7,2,0]
s = 0
for i in range(len(a)):
    s += a[i]
print('The cumilative sum is',s)

#Output 16
The cumilative sum is 31


#Source Code 17
a = [5,4,8,2,3,7,2,0]
b = set(a)
b = list(b)
for i in range(len(b)):
    tempv = 0
    for n in range(len(a)):
        if b[i] == a[n]:
            tempv += 1
    print(b[i],"-",tempv)

#Output 17
0 - 1
2 - 2
3 - 1
4 - 1
5 - 1
7 - 1
8 - 1


#Source Code 18
a = input("Enter a sectence: ")
lista = a.split()
llista = len(lista)
clist = []
for i in range(llista):
    wrd = lista[i]
    if wrd[0] == 'A':
        print(wrd)

#Output 18
Enter a sectence: Apple products have An Apple logo in them
Apple
An
Apple


#Source Code 19
a = [42,53,96,47,33,21,83]
s = 0
for i in range(len(a)):
    aa = str(a[i])
    laa = len(aa)-1
    if aa[laa] == '3':
        s += a[i]
print(s)

#Output 19
169


#Source code 20
a = [-2,5,-6,8,1,4]
a.sort()
a.reverse()
print(a)

#Output 20
[8, 5, 4, 1, -2, -6]


#Source Code 21
a = [3,7,5,6,14,8,12,21]
for i in range(len(a)):
    if a[i] % 7 == 0:
        #print(ab)
        a[i],a[i-1] = a[i-1],a[i]
    else:
        pass

print(a)

#Output 21
[7, 3, 5, 14, 6, 8, 21, 12]


#Source Code 22
a = []
aa = 1
print("Enter numbers below")
print("Enter 0 to stop")
while aa != 0:
    aa = int(input("Enter number: "))
    a.append(aa)

a = tuple(a)
print(a)

#Output 22
Enter numbers below
Enter 0 to stop
Enter number: 3
Enter number: 4
Enter number: 5
Enter number: 2
Enter number: 0
(3, 4, 5, 2, 0)


#Source Code 23
sec = []
stre = []
n = int(input("How much sections? "))
for i in range(1,n+1):
    secst = "Enter section " + str(i) + " : "
    isec = input(secst)
    strest = "Enter Stream of "+isec+": "
    istre = input(strest)
    sec.append(isec)
    stre.append(istre)
print()
print("Section\t\t\tStream")
for i in range(len(sec)):
    print(sec[i]+"\t\t\t"+stre[i])

#Output 23
How much sections? 3
Enter section 1 : A
Enter Stream of A: Engineering
Enter section 2 : B
Enter Stream of B: Medical
Enter section 3 : C
Enter Stream of C: Commerce
Section                 Stream
A                       Engineering
B                       Medical
C                       Commerce

#Source code 24
country = []
country_capital = []
country_currency = []
n = int(input("How much countries?: "))
for i in range(1,n+1):
    contst = "Enter Country " + str(i) + " : "
    cont = input(contst)
    concaptst = "Enter Capital of "+cont+": "
    concapt = input(concaptst)
    concurst = "Enter Currency of "+cont+": "
    concur = input(concurst)
    country.append(cont)
    country_capital.append(concapt)
    country_currency.append(concur)

conandcap = dict(zip(country, country_capital))
conandcurr= dict(zip(country,country_currency))
st = """
Good! We have stored the values!
Now to access, choose from following
    1. Get Data in tabular form
    2. Get Captial and Currency by providing a country name
"""
print(st)
qu = int(input())
if qu == 1:
    print('Country\t\t\tCapital\t\t\tCurrency')
    for i in range(len(country)):
        scon = country[i]
        sconcap = country_capital[i]
        sconcurr = country_currency[i]
        print(scon,"\t\t",sconcap,"\t\t",sconcurr)
elif qu == 2:
    c = input("Enter Country's name: ")
    scap = conandcap.get(c)
    scurr = conandcurr.get(c)
    if scap == None and scurr == None:
        print("Country not found")
        quit()
    elif scap == '':
        print("Capital was not entered")
        quit()
    elif scurr == '':
        print("Currency was not entered")
        quit()
    else:
        print('The captial and currency of',c,"is",scap,"and",scurr)

#Output 24 (1)
How much countries?: 2
Enter Country 1 : America
Enter Capital of America: Washington DC
Enter Currency of America: American Dollars
Enter Country 2 : India
Enter Capital of India: Delhi
Enter Currency of India: Indian Rupees

Good! We have stored the values!
Now to access, choose from following
    1. Get Data in tabular form
    2. Get Captial and Currency by providing a country name

1
Country                 Capital                 Currency
America                          Washington DC                   American Dollars
India                    Delhi                   Indian Rupees

#Output 24 (2)
How much countries?: 2
Enter Country 1 : America
Enter Capital of America: Washington DC
Enter Currency of America: American Dollars
Enter Country 2 : India
Enter Capital of India: Delhi
Enter Currency of India: Indian Rupees

Good! We have stored the values!
Now to access, choose from following
    1. Get Data in tabular form
    2. Get Captial and Currency by providing a country name

2
Enter Country's name: America
The captial and currency of America is Washington DC and American Dollars
'''
