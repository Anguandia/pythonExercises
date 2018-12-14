'''a function to print the first five squares of natural numbers'''


def printlist():
    result = []
    for num in range(1, 21):
        sq = num**2
        result.append(sq)
    print(result[0:5])


def grade(marks):
    if not marks:
        marks = input()
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


def balance(*args):
    bal = 0
    for arg in args:
        if arg.split(' ')[0] == 'D':
            bal += int(arg.split(' ')[1])
        elif arg.split(' ')[0] == 'W':
            bal -= int(arg.split(' ')[1])
        else:
            bal = 'bad arg'
    print(bal)


def capitalize(lines):
    a = input()
    lines = str(a)
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
        print(arg)

call(*(bin_div_5(1001, 1100, 1010, 1111, 1011, 1101, 1000), balance('D 400', 'W 700'), grade([99, 70, 25, 66, 59]), capitalize('')))
