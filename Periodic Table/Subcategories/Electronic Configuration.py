from findelement import findingelement
def electrons():    
    global group1,group2,group3,group4,group5,group6,group7,group8,group9,group10,group11,group12,group13,group14,group15,group16,group17,group18
    global period1,period2,period3,period4,period5,period6,period7
    global alkalimet,alkaliemet,halo,inertg,trans,posttrans,lan,act,mettaloid,reactnmetal,unknownprop

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

    """
    Now comes the type of element category
    Elements in the periodictable have some characteristics based on their source, atomic structure etc
    They are:
    Alkali Metals,
    Alali Earth Metals,
    Lanthanoids,
    Actinoids
    Halogens,
    Mettaloids,
    Transition Elements,
    Post Trasition Elements,

    Some elements are known to have unknown properties
    Down below, We will put the atoms which come under corresponding Types
    """
    #alkalimetals
    alkalimet = [3,11,19,37,55,87]

    #alkali earth metals
    alkaliemet = group2
    #inert gases
    inertg = group18

    #lanthanoids
    lan = []
    for number in range(57,72):
        lan.append(number)
    #actinoids
    act = []
    for number in range(89,104):
        act.append(number)
    #halogens
    halo = group17
    #mettaloids
    mettaloid = [5,14,32,33,51,52,85]

    # post transition elements
    posttrans = [13,31,49,81,50,82,83,84]
    # reactive non metals
    reactnmetal = [1,6,7,8,9,15,16,17,34,35,53]

    #transition metals
    trans = [21,39,27,45,77,28,46,78,29,47,79]
    trans = trans + group4 + group5 + group6 + group7 + group8 + group12

    #elements with unknown properties
    unknownprop = [109,110,111,113,114,115,116]

    # Organizing several groups to their respective block(s/p/d/f)
    sblock = group1 + group2
    pblock = group13 + group14 + group15 + group16 + group17 + group18
    dblock = group3 + group4 + group5 + group6 + group7 + group8 + group9 + group10 + group11 + group12
    fblock = lan + act


    """
    Here is where the real process comes.
    Initially the following variables group, period, type and block are defined to store the
    Group number, Period Number, Type in which it falls(alkali, halogens, etc) and its block
    Also as it is harder to refer the block name each time in future, a new variable blockvalue
    is defined to store a unique number for each block
    """

    group = 0
    period = 0
    type = ""
    block = ""
    blockvalue = 0

    #getting input from user
    atomicnumber = int(input("Enter Atomic Number: "))
    findingelement(atomicnumber)
    
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

    # Doing the Type allotment
    if atomicnumber in alkalimet:
        type = "Alkali Metals"
    elif atomicnumber in alkaliemet :
        type = "Alkali Earth Metals"
    elif atomicnumber in inertg:
        type = "Inert / Noble gas"
    elif atomicnumber in lan:
        type = "Lanthanoids"
    elif atomicnumber in act:
        type = "Actinoids"
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

    # doing the block identification
    
    if atomicnumber in sblock:
        block = "S-Block"
        blockvalue = 1
    elif atomicnumber in pblock:
        block = "P-Block"
        blockvalue = 2
    elif atomicnumber in dblock:
        block = "D-Block"
        blockvalue = 3
    elif atomicnumber in fblock:
        block = "F-Block"
        blockvalue = 4


    """
    Now things are getting complicated.
    Let's take the actual electronic configuration of the Nobel gases Helium, Neon, Argon, Krypton, Xenon, Radon and not Oganesson
    because, 
    for every element in the periodic table (not H and He) has a prefix i.e. the actual E.C of the before nobel gas.
    As there are no elements beyond 118, Oganesson is not taken

    E.C OF B4 INERTGAS + E.C OF GIVEN ELEMENT (MUST BE TAKEN FROM STARING OF IT'S PERIOD) = REQUIRED E.C
    
    Now we put the E.C strings into their respective variables
    """

    rn = "1s2 2s2 2p6 3s2 3p6 4s2 4p6 3d10 4f14 5s2 5p6 4d10 6s2 6p6"   
    xe = "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6"    
    kr = "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6" 
    ar = "1s2 2s2 2p6 3s2 3p6"  
    ne = "1s2 2s2 2p6"  
    he = "1s2"
    
    """
    Now notice that all elements which is beyond Radon will have Radon's E.C as it's Prefix
    The same logic can be applied for
    """
    if atomicnumber > 86:
        pre1 = rn
    elif atomicnumber > 54:
        pre1 = xe
    elif atomicnumber > 36:
        pre1 = kr
    elif atomicnumber > 18:
        pre1 = ar
    elif atomicnumber > 10:
        pre1 = ne
    elif atomicnumber > 2:
        pre1 = he

    #when element in p block
    def ecp():
        pp2 = [
        5,
        6,
        7,
        8,
        9,
        10
        ]

        pp3 = []
        pp4 = []
        pp5 = []
        pp6 = []
        pp7 = []

        for number in pp2:
            pp3.append(number + 8)
            pp4.append(number + 26)
            pp5.append(number + 44)
            pp6.append(number + 76)
            pp7.append(number + 108)

        gp1 = [5,13,31,49,81,113]

        gp2 = []
        gp3 = []
        gp4 = []
        gp5 = []
        gp6 = []

        for number in gp1 :
            gp2.append(number + 1)
            gp3.append(number + 2)
            gp4.append(number + 3)
            gp5.append(number + 4)
            gp6.append(number + 5)

        gp = 0
        pp = 0

        if atomicnumber in gp1 :
            gp = 1
        elif atomicnumber in gp2:
            gp = 2
        elif atomicnumber in gp3:
            gp = 3
        elif atomicnumber in gp4:
            gp = 4
        elif atomicnumber in gp5:
            gp = 5
        elif atomicnumber in gp6:
            gp = 6

        rd = "1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10" 
        xe = "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 " 
        kr = "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 "   
        ar = "1s2 2s2 2p6 3s2 3p6 3d10 "    
        ne = "1s2 2s2 2p6"  
        he = "1s2"  
        preig = ""
        if atomicnumber in pp2:
            pp = 2
            preig = he
        elif atomicnumber in pp3:
            pp = 3
            preig = ne
        elif atomicnumber in pp4:
            pp = 4
            preig = ar
        elif atomicnumber in pp5:
            pp = 5
            preig = kr
        elif atomicnumber in pp6:
            pp = 6
            preig = xe
        elif atomicnumber in pp7:
            pp = 7
            preig = rd
        ec = preig + str(pp)+"s2 "+str(pp) + "p" + str(gp)
        print(ec)
    #when element in f block
    def ecf():
        lanpref = "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 6s2 "
        actpref = "1s2 2s2 2p6 3s2 3p6 4s2 4p6 4d10 4f14 5s2 5p6 6s2 6p6 7s2 "
        g1 = [58,59,60,61,62,63,67,68,69,70]
        g2 = [97,98,99,100,101,102]

        g3 = [91,92,96,103]

        dict1 = {
        66: lanpref + "4f10 5d1 6s2",
        71: lanpref + "4f14 5d1 6s2",
        90: actpref + "5f0 6d2 7s2",
        94: actpref + "5f6 6d0 7s2",
        95: actpref + "5f6 6do 7s2"
        }
        num1 = 0
        if atomicnumber in g1:
            num = atomicnumber-56
            ec = lanpref+"4f"+str(num1)+" 5d0 6s2"
        elif atomicnumber in g2:
            num1 = atomicnumber-88
            ec = actpref+"5f"+ str(num1) + " 6d0 7s2"
        elif atomicnumber in g3:
            num1 = atomicnumber-89
            ec = actpref + "5f" + str(num1) + " 6d0 7s1"

        if atomicnumber == 64 or 65:
            ec = lanpref + "4f9 5d0 6s2"
        print(ec)

    #while element in d block
    def ecd():
        pd3 = []
        pd4 = []
        pd5 = [56]
        pd6 = [89]

        for num in range(21,31):
            pd3.append(num)
            pd4.append(num+18)
        for num in range(72,81):
            pd5.append(num)
            pd6.append(num+32)

        gd1 = [
        21,
        39,
        57,
        89
        ]

        gd2 = [
        22,
        40,
        72,
        104
        ]

        gd3 = []
        gd4 = []
        gd5 = []
        gd6 = []
        gd7 = []
        gd8 = []
        gd9 = []
        gd10 = []

        for num in gd2:
            gd3.append(num+1)
            gd4.append(num+2)
            gd5.append(num+3)
            gd6.append(num+4)
            gd7.append(num+5)
            gd8.append(num+6)
            gd9.append(num+7)
            gd10.append(num+8)

        pref = ""
        pd = 0
        if atomicnumber in pd3:
            pref = ar
            pd = 3
        elif atomicnumber in pd4:
            pref = kr
            pd = 4
        elif atomicnumber in pd5:
            pref = xe
            pd = 5
        elif atomicnumber in pd6:
            pref = rn
            pd = 6

        gd = 0
        if atomicnumber in gd1:
            gd = 1
        elif atomicnumber in gd2:
            gd = 2
        elif atomicnumber in gd3:
            gd = 3
        elif atomicnumber in gd4:
            gd = 4
        elif atomicnumber in gd5:
            gd = 5
        elif atomicnumber in gd6:
            gd = 6
        elif atomicnumber in gd7:
            gd = 7
        elif atomicnumber in gd8:
            gd = 8
        elif atomicnumber in gd9:
            gd = 9
        elif atomicnumber in gd10:
            gd = 10

        g1 = (24,29,41,42,44,45,46,47,78,79,110,111)
        dictg1 = {
        24: pref + "3d5 4s1",
        29: pref + "3d10 4s1",
        41: pref + "4d4 5s1",
        42: pref + "4d5 5s1",
        44: pref + "4d7 5s1",
        45: pref + " 4d8 5s1",
        46: pref + "4d10",
        47: pref + "4d10 5s1",
        78: pref + "5d9 6s1",
        79: pref + "5d10 6s1",
        110: "6d9  7s1",
        111: "6d9  7s1"
        }


        if atomicnumber in g1:
            ec = dictg1.get(atomicnumber, "E.C not available")

        elif atomicnumber in range(72,81) or  range(104,113):
            ec = pref + " " + str(pd-1) + "f14 " + str(pd) + "d" + str(gd) + " " + str(pd + 1) + "s2"

        else:
            ec = pref + "  " + str(pd)  + "d" + str(gd) + " " + str(pd + 1) + "s2"
        print(ec)

    if blockvalue == 1:
        ec = pre1 + " "+str(period)+"s"+str(group)
        print(ec)
    elif blockvalue == 2:
        ecp()
    elif blockvalue == 3:
        ecd()
    elif blockvalue == 4:
        ecf()

while 1 > 0:
    electrons()