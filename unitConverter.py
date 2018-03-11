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
    print('8. mL to tbsp')
    print('9. 1 fl oz or 2 tbsp per mL')
    print('10. mL to fl oz')
    print('11. 1 cup or 8 fl oz per mL')
    print('12. mL to cups')
    print('13. 1 pint or 2 cups or 16 fl oz per mL')
    print('14. mL to pints')
    print('15. 1 quart or 2 pints per mL')
    print('16. mL to quarts')
    print('17. 1 gallon or 4 quarts or 128 fl oz per Liter')
    print('18. Liters to gallons')

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

def mL_pint():
    mL = float(input('Enter the number of pints: '))
    pint = mL / 473.17648

    print('mL in pints: {0}'.format(pint))

def quart_mL():
    quart = float(input('Enter the number of quarts: '))
    mL = quart * 946.35296

    print('quarts in mL: {0}'.format(mL))

def mL_quart():
    mL = float(input('Enter the number of mL: '))
    quart = mL / 946.35296

    print('mL in quarts: {0}'.format(quart))

def gal_Liters():
    gal = float(input('Enter the number of gallons: '))
    Liters = gal * 3.7854

    print('gallons in Liters: {0}'.format(Liters))

def Liters_gal():
    Liters = float(input('Enter the number of Liters: '))
    gal = Liters / 3.7854

    print('Liters in gallons: {0}'.format(gal))

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

    if choice == '8':
        mL_tbsp()

    if choice == '9':
        floz_mL()

    if choice == '10':
        mL_floz()

    if choice == '11':
        cup_mL()

    if choice == '12':
        mL_cup()

    if choice == '13':
        pint_mL()

    if choice == '14':
        mL_pint()

    if choice == '15':
        quart_mL()

    if choice == '16':
        mL_quart()

    if choice == '17':
        gal_Liters()

    if choice == '18':
        Liters_gal()
