#!/usr/bin/python3

def main():
    """ Main entry point of the app """
    print("STRING:")
    message = "This is string"  #string
    print(message)
    message = "Hello " + "I am python"
    print(message)
    message = "M E S S A G E "
    print(message.strip())
    print(type(message))
    print('\n')

    print('NUMBERS:')
    num = 2     #number
    print(num)

    num = (2+4) * 3
    print(num)
    print(type(num))
    print('\n')

    print('FLOATS:')
    num = 2.19
    print(num)

    num = (2.19+2.34) + 3.24
    print(num)
    print(type(num))

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
