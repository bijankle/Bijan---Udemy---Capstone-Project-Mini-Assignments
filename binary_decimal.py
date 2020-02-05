def power2(mynum):
    x = 0
    if mynum == 2:
        return 1
    elif mynum == 1:
        return 0
    else:
        while mynum > 2 ** (x + 1):
            x += 1
        return x


def binary(mynum):
    mynums = ['0'] * (power2(mynum) + 1)

    while mynum != 0:
        x = power2(mynum)
        mynum -= 2 ** x
        mynums[x] = '1'

    return mynums

def binary_decimal():

    mytype = input ('Do you want to convert from binary, or from a number? (bin/num): ')
    mynum = input ('Input number: ')

    result = 0

    if mytype == 'bin':

        for i in enumerate(mynum[::-1]):
            result += int(i[1]) * 2 ** int(i[0])
        print(result)

    elif mytype == 'num':

        mynum = int(mynum)

        if mynum == 0:
            result = '0'

        else:
            result = ''
            for i in binary(mynum)[::-1]:
                result += i

    return result




#print(power2(0))
print(binary_decimal())









