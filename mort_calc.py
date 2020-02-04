def mort_calc():

    r = float(input('input interest rate 0 < r < 1: '))
    n = int(input('input frequency 1 or 12: '))
    p = float(input('input principle amount: (p > 0): '))
    pb = float(input('input monthly payback amount: (payback > 0: '))
    t = 0

    while True:
        if n == 1:

            if 12 * pb >= p:
                t += (p/pb)/12
                print(f'Loan takes {t} years to pay off')
                break

            else:
                old = p
                p = p - 12 * pb
                i = p * r
                p = p + i
                t += 1
                if p > old:
                    print('paying back too slow!')
                    break

        elif n == 12:

            if pb >= p:
                t += (p/pb)
                print(f'Loan takes {t/12} years to pay off')
                break

            else:
                old = p
                p = p - pb
                i = p * r/12
                p = p - i
                t += 1
                if p > old:
                    print('paying back too slow!')
                    break

mort_calc()





'''
    global r
    global n

    def freq_input():
        global n
        n = 1
        while True:
            try:
                freq = input('compunded yearly or monthly? (y/m)')
            else:
                if freq == 'y':
                    n = 1
                    break
                elif freq == 'n':
                    n = 12
                    break
                else:
                    continue

    def rate_input():

        global r
        r = 20
        while True:
            try:
                r = float(input('rate? (0 < r < 1): '))
            else:
                if 0 < r < 1:
                    break

                else:
                    continue
'''
