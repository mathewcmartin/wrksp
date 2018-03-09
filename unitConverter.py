# Doing Math with Python Quizes

# Programming Challenges pg 22 - 26

# #3 Enhanced Unit Converter
# Unit Converter: Miles <=> Kilometers, Kilograms <=> Pounds and Celsius <=> Farenheit.

# Unit Converter: Miles <=> Kilometers, Kilograms <=> Pounds and Celsius <=> Farenheit.

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

def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609

    print('Distance in kilometers: {0}'.format(km))

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
    farenheit = celsius * (9 / 5) + 32

    print('Temperature in Farenheit: {0}'.format(farenheit))

def farenheit_celsius():
    farenheit = float(input('Enter temperature in Farenheit: '))
    celsius = (farenheit - 32) * (5 / 9)

    print('Temperature in Celsius: {0}'.format(celsius))

if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do?: ')
    if choice == '1':
        km_miles()

    if choice == '2':
        miles_km()

    if choice == '3':
        kilo_lbs()

    if choice == '4':
        lbs_kilo()

    if choice == '5':
        celsius_farenheit()

    if choice == '6':
        farenheit_celsius()
