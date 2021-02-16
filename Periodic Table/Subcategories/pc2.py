# Updating all the group numbers


group1 = [
    1,
    3,
    11,
    19,
    37,
    55,
    87
]

group2 = [
    4,
    12,
    20,
    38,
    56,
    88
]

group3 = [
    21,
    39,
    57,
    89
]

group4 = [
    22,
    40,
    72,
    104
]
group5 = []
group6 = []
group7 = []
group8 = []
group9 = []
group10 = []
group11 = []
group12 = []
group13 = [
    5,
    13,
    31,
    49,
    81,
    113
]
group14 = []
group15 = []
group16 = []
group17 = []
group18 = [
    2
]

for number in group4:
    group5.append(number + 1)
    group6.append(number + 2)
    group7.append(number + 3)
    group8.append(number + 4)
    group9.append(number + 5)
    group10.append(number + 6)
    group11.append(number + 7)
    group12.append(number + 8)

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
period2 = [
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10
]
period3 = []
period4 = []
period5 = []
period6 = [
    55,
    56,
    57
]
period7 = []

for number in period2:
    period3.append(number + 8)
for number in range(19, 37):
    period4.append(number)
for number in period4:
    period5.append(number + 18)
for number in range(72, 87):
    period6.append(number)
for number in period6:
    period7.append(number + 32)

# alkalimetals
alkalimet = [
    3,
    11,
    19,
    37,
    55,
    87
]

# alkali earth metals
alkaliemet = group2
# inert gases
inertg = group18

# lanthanoids
lan = []
for number in range(57, 72):
    lan.append(number)
# actinoids
act = []
for number in range(89, 104):
    act.append(number)
# halogens
halo = group17
# mettaloids
mettaloid = [
    5,
    14,
    32,
    33,
    51,
    52,
    85,
    117
]

# different block element
sblock = group1 + group2
pblock = group13 + group14 + group15 + group16 + group17 + group18
dblock = group3 + group4 + group5 + group6 + group7 + group8 + group9 + group10 + group11 + group12
fblock = lan + act

# post transition elements
posttrans = [
    13,
    31,
    49,
    81,
    50,
    82,
    83,
    84
]

posttrans = posttrans + group12

# reactive non metals
reactnmetal = [
    1,
    6,
    7,
    8,
    9,
    15,
    16,
    17,
    34,
    35,
    53
]

# transition metals
trans = [
    21,
    39,
    27,
    45,
    77,
    28,
    46,
    78,
    29,
    47,
    79
]
trans = trans + group4 + group5 + group6 + group7 + group8

# elements with unknown properties
unknownprop = [
    109,
    110,
    111,
    113,
    114,
    115,
    116
]

group = 0
period = 0
type = ""
block = ""
atomicnumber = int(input("Enter Atomic Number: "))
# finding group
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

# finding period
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

uqn = 0
if atomicnumber in alkalimet:
    type = "Alkali Metals"
elif atomicnumber in alkaliemet:
    type = "Alkali Earth Metals"
elif atomicnumber in inertg:
    type = "Inert / Noble gas"
elif atomicnumber in lan:
    type = "Lanthanoids"
    uqn = 1
elif atomicnumber in act:
    type = "Actinoids"
    uqn = 2
elif atomicnumber in halo:
    type = "Halogen"
elif atomicnumber in mettaloid:
    type = "Mettaloid"
elif atomicnumber in posttrans:
    type = "Post Transition Metals"
elif atomicnumber in trans:
    type = "Transition Metals"
elif atomicnumber in reactnmetal:
    type = "Reactive Non-Metal"
elif atomicnumber in unknownprop:
    type = "Properties are unknown"
elif atomicnumber > 118:
    print("Only 118 Elements were discovered until 2020")

if atomicnumber in sblock:
    block = "S-Block"
elif atomicnumber in pblock:
    block = "P-Block"
elif atomicnumber in dblock:
    block = "D-Block"
elif atomicnumber in fblock:
    block = "F-Block"

if uqn == 1:
    print("It comes under "+type)
    print("The Group Number and Period Number of given element cannot be calculated as it belongs to "+type)
elif uqn == 2:
    print("It comes under "+type)
    print("The Group Number and Period Number of given element cannot be calculated as it belongs to "+type)
elif uqn == 0:
    print("The Group Number of given element is "+str(group)+"\nThe Period Number of given element is "+str(period))
    print("It comes under "+type)
