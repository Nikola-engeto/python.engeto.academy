

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
USERS = {
    'bob' : '123' ,
    'ann' : 'pass123' ,
    'mike' : 'password123' ,
    'liz' : 'pass123'}
USERS_lst = list(USERS.keys())

if (USERNAME in USERS_lst) and PASSWORD == USERS[USERNAME]:
    print('We have 3 texts to be analyzed')

    choosen_text = input('Enter a number between 1 and 3 to select:')
    print('-' * 40)
    CHT = int(choosen_text) - 1


    splited_text = TEXTS[CHT].split()
    splited_text1 = [i.strip(',.') for i in splited_text]

    print('-' * 40)

    print('There are ' + str(len(splited_text1)) + ' words in the selected text.')


    sumof_numbers = 0
    num_of_title_words = 0
    num_of_upper_words = 0
    num_of_lower_words = 0
    num_of_digit_words = 0
    stats_of_lines = {}
    while splited_text1:
        word = splited_text1.pop(0)
        if word.isnumeric():
            sumof_numbers = int(sumof_numbers) + int(word)
        if word.istitle():
            num_of_title_words = num_of_title_words + 1
        if word.isupper():
            num_of_upper_words = num_of_upper_words + 1
        if word.islower():
            num_of_lower_words = num_of_lower_words + 1
        if word.isdigit():
            num_of_digit_words = num_of_digit_words + 1
        lenght_of_word = len(word)
        # number of the words of the same lenght
        PSORD = stats_of_lines.setdefault(lenght_of_word, 0)
        stats_of_lines[lenght_of_word] = PSORD + 1

    print('There are ' + str(num_of_title_words) + ' titlecase words.')
    print('There are ' + str(num_of_upper_words) + ' uppercase words.')
    print('There are ' + str(num_of_lower_words) + ' lowercase words.')
    print('There are ' + str(num_of_digit_words) + ' digit strings')

    ser_stats_of_lines = stats_of_lines.items()
    for value, category in sorted(ser_stats_of_lines):
        print(value, '*' * category, category)
        print('-' * 40)

    # count the total sum of the numbers in the choosen text

    print('If we summed all the numbers in this text we would get: ' + str(sumof_numbers))

else:
    print('The password or name is wrong')

