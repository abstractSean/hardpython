from math import factorial

def main():
    print('Enter number:')
    
    try:
        number = int(input())
    except ValueError:
        print('Enter a valid number, no spaces.')
        main()
    else:
        result = factorial(number)
        print('{}! = {}'.format(number, result))

if __name__ == '__main__':
    main()
