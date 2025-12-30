import random
import sys
while True:
    print('Welcome to the game!')
    a=random.randint(1,100)
    # print(a)
    count=7
    while count>0:
        try:
            b=int(input('Enter number:'))
        except ValueError:
            print('Integers only please!')
            continue
        if 0<b<101:
            pass
        else:
            print('Integers between 1-100 please!')
            continue
        count-=1
        if b==a:
            print(f'You win! Attempts left:{count}')
            c=input('Wanna play again?(y/n):')
            if c=='y':
                break
            elif c=='n':
                sys.exit()
            else:
                print('Incorrect input!')
                sys.exit()
        elif b>a:
            print(f'Go lower! Attempts left:{count}')
        else:
            print(f'Go higher! Attempts left:{count}')
    else:
        print('You lose! GAME OVER!')
        c=input('Wanna play again?(y/n):')
        if c=='y':
            continue
        elif c=='n':
            break
        else:
            print('Incorrect input!')
            break

