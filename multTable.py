# Doing Math with Python Quizes

# Programming Challenges pg 22 - 26

# #2: Enhanced Multiplication Table Generator

def multi_table(a):

    for i in range(1, 11):
        print('{0} x {1} = {2}'.format(a, i, a*i))

def count(b):
    b = count + 1
    while count >= 0:
        print(count)

if __name__ == '__main__':
    while True:
        a = input('Enter a number: ')
#        n = input('Enter a multiple: ')
        b = input('Enter the range or how many iterations you would like to see: ')
        multi_table(a)
        count(b)

        answer = input('Do you want to exit? (y) for yes ')
        if answer == 'y':
            break

'''

def multi_table(a):

        for i in range(1, 11):
            print('{0} x {1} = {2} '.format(a, i, a*i))

if __name__ == '__main__':
    a = input('Enter a number: ')
#    count = input('Enter the range or how many iterations you would like to see: ')
    multi_table(a)
'''
