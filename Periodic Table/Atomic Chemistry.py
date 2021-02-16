# Program to solve Chemistry problems
import time
a = 1

print("Welcome to Periodic Table Calculator")
print("You can find the name of element, periodic number, group number, electronic configuration and valency of a given Atomic number")

def calculate():
    try:
        # Get input from user
        #time.sleep(3)
        atomicnumber = int(input("Enter Atomic Number: "))
    
        # To display element's name and their symbol:
        # we create a dictionary to store the information
    
        elements = {
            1: "Hydrogen  H",
            2: "Helium  He",
            3: "Lithium  Li",
            4: "Beryllium  Be",
            5: "Boron  B",
            6: "Carbon  C",
            7: "Nitrogen  N",
            8: "Oxygen  O",
            9: "Fluorine  F",
            10: "Neon  Ne",
            11: "Sodium  Na",
            12: "Magnesium  Mg",
            13: "Aluminium  Al",
            14: "Silicon  Si",
            15: "Phosphorus  P",
            16: "Sulfur  S",
            17: "Chlorine  Cl",
            18: "Argon  Ar",
            19: "Potassium  K",
            20: "Calcium  Ca",
            21: "Scandium  Sc",
            22: "Titanium  Ti",
            23: "Vanadium  V",
            24: "Chromium  Cr",
            25: "Manganese  Mn",
            26: "Iron  Fe",
            27: "Cobalt  Co",
            28: "Nickel  Ni",
            29: "Copper  Cu",
            30: "Zinc  Zn",
            31: "Gallium  Ga",
            32: "Germanium  Ge",
            33: "Arsenic  As",
            34: "Selenium  Se",
            35: "Bromine  Br",
            36: "Krypton  Kr",
            37: "Rubidium  Rb",
            38: "Strontium  Sr",
            39: "Yttrium  Y",
            40: "Zirconium  Zr",
            41: "Niobium  Nb",
            42: "Molybdenum  Mo",
            43: "Technetium  Tc",
            44: "Ruthenium  Ru",
            45: "Rhodium  Rh",
            46: "Palladium  Pd",
            47: "Silver  Ag",
            48: "Cadmium  Cd",
            49: "Indium  In",
            50: "Tin  Sn",
            51: "Antimony  Sb",
            52: "Tellurium  Te",
            53: "Iodine  I",
            54: "Xenon  Xe",
            55: "Caesium  Cs",
            56: "Barium  Ba",
            57: "Lanthanum  La",
            58: "Cerium  Ce",
            59: "Praseodymium  Pr",
            60: "Neodymium  Nd",
            61: "Promethium  Pm",
            62: "Samarium  Sm",
            63: "Europium  Eu",
            64: "Gadolinium  Gd",
            65: "Terbium  Tb",
            66: "Dysprosium  Dy",
            67: "Holmium  Ho",
            68: "Erbium  Er",
            69: "Thulium  Tm",
            70: "Ytterbium  Yb",
            71: "Lutetium  Lu",
            72: "Hafnium  Hf",
            73: "Tantalum  Ta",
            74: "Tungsten  W",
            75: "Rhenium  Re",
            76: "Osmium  Os",
            77: "Iridium  Ir",
            78: "Platinum  Pt",
            79: "Gold  Au",
            80: "Mercury  Hg",
            81: "Thallium  Tl",
            82: "Lead  Pb",
            83: "Bismuth  Bi",
            84: "Polonium  Po",
            85: "Astatine  At",
            86: "Radon  Rn",
            87: "Francium  Fr",
            88: "Radium  Ra",
            89: "Actinium  Ac",
            90: "Thorium  Th",
            91: "Protactinium  Pa",
            92: "Uranium  U",
            93: "Neptunium  Np",
            94: "Plutonium  Pu",
            95: "Americium  Am",
            96: "Curium  Cm",
            97: "Berkelium  Bk",
            98: "Californium  Cf",
            99: "Einsteinium  Es",
            100: "Fermium  Fm",
            101: "Mendelevium  Md",
            102: "Nobelium  No",
            103: "Lawrencium  Lr",
            104: "Rutherfordium  Rf",
            105: "Dubnium  Db",
            106: "Seaborgium  Sg",
            107: "Bohrium  Bh",
            108: "Hassium  Hs",
            109: "Meitnerium  Mt",
            110: "Darmstadtium  Ds",
            111: "Roentgenium  Rg",
            112: "Copernicium  Cn",
            113: "Nihonium Nh",
            114: "Flerovium  Fl",
            115: "Moscovium Mc",
            116: "Livermorium  Lv",
            117: "Tennessine Ts",
            118: "Oganesson Og"
        }
    
        # To display the name and symbol:
        # we use get() function
    
        element = elements.get(atomicnumber)
    
        # To display element's Electronic Configuration configuration:
        # we create a dictionary to store the information
    
        elecconf = {
            1: "1s1",
            2: "1s2",
            3: "[He]2s1",
            4: "[He]2s2",
            5: "[He]2s2 2p1",
            6: "[He]2s2 2p2",
            7: "[He]2s2 2p3",
            8: "[He]2s2 2p4",
            9: "[He]2s2 2p5",
            10: "[He]2s2 2p6",
            11: "[Ne]3s1",
            12: "[Ne]3s2",
            13: "[Ne]3s2 3p1",
            14: "[Ne]3s2 3p2",
            15: "[Ne]3s2 3p3",
            16: "[Ne]3s2 3p4",
            17: "[Ne]3s2 3p5",
            18: "[Ne]3s2 3p6",
            19: "[Ar]4s1",
            20: "[Ar]4s2",
            21: "[Ar]3d1 4s2",
            22: "[Ar]3d2 4s2",
            23: "[Ar]3d3 4s2",
            24: "[Ar]3d3 4s1",
            25: "[Ar]3d5 4s2",
            26: "[Ar]3d6 4s2",
            27: "[Ar]3d7 4s2",
            28: "[Ar]3d8 4s2",
            29: "[Ar]3d10 4s1",
            30: "[Ar]3d10 4s2",
            31: "[Ar]3d10 4s2 4p1",
            32: "[Ar]3d10 4s2 4p2",
            33: "[Ar]3d10 4s2 4p3",
            34: "[Ar]3d10 4s2 4p4",
            35: "[Ar]3d10 4s2 4p5",
            36: "[Ar]3d10 4s2 4p6",
            37: "[Kr]5s1",
            38: "[Kr]5s2",
            39: "[Kr]4d1 5s2",
            40: "[Kr]4d2 5s2",
            41: "[Kr]4d4 5s1",
            42: "[Kr]4d5 5s1",
            43: "[Kr]4d5 5s2",
            44: "[Kr]4d7 5s1",
            45: "[Kr]4d8 5s1",
            46: "[Kr]4d10",
            47: "[Kr]4d10 5s1",
            48: "[Kr]4d10 5s2",
            49: "[Kr]4d10 5s2 5p1",
            50: "[Kr]4d10 5s2 5p2",
            51: "[Kr]4d10 5s2 5p3",
            52: "[Kr]4d10 5s2 5p4",
            53: "[Kr]4d10 5s2 5p5",
            54: "[Kr]4d10 5s2 5p6",
            55: "[Xe]6s1",
            56: "[Xe]6s2",
            57: "[Xe]5d1 6s2",
            58: "[Xe]4f1 5d1 6s2",
            59: "[Xe]4f3 6s2",
            60: "[Xe]4f4 6s2",
            61: "[Xe]4f5 6s2",
            62: "[Xe]4f6 6s2",
            63: "[Xe]4f7 6s2",
            64: "[Xe]4f7 5d1 6s2",
            65: "[Xe]4f9 6s2",
            66: "[Xe]4f10 6s2",
            67: "[Xe]4f11 6s2",
            68: "[Xe]4f12 6s2",
            69: "[Xe]4f13 6s2",
            70: "[Xe]4f14 6s2",
            71: "[Xe]4f14 5d1 6s2",
            72: "[Xe]4f14 5d2 6s2",
            73: "[Xe]4f14 5d3 6s2",
            74: "[Xe]4f14 5d4 6s2",
            75: "[Xe]4f14 5d5 6s2",
            76: "[Xe]4f14 5d6 6s2",
            77: "[Xe]4f14 5d7 6s2",
            78: "[Xe]4f14 5d9 6s1",
            79: "[Xe]4f14 5d9 6s2",
            80: "[Xe]4f14 5d10 6s2",
            81: "[Xe]4f14 5d10 6s2 6p1",
            82: "[Xe]4f14 5d10 6s2 6p2",
            83: "[Xe]4f14 5d10 6s2 6p3",
            84: "[Xe]4f14 5d10 6s2 6p4",
            85: "[Xe]4f14 5d10 6s2 6p5",
            86: "[Xe]4f14 5d10 6s2 6p6",
            87: "[Rn]7s1",
            88: "[Rn]7s2",
            89: "[Rn]6d1 7s2",
            90: "[Rn]6d2 7s2",
            91: "[Rn]5f2 6d1 7s2",
            92: "[Rn]5f3 6d1 7s2",
            93: "[Rn]5f4 6d1 7s2",
            94: "[Rn]5f6 7s2",
            95: "[Rn]5f7 7s2",
            96: "[Rn]5f7 6d1 7s2",
            97: "[Rn]5f9 7s2",
            98: "[Rn]5f10 7s2",
            99: "[Rn]5f11 7s2",
            100: "[Rn]5f12 7s2",
            101: "[Rn]5f13 7s2",
            102: "[Rn]5f14 7s2",
            103: "[Rn]5f14 7s2 7p1",
            104: "[Rn]5f14 6d2 7s2",
            105: "[Rn]5f14 6d3 7s2     (Predicted)",
            106: "[Rn]5f14 6d4 7s2     (Predicted)",
            107: "[Rn]5f14 6d5 7s2     (Predicted)",
            108: "[Rn]5f14 6d6 7s2     (Predicted)",
            109: "[Rn]5f14 6d7 7s2     (Predicted)",
            110: "[Rn]5f14 6d9 7s1     (Predicted)",
            111: "[Rn]5f14 6d10 7s1     (Predicted)",
            112: "[Rn]5f14 6d10 7s2     (Predicted)",
            113: "[Rn]5f14 6d10 7s2 7p1     (Predicted)",
            114: "[Rn]5f14 6d10 7s2 7p2     (Predicted)",
            115: "[Rn]5f14 6d10 7s2 7p3     (Predicted)",
            116: "[Rn]5f14 6d10 7s2 7p4     (Predicted)",
            117: "[Rn]5f14 6d10 7s2 7p5     (Predicted)",
            118: "[Rn]5f14 6d10 7s2 7p6     (Predicted)",
        }
    
        # To display the name and symbol:
        # we use get() function
    
        config = elecconf.get(atomicnumber)
    
        # To display element's group number:
        # we create individual lists for individual groups to store the information
    
        group1 = [1, 3, 11, 19, 37, 55, 87]
        group2 = [4, 12, 20, 38, 56, 88]
        group3 = [21, 39]
        group4 = [22, 40, 72, 104]
        group5 = [23, 41, 73, 105]
        group6 = [24, 42, 74, 106]
        group7 = [25, 43, 75, 107]
        group8 = [26, 44, 76, 108]
        group9 = [27, 45, 77, 109]
        group10 = [28, 46, 78, 110]
        group11 = [29, 47, 79, 111]
        group12 = [30, 48, 80, 112]
        group13 = [5, 13, 31, 49, 81, 113]
        group14 = [6, 14, 32, 50, 82, 114]
        group15 = [7, 15, 33, 51, 83, 115]
        group16 = [8, 16, 34, 52, 84, 116]
        group17 = [9, 17, 35, 53, 85, 117]
        group18 = [2, 10, 18, 36, 54, 86, 118]
    
        # To display element's period number:
        # we create individual lists for individual periods to store the information
    
        period1 = [1, 2]
        period2 = [3, 4, 5, 6, 7, 8, 9, 10]
        period3 = [11, 12, 13, 14, 15, 16, 17, 18]
        period4 = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 32, 34, 35, 36]
        period5 = [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]
        period6 = [55, 56, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]
        period7 = [87, 88, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118]
    
        # To display element's nature:
        # we create individual lists for individual types to store the information
    
        # alkalimetals
        alkalimet = [3, 11, 19, 37, 55, 87]
    
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
        mettaloid = [5, 14, 32, 33, 51, 52, 85]
    
        # post transition elements
        posttrans = [13, 31, 49, 81, 50, 82, 83, 84]
    
        # reactive non metals
        reactnmetal = [6, 7, 8, 9, 15, 16, 17, 34, 35, 53, 85, 117]
    
        # transition metals
        trans = group3 + group4 + group5 + group6 + group7 + group8 + group9 + group10 + group11 + group12
    
        # To display element'sblock:
        # we combine the groups into individual blocks using '+'
    
        sblock = group1 + group2
        pblock = group13 + group14 + group15 + group16 + group17 + group18
        dblock = group3 + group4 + group5 + group6 + group7 + group8 + group9 + group10 + group11 + group12
        fblock = lan + act
    
        # General form to define the variable
        group = 0
        period = 0
        type = ""
        block = ""
    
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
    
        # finding nature
        idn = 0
        if atomicnumber in alkalimet:
            type = "Alkali Metals"
        elif atomicnumber in alkaliemet:
            type = "Alkali Earth Metals"
        elif atomicnumber in inertg:
            type = "Inert / Noble gas"
        elif atomicnumber in lan:
            type = "Lanthanoids"
            idn = 1
        elif atomicnumber in act:
            type = "Actinoids"
            idn = 1
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
        elif atomicnumber > 118:
            idn = 2
        elif atomicnumber == 1:
            idn = 3
    
        # finding block
        if atomicnumber in sblock:
            block = "S-Block"
        elif atomicnumber in pblock:
            block = "P-Block"
        elif atomicnumber in dblock:
            block = "D-Block"
        elif atomicnumber in fblock:
            block = "F-Block"
    
        gn = 0
        ve = 0
        if atomicnumber == 118:
            gn = 18
            ve = 0
    
        elif atomicnumber >= 100:
            gn = atomicnumber - 100
            ve = gn
    
        elif atomicnumber == 86:
            gn = 18
            ve = 0
    
        elif atomicnumber >= 68:
            gn = atomicnumber - 68
            ve = gn
    
        elif atomicnumber == 54:
            gn = 18
            ve = 0
    
        elif atomicnumber > 36:
            gn = atomicnumber - 36
            ve = gn
    
        elif atomicnumber == 36:
            gn = 18
            ve = 0
    
    
        elif atomicnumber > 18:
            gn = atomicnumber - 18
            ve = gn
    
        elif atomicnumber == 18:
            gn = 18
            ve = 0
    
        elif atomicnumber > 10:
            gn = atomicnumber - 10
            ve = gn
    
        elif atomicnumber == 10:
            gn = 10
            ve = 0
    
        elif atomicnumber > 2:
            gn = atomicnumber - 2
            ve = gn
    
        elif atomicnumber == 2:
            gn = 18
            ve = 0
    
        elif atomicnumber == 1:
            gn = 1
    
        elif atomicnumber == 0:
            sc = 0
            gn = 0
    
        while gn > 18:
            gn = gn - 18
    
        while ve > 8:
            ve = ve - 8
    
        dictatm = {
            1: "1.008",
            2: "4.002",
            3: "6.942",
            4: "9.012",
            5: "10.812",
            6: "12.011",
            7: "14.007",
            8: "15.999",
            9: "18.998)",
            10: "20.179",
            11: "22.989",
            12: "24.305",
            13: "26.981",
            14: "28.085",
            15: "30.973",
            16: "32.062",
            17: "35.452",
            18: "39.948",
            19: "39.098",
            20: "40.078",
            21: "44.955",
            22: "47.867",
            23: "50.941",
            24: "51.996",
            25: "54.938",
            26: "55.845",
            27: "58.933",
            28: "58.693",
            29: "63.546",
            30: "65.382",
            31: "69.723",
            32: "72.630",
            33: "74.921",
            34: "78.964",
            35: "79.904",
            36: "83.798",
            37: "85.467",
            38: "87.624",
            39: "88.905",
            40: "91.224",
            41: "92.906",
            42: "95.962",
            43: "[98]1",
            44: "101.07(2)2",
            45: "102.90550(2)",
            46: "106.42(1)2",
            47: "107.8682(2)2",
            48: "112.411(8)2",
            49: "114.818(1)",
            50: "118.710(7)2",
            51: "121.760(1)2",
            52: "127.60(3)2",
            53: "126.90447(3)",
            54: "131.293(6)2 3",
            55: "132.9054519(2)",
            56: "137.327(7)",
            57: "138.90547(7)2",
            58: "140.116(1)2",
            59: "140.90765(2)",
            60: "144.242(3)2",
            61: "[145]1",
            62: "150.36(2)2",
            63: "151.964(1)2",
            64: "157.25(3)2",
            65: "158.92535(2)",
            66: "162.500(1)2",
            67: "164.93032(2)",
            68: "167.259(3)2",
            69: "168.93421(2)",
            70: "173.054(5)2",
            71: "174.9668(1)2",
            72: "178.49(2)",
            73: "180.94788(2)",
            74: "183.84(1)",
            75: "186.207(1)",
            76: "190.23(3)2",
            77: "192.217(3)",
            78: "195.084(9)",
            79: "196.966569(4)",
            80: "200.592(3)",
            81: "204.389 ",
            82: "207.2(1)2 4",
            83: "208.98040(1)1",
            84: "[209]1",
            85: "[210]1",
            86: "[222]1",
            87: "[223]1",
            88: "[226]1",
            89: "[227]1",
            90: "232.03806(2)1 2",
            91: "231.03588(2)1",
            92: "238.02891(3)1",
            93: "[237]1",
            94: "[244]1",
            95: "[243]1",
            96: "[247]1",
            97: "[247]1",
            98: "[251]1",
            99: "[252]1",
            100: "[257]1",
            101: "[258]1",
            102: "[259]1",
            103: "[262]1",
            104: "[267]1",
            105: "[268]1",
            106: "[269]1",
            107: "[270]1",
            108: "[269]1",
            109: "[278]1",
            110: "[281]1",
            111: "[281]1",
            112: "[285]1",
            113: "[286]1",
            114: "[289]1",
            115: "[288]1",
            116: "[293]1",
            117: "[294]1",
            118: "[294]1"
        }
    
        atmass = dictatm.get(atomicnumber, "Atomic Mass of the given element was not Predicted")

        # Displaying the answers
        if idn == 1:
            print("Element Name and symbol: " + str(element))

            print("Electronic Configuration configuration: " + str(config))
            print("Atomic Mass of given element is " + atmass)
            print("It has about " + str(atomicnumber) + " protons and electrons")
            print("It comes under " + block)
            print("It comes under " + type)
            print("The valency of the given element is " + str(ve))
            print("The Group Number and Period Number of given element cannot be calculated as it belongs to " + type)
        elif idn == 0:
            print("Element Name and symbol: " + str(element))

            print("Electronic Configuration configuration: " + str(config))
            print("Atomic Mass of given element is " + atmass)
            print("It has about " + str(atomicnumber) + " protons and electrons")
            print("The Group Number of given element is " + str(group) + "\nThe Period Number of given element is " + str(
                period))
            print("It comes under " + block)
            print("It comes under " + type)
            print("The valency of the given element is " + str(ve))
        elif idn == 2:
            print("Element not found")
            print("Only 118 Elements were discovered until 2020")
        elif idn == 3:
            print("Element Name and symbol: " + str(element))
            print("Electronic Configuration configuration: " + str(config))
            print("Atomic Mass of given element is " + atmass)
            print("It has about " + str(atomicnumber) + " protons and electrons")
            print("The Group Number of given element is " + str(group) + "\nThe Period Number of given element is " + str(
                period))
            print("It comes under " + block)
            print(
                "It has peculiar property such that it's exact nature cannot be determined \nBut it considered as a Non-metal")
            print("The valency of given element is 1")
        else:
            print("ERROR! \nContact the administrator")
       
    except ValueError:
        print(
            "Invalid or No Characters were entered. \nPlease Run the program again.\nIf the problem persists, contact the developer")
    
    except KeyboardInterrupt:
        print(
            "\nBAD COMBINATION: Ctrl + C was entered \nPlease Run the program again.\nIf the problem persists, contact the developer")
    
    except EOFError:
        print(
            "\nBAD COMBINATION: Ctrl + Z was entered \nPlease Run the program again.\nIf the problem persists, contact the developer")
    print("Press any letter followed by ENTER to exit the program else just press ENTER")
    op = input("")
    if op != "":
        print("Thank You for using our Periodic Table")
        print("Atomic Chemistry - Periodic Table")
        print("Copyright (c) STUDIES OVERLOADED")
        print("presented by Akash Shanmugaraj and Chandramouli M")
        exit()
    
while a == 1:
    calculate()