# Multiplication table printer... 3rd attempt

def multi_table(b):

    for i in range(1, b+1):
        if b % 1 == 0:
            print('{0} x {1} = {2}'.format(a, i, a*i))

if __name__ == '__main__':
    a = input('Enter a number: ')
    b = input('Enter a range: ')
    b = float(b)
