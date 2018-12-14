'''a function to print the first five squares of natural numbers'''


def printlist():
    result = []
    for num in range(1, 21):
        sq = num**2
        result.append(sq)
    print(result[0:5])


def grade(marks):
    list1 = [mark for mark in marks if mark < 50]
    list2 = [mark for mark in marks if mark >= 50]
    for mark in marks:
        if mark >= 90:
            print('Excellent')
        elif mark in range(70, 90):
            print('Very Good')
        elif mark in range(60, 70):
            print('Good')
        elif mark in range(40, 60):
            print('Poor')
        elif mark in range(20, 40):
            print('Very Poor')
        else:
            print('Repeat')
    print(list1, list2)


def div_7():
    result = []
    for num in range(2000, 3201):
        if not num % 7 and num//5:
            result.append(str(num))
    print(','.join(result).encode('unicode_escape').decode())


def balance(transaction):
    bal = 0
    if not transaction:
        a = input()
        transaction = str(a)
    c = transaction.split(' ')
    if transaction.split(' ')[0] == 'D':
        bal += int(transaction.split(' ')[1])
    elif transaction.split(' ')[0] == 'W':
        bal -= int(c[1])
    else:
        bal = 'bad transaction'
    print(bal)


def capitalize(lines):
    for line in lines.split('\n'):
        print(line.upper())


def bin_div_5(*args):
    out = []
    for arg in args:
        dec = 0
        for i in range(0, 4):
            dec += int(str(arg)[i])*(2**i)
            if dec % 5 == 0:
                out.append(arg)
    print(out)
    #print(','.join(str(out)).encode('unicode_escape').decode())


def call(*args, **kwargs):
    for arg in args:
        arg()
    for key in kwargs:
        kwargs[key][0](kwargs[key][1])
