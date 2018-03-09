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
    print('7. tbsp to mL')
    print('7a. mL to tbsp')
    print('8. 1 fl oz or 2 tbsp to mL')
    print('8a. mL to fl oz')
    print('9. 1 cup or 8 fl oz to mL')
    print('9a. mL to cups')
    print('10. 1 pint or 2 cups or 16 fl oz to mL')
    print('11. 1 quart or 2 pints to mL')
    print('12. 1 gallon or 4 quarts or 128 fl oz to Liters')

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

def tbsp_mL():
    tbsp = float(input('Enter the number of tbsp: '))
    mL = tbsp * 14.78677

    print('tbsp in mL: {0}'.format(mL))

def mL_tbsp():
    mL = float(input('Enter the number of mL: '))
    tbsp = mL / 14.78677

    print('mL in tbsp: {0}'.format(tbsp))

def floz_mL():
    floz = float(input('Enter the number of fluid ounces: '))
    mL = floz * 29.57353

    print('fluid ounces in mL: {0}'.format(mL))

def mL_floz():
    mL = float(input('Enter the number of mL: '))
    floz = mL / 29.57353

    print('fluid ounces in mL: {0}'.format(floz))

def cup_mL():
    cup = float(input('Enter the number of cups: '))
    mL = cup * 236.58824

    print('cups in mL: {0}'.format(mL))

def mL_cup():
    mL = float(input('Enter the number of mL: '))
    cup = mL / 236.58824

    print('mL in cups: {0}'.format(cup))

def pint_mL():
    pint = float(input('Enter the number of pints: '))
    mL = pint * 473.17648

    print('pints in mL: {0}'.format(mL))

def quart_mL():
    quart = float(input('Enter the number of quarts: '))
    mL = quart * 946.35296

    print('quarts in mL: {0}'.format(mL))

def gal_Liters():
    gal = float(input('Enter the number of gallons: '))
    Liters = gal * 3.7854

    print('gallons in Liters: {0}'.format(Liters))

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

    if choice == '7':
        tbsp_mL()

    if choice == '7a':
        mL_tbsp()

    if choice == '8':
        floz_mL()

    if choice == '8a':
        mL_floz()

    if choice == '9':
        cup_mL()

    if choice == '9a':
        mL_cup()

    if choice == '10':
        pint_mL()

    if choice == '11':
        quart_mL()

    if choice == '12':
        gal_Liters()
