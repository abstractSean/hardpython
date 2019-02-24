import sys

def main():
    print('Enter a number.')
    number = str(input())
    try:
        numbers = [int(n) for n in number]
    except ValueError:
        print("Not a number. Enter a single number, no spaces.")
        main()
    else:
        print('Total of individual digits is: {}.'.format(sum(numbers)))

if __name__ == "__main__":
    main()




