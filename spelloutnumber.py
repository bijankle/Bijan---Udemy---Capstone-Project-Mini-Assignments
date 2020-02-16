names1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
names2 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
names3 = ['ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
names4 = ['hundred', 'thousand', 'million', 'billion', 'trillion']


def return_tens(mynum):
    myint = int(mynum[-2] + mynum[-1])
    if 0 <= myint < 10:
        return names1[myint]
    elif myint % 10 == 0:
        return names3[int(mynum[-2]) - 1]
    elif 10 < myint < 20:
        return names2[int(mynum[-1]) - 1]
    else:
        return names3[int(mynum[-2]) - 1] + ' ' + names1[int(mynum[-1])]

def return_hundreds(mynum):
    if mynum[-3] != '0':
        if return_tens(mynum) == 'zero':
            return names1[int(mynum[-3])] + ' hundred'
        else:
            return names1[int(mynum[-3])] + ' hundred and ' + return_tens(mynum)
    elif mynum[-3] == '0':
        return return_tens(mynum)

def spell_out():

    mynum = input('Input: ')

    mylist = ['']
    l = len(mynum)
    bigstring = ''

    #loop creates a 3 grouping e.g. 10,115,220 --> [10, 115, 220]
    for num in enumerate(mynum):
        i = num[0]
        d = num[1]

        if mylist[0]== '':
            mylist[0] = (d)

        elif (l - i) % 3 == 0:
            mylist.append(d)

        else:
            mylist[-1] += d

    switch = True
    for num in enumerate(mylist):

        if len(num[1]) == 2:
            mylist[num[0]] = '0' + mylist[num[0]]

        elif len(num[1]) == 1:
            mylist[num[0]] = '00' + mylist[num[0]]

        elif len(num[1]) == 3:
            mylist[num[0]] = mylist[num[0]]

        if switch == False:
            switch = True
            continue

        l2 = len(mylist)
        i = num[0]
        d = num[1]

        if switch:
            if (l2 - i) == 6:
                bigstring += return_hundreds(mylist[i]) + ' thousand, ' + return_hundreds(mylist[i + 1]) + ' billion, '
                switch = False
            elif (l2 - i) == 5:
                bigstring += return_hundreds(mylist[i]) + ' billion, '
            elif (l2 - i) == 4:
                bigstring += return_hundreds(mylist[i]) + ' thousand, ' + return_hundreds(mylist[i + 1]) + ' million, '
                switch = False
            elif (l2 - i) == 3:
                bigstring += return_hundreds(mylist[i]) + ' million, '
            elif (l2 - i) == 2:
                bigstring += return_hundreds(mylist[i]) + ' thousand, '
            elif (l2 - i) == 1:
                bigstring += return_hundreds(mylist[i])


    print(f'\n__________This is how you say {mynum} in english\n__________{bigstring}')








spell_out()








'''
def say_num():

    #e.g. 1,234,567

    bigstring = ''
    mynum = input('Input num: ')
    l = len(mynum)
    for num in enumerate(mynum):

        #e.g. index for 1 in 1,000 is 4
        i = l - num[0]

        #e.g. d is '1' for above e.g.
        d = mynum[num[1]]

        #numcat 100 = 0, 1,000 = 1, 10,000 = 1, 100,000 = 1, 1,000,000 = 2
        numcat = ((i - 1) - (i - 1) % 3) / 3

        if (i - 1) % 3 == 0:
            bigstring += names1[int(d)] + ' ' + names4[numcat]






say_num()
#print(return_tens('12369'))

'''

