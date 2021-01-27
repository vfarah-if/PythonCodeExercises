from arithmatic.another_sum import another_sum
from requests import get

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

response = get('https://httpbin.org/ip')
print('Your IP is {0}'.format(response.json()['origin']))
