

print("Welcome to Periodic Table Calculator \nYou can calculate the periodic number, group number, valency of a given Atomic number")
Z = int(input("Enter Atomic Number: "))

sc = 0
ve = 0
gn = 0
c = 0
c2 = 0

noble_gases = [
	2,
	8,
	18,
	36,
	54,
	86,
	118
]

for lan in range(58,72):
	if str(lan) in str(Z):
		c2 = 0
	
for act in range(90,104):
	if str(act) in str(Z):
		c2 = 1


if c2 == 1:
	print("The Application is not applicable for Lantanoids and Actinoids ")
	quit()
elif Z > 118:
	print("ERROR \nThe Periodic table only contains 118 elements")


elif Z >= 100:
	sc = 6
	gn = Z-100
	ve = gn

elif Z >= 68:
	sc = 5
	gn = Z-68
	ve = gn

elif Z > 36:
	sc = 4
	gn = Z-36
	ve = gn

elif Z == 36:
	sc = 4
	gn = 18
	ve = 0


elif Z > 18:
	sc = 4
	gn = Z-18
	ve = gn

elif Z == 18:
	sc = 4
	gn = 18
	ve = 0

elif Z > 10:
	sc = 3
	gn = Z-10
	ve = gn

elif Z == 10:
	sc = 3
	gn = 10
	ve = 0

elif Z > 2:
	sc = 2
	gn = Z-2
	ve = gn

elif Z == 2:
	sc = 1
	gn = 18
	ve = 0
	
elif Z == 1:
	sc = 1
	gn = 1

elif Z == 0:
	sc = 0
	gn = 0

while gn > 18:
	gn = gn-18


while ve > 8 :
	ve = ve - 8

if Z == 10 or 18 or 36:
	c = -1

print("The Group Number of given element is "+str(gn)+" \nand the Period Number of given element is "+str(sc+c))
print("The valency/number of valence  electron of given element is "+str(ve))
