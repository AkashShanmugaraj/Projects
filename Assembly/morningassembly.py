import time
lastrollnum = int(input("What was the roll number of the boy/girl who did prayer(the first task) today?"))
names = {
    1 : 'D AAKASH',
    2 : 'C B ABIJITH KAARTHIGEYAN',
    3 : 'A ADIT PRASAD',
    4 : 'R ADITHYA NARAYANAN',
    5 : 'S AKASH',
    6 : 'BARATH GIRI C S',
    7 : 'JAYANTH S',
    8 : 'K LAKSHAN ANIRUDH',
    9 : 'M LOGANATH',
    10 : 'R MATHURANATHAN',
    11 : 'M RAJ RAGAVENDER',
    12 : 'ROHITH PRAKASH',
    13 : 'R ROSHAUN INFANT',
    14 : 'S SARVESH',
    15 : 'SARVESHWAR P G',
    16 : 'S SHIV SANJAY',
    17 : 'TARUN MURUGAN',
    18 : 'TARUN SELVARAJU',
    19 : 'VANSH JAIN',
    20 : 'V VISHNU',
    21 : 'C CHARU MITHRA',
    22 : 'DIVYADHARSHINI H',
    23 : 'M HARISA NANTHIKA',
    24 : 'HARSHINI T',
    25 : 'HARSHITHA V',
    26 : 'ILAKKIYA S',
    27 : 'JYOTHSNA A',
    28 : 'KEERTI',
    29 : 'MALAVIKA K MENON',
    30 : 'NANDHANA PRAKASH',
    31 : 'POOJITHA SAI MANIKANDAN',
    32 : 'PRACHI P',
    33 : 'RESHMA S',
    34 : 'RISHA R',
    35 : 'S RITHANYA',
    36 : 'P SADHIKAA SREE',
    37 : 'SRIYA SANTHANAM',
    38 : 'SWATHIKA SUBRAMANIAN',
    39 : 'M NITHU KRISHNAA',
    40 : 'NIVEDHA B'
}
print("Note Nivedha is considered as last in girls and Nithu Krishna is considered as last roll number in boys")
a = 'Morning Assembly\n1.Prayer-Adithya\n2.News-Akash S\n3.Thought for the day-Barath Giri\n4.Facts.-Jayanthn\5.Word of the day-Lakshan'
ppl = []
print("Next set of people are: ")
for i in range(lastrollnum+1,lastrollnum+6):
    ppl.append(names.get(i))
print('Morning Assembly\n1.Prayer-'+ppl[0]+'\n2.News-'+ppl[1]+'\n3.Thought for the day-'+ppl[2]+'\n4.Facts-'+ppl[3]+'\n5.Word of the day-'+ppl[4])
time.sleep(5)
