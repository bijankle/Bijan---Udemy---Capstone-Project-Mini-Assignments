def factorialfinder():

    while True:

        mynum = int(input('Input num, ill output its factorial: '))

        if mynum == 0 or mynum == 1:
            print(1)

        else:

            for i in range(mynum, 1, -1):
                mynum *= (i-1)


            print(mynum)


factorialfinder()
