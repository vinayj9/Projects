import sys
while True:
    print('Welcome User!')
    try:
        a=float(input('Enter first number:'))
        b=float(input('Enter second number:'))
    except ValueError:
        print('Please enter valid number!')
        sys.exit()
    except:
        print('Something else went wrong')
    c=input('Enter your choice of operation(+-*/):')
    if c=='+':
        d=a+b
        print(d)
    elif c=='-':
        d=a-b
        print(d)
    elif c=='*':
        d=a*b
        print(d)
    elif c=='/':
        try:
            d=a/b
            print(d)
        except ZeroDivisionError:
            print('denominator cant be zero')
    else:
        print('Invalid operation')
    e=input('Wanna do another one(y/n):')
    if e=='y':
        continue
    if e=='n':
        sys.exit()
    else:
        print('Invalid response')
        break