# Doing Math with Python Quizes

## Programming Challenges pg 22 - 26
## #1: Even-Odd Vending Machine

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
