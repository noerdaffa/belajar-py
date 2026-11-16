# Print Number until the user enters 0
number = int(input('Enter a number: '))

#iterate until the user enters 0
while number != 0:
    print('You entered ', number)
    number = int(input('Enter a number: '))

print('The end.')
