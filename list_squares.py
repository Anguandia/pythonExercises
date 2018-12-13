'''a function to print the first five squares of natural numbers'''
def printList():
    result = []
    for num in range(1, 21):
        sq = num**2
        result.append(sq)
    print(result[0:5])


def grade(marks):
    pass


def div_7():
    result = []
    for num in range(2000, 3201):
        if not num %7 and num//5:
            result.append(str(num))
        #return result
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
