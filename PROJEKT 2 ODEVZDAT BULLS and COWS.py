import random
number = []
pokusy = 0
#definice funkce, která nám zvolí náhodné číslo o délce 4 znaků

print('I have a 4-digit number for you!\n * Rule is to enter a '
      '4-digit number. \n * If you will enter right number on the '
      'right position you have gulls. \n * If you will guess the '
      'right number but not on right possition you have a '
      'cows. \n * So, you have to guess the right number on the '
      'right possition and get 4 gulls.\n LETS START \n ' , ("=" * 60))
def vytvorcislo():
    for i in range(4):
        y = random.randrange(0,9)
        number.append(y)
    if len(number) > len(set(number)):
        number.clear()
        vytvorcislo()

print('ENTER YOUR NUMBER')

def hra():
    global pokusy
    pokusy += 1
    cows_kravy = 0
    bulls_byci = 0
    choice = input('>>>>')
    guess = []
    for i in range(4):
        guess.append(int(choice[i]))
    for i in range(4):
        for z in range(4):
            if(guess[i] == number[z]):
                cows_kravy += 1
    for y in range(4):
        if guess[y] == number [y]:
            bulls_byci += 1

    print("Bulls" , bulls_byci , " Cows" , cows_kravy )
    print("×" * 60 )
    if(bulls_byci == 4):
        print("Congratulations! You WON in  : " , pokusy , "attempts")
    if(bulls_byci != 4):
        hra()

vytvorcislo()
hra()









