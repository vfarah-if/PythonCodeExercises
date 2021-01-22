from sum.another_sum import another_sum

def getNumbers():
    first_number = int(input('What is the first number? '))
    second_number = int(input('What is the second number? '))
    print(another_sum(first_number, second_number))

def getConfirmation():
    global confirmation
    confirmation = input('Would you like to do some sums? (Y or n) ')

confirmation = 'Y'
while confirmation.strip().upper() == 'Y':
    getNumbers()
    getConfirmation()


