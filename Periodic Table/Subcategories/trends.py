atomicnumber = int(input("Enter Atomic number of Element 1: "))
gvar = 0
ge2 = 0
pvar = 0
pe2 = 0
thelist = []

#Updating all the group numbers
group1 = [1,3,11,19,37,55,87]
group2 = [4,12,20,38,56,88]
group3 = [21,39,57,89]
group4 = [22,40,72,104]
"""
Only Groups 1 2 3 4 and 13 have unique pattern. Remaining can be just made with a forloop and adding  for each element
which is done below
Initially, empty sets are given for groups which have repeating pattern
Then comes the forloop
"""
group5 = []
group6 = []
group7 = []
group8 = []
group9 = []
group10 = []
group11 = []
group12 = []
group13 = [5,13,31,49,81,113]
group14 = []
group15 = []
group16 = []
group17 = []
group18 = [2]
for number in group4:
    group5.append(number+1)
    group6.append(number+2)
    group7.append(number+3)
    group8.append(number+4)
    group9.append(number+5)
    group10.append(number+6)
    group11.append(number+7)
    group12.append(number+8)
for number in group13:
    group14.append(number + 1)
    group15.append(number + 2)
    group16.append(number + 3)
    group17.append(number + 4)
    group18.append(number + 5)
# Updating all the period numbers
period1 = [
    1,
    2
]
period2 = [3,4,5,6,7,8,9,10]
period3 = []
period4 = []
period5 = []
period6 = [55,56,57]
period7 = []
"""
This section is also similar to the earlier multi-line comment except tha it is for periods and not groups
"""
for number in period2:
    period3.append(number + 8)
for number in range(19,37):
    period4.append(number)
for number in period4:
    period5.append(number + 18)
for number in range(72,87):
    period6.append(number)
for number in period6:
    period7.append(number + 32)
group = 0
period = 0
"""
Now, we tell Python that if the given Integer lies in 
the list group1, then the variable group will be integer 1 and so on
"""
if atomicnumber in group1:
    group = 1
elif atomicnumber in group2:
    group = 2
elif atomicnumber in group3:
    group = 3
elif atomicnumber in group4:
    group = 4
elif atomicnumber in group5:
    group = 5
elif atomicnumber in group6:
    group = 6
elif atomicnumber in group7:
    group = 7
elif atomicnumber in group8:
    group = 8
elif atomicnumber in group9:
    group = 9
elif atomicnumber in group10:
    group = 10
elif atomicnumber in group11:
    group = 11
elif atomicnumber in group12:
    group = 12
elif atomicnumber in group13:
    group = 13
elif atomicnumber in group14:
    group = 14
elif atomicnumber in group15:
    group = 15
elif atomicnumber in group16:
    group = 16
elif atomicnumber in group17:
    group = 17
elif atomicnumber in group18:
    group = 18
"""
Similar to the group allotment, down below,
we go on with the Period Allotment
"""
if atomicnumber in period1:
    period = 1
elif atomicnumber in period2:
    period = 2
elif atomicnumber in period3:
    period = 3
elif atomicnumber in period4:
    period = 4
elif atomicnumber in period5:
    period = 5
elif atomicnumber in period6:
    period = 6
elif atomicnumber in period7:
    period = 7
gvar = group
pvar = period
print(group, period)
print(gvar, pvar)



element2 = int(input("Enter Atomic number of Element 2: "))
