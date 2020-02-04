def complex_numbers():

    #input control loop - num1 = a + bi
    while True:

        try:
            a = int(input('input num1 Re: '))
            b = int(input('input num1 Im: '))
            break

        except:
            print('error: input an int ... ')

        else:
            continue

    print(f'\nnum1 = {a} + {b}i\n')

    operating = True
    while operating:

        #input control loop - operation
        while True:
            try:
                operation = input('input operation: ')
            except:
                pass

            else:
                if operation != '+' and operation != '-' and operation != '*' and operation != '/':
                    print('error: please input +, -, * or / ... ')
                    continue
                else:
                    break

        #input control loop - num2 = c + di
        while True:

            try:
                c = int(input('input num2 Re: '))
                d = int(input('input num2 Im: '))
                break

            except:
                print('error: input an int ... ')

            else:
                continue

        print(f'\nnum2 = {c} + {d}i\n')

        #(a + bi)(c + di) = ac + (bc + ad)i -bd
        if operation == '*':
            re_result = a * c - b * d
            im_result = b * c + a * d

        elif operation == '+':
            re_result = a + c
            im_result = b + d

        elif operation == '-':
            re_result = a - c
            im_result = b - d

        #(a + bi)/(c + di) * (c - di)/(c - di) = (ac - (ad-bc)i + bd) / (c^2 + d^2)
        elif operation == '/':
            re_result = (a * c + b * d)/(c**2 + d**2)
            im_result = (b * c - a * d)/(c**2 + d**2)

        a = re_result
        b = im_result

        if a == 0:
            print(f'\ncurrent result = {b}i\n')

        elif b == 0:
            print(f'\ncurrent result = {a}\n')

        else:
            print(f'\ncurrent result = {a} + {b}i\n')

        #input control loop - 'operating'
        while True:

            try:
                operating = input('do you want to add more operations? (y/n): ').lower()

            except:
                print('error: input y/n ... ')

            else:
                if operating == 'y':
                    operating = True
                    break

                elif operating == 'n':
                    operating = False
                    break

                else:
                    continue

        if a == 0:
            print(f'\nfinal result = {b}i\n')

        elif b == 0:
            print(f'\nfinal result = {a}\n')

        else:
            print(f'\nfinal result = {a} + {b}i\n')



complex_numbers()








