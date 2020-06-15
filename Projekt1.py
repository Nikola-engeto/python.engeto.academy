from typing import List

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

print('-' * 40)
print('Welcome to the app, please login:')
USERNAME = input('USERNAME: ')
PASSWORD = input('PASSWORD: ')
print('-' * 40)
uzivatele = {
    'bob' : '123' ,
    'ann' : 'pass123' ,
    'mike' : 'password123' ,
    'liz' : 'pass123'}
uzivatele_lst = list(uzivatele.keys())

if USERNAME in uzivatele_lst:
    if PASSWORD == uzivatele[USERNAME]:
        print('We have 3 texts to be analyzed')

        zvoleny_text = input('Enter a number between 1 and 3 to select:')
        print('-' * 40)
        ZT = int(zvoleny_text) - 1
        print(TEXTS[ZT])

        rozdeleny_text = TEXTS[ZT].split()
        print(rozdeleny_text)
        rozdeleny_text1 = [i.strip(',.') for i in rozdeleny_text]
        print(rozdeleny_text1)

        print('-' * 40)

        print('There are ' + str(len(rozdeleny_text1)) + ' words in the selected text.')


        soucet_cisel = 0
        pocet_title_slov = 0
        pocet_upper_slov = 0
        pocet_lower_slov = 0
        pocet_digit_slov = 0
        slovnik = {}
        while rozdeleny_text1:
            slovo = rozdeleny_text1.pop(0)
            if slovo.isnumeric():
                soucet_cisel = int(soucet_cisel) + int(slovo)
            if slovo.istitle():
                pocet_title_slov = pocet_title_slov + 1
            if slovo.isupper():
                pocet_upper_slov = pocet_upper_slov + 1
            if slovo.islower():
                pocet_lower_slov = pocet_lower_slov + 1
            if slovo.isdigit():
                pocet_digit_slov = pocet_digit_slov + 1
            delka_slova = len(slovo)
            # počet slov o rovnakej dlžke
            PSORD = slovnik.setdefault(delka_slova, 0)
            slovnik[delka_slova] = PSORD + 1

        print('There are ' + str(pocet_title_slov) + ' titlecase words.')
        print('There are ' + str(pocet_upper_slov) + ' uppercase words.')
        print('There are ' + str(pocet_lower_slov) + ' lowercase words.')
        print('There are ' + str(pocet_digit_slov) + ' digit strings')
        print(slovnik.items())

        ser_slovnik = slovnik.items()
        for hodnota, kategorie in sorted(ser_slovnik):
            print(hodnota, '*' * kategorie, kategorie)
            print('-' * 40)

        # spocitej soucet vsech cisel ve zvolenem textu

        print('If we summed all the numbers in this text we would get: ' + str(soucet_cisel))


    else:
        print('The password or name is wrong')
else:
    print('Uzivatel neni registrovan')
