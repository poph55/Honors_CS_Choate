#name = str(input("What is your name?"))
#print('hello, ' + name + '!')
import sys

# the end function declares what follows the printed statement. 
# This is important because if it was left out the next name we tried to print
# would by default go to the next line.
print('Hello, ', end='')
print(sys.argv[1], end=', ')
print(sys.argv[2], end=', and ')
print(sys.argv[3], end='')
print('! Welcome.')


# to run the code type: python3 hello.py Meghan Ned Francie 
