# Doing Math with Python Quizes

## Programming Challenges pg 22 - 26
## #1: Even-Odd Vending Machine
'''
def coinMachine(coin):

    if coin % 2 == 0:
        print('Your number is even')
        for i in range(coin, coin+19, 2):
            print(i)
    else:
        print('Your number is odd')
        for i in range(coin, coin+19, 2):
            print(i)


if __name__ == '__main__':
    coin = input('Your Number Please: ')
    coin = float(coin)

    if coin > 0 and coin.is_integer():
        coinMachine(int(coin))
    else:
        print('Please enter a positive integer, a number with nothing beyond the decimal point')
'''

## #2: Enhanced Multiplication Table Generator

'''
def multi_table(a):
    for a in range(a, a+n):
        print('{0} x {1} = {2} '.format(a, b, a * b))

if __name__ == '__main__':
    a = input('Enter a number: ')
    b = input('Enter a multiple: ')
    n = input('Enter the range or how many iterations you would like to see: ')
    multi_table(a)
'''
## #3 Enhanced Unit Converter
## Unit Converter: Miles <=> Kilometers, Kilograms <=> Pounds and Celsius <=> Farenheit.

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Kilograms to Pounds')
    print('4. Pounds to Kilograms')
    print('5. Celsius to Farenheit')
    print('6. Farenheit to Celsius')

def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609

    print('Distance in miles: {0}'.format(miles))

def mile_km():
    miles = float(input('Enter distance in kilometers: '))
    miles = km * 1.609

    print('Distance in Kilometers: {0}'.format(km))

def kilo_lbs():
    kilo = float(input('Enter mass in Kilograms: '))
    kilo = lbs / 2.2046226218

    print('Mass in Pounds: {0}'.format(kilo))

def lbs_kilo():
    lbs = float(input('Enter mass in pounds: '))
    lbs = kilo * 2.2046226218

    print('Mass in Kilograms: {0}'.format(lbs))

def celsius_farenheit():
    celsius = float(input('Enter temperature in Celsius: '))
    celsius = (farenheit - 32) * (5 / 9)

    print('Temperature in Celsius: {0}'.format(celsius))

def farenheit_celsius():
    farenheit = float(input('Enter temperature in Farenheit: '))
    farenheit = celsius * (9 / 5) + 32

    print('Temperature in Farenheit: {0}'.format(farenheit))

if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do?: ')
    if choice == '1':
        km_miles()

    if choice == '2':
        mile_km()

    if choice == '3':
        kilo_lbs()

    if choice == '4':
        lbs_kilo()

    if choice == '5':
        celsius_farenheit()

    if choice == '6':
        farenheit_celsius()
