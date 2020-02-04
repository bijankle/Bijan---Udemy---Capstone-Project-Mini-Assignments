#While loops (no recursion)
'''
def find_happy_number(mynum):

    count = 0
    result = mynum

    while count != 50 and result != 1:

        temp = result
        for i in str(result):

            result +=  (int(i))**2

        result -= temp

        if result == 1:
            return mynum
        elif count == 50:
            return null
        else:
            count += 1

def happy_numbers(mynum):

    hap_num = []

    while len(hap_num) < 8:
        hap_num.append(find_happy_number(mynum))

        if hap_num[len(hap_num) - 1] == None:
            hap_num.pop()
        mynum += 1
    print(hap_num)


happy_numbers(2)
'''

#recursion attempt 1

def hap_num(mynum):
    temp = mynum
    for i in str(mynum):
        mynum += int(i)**2
    mynum -= temp






