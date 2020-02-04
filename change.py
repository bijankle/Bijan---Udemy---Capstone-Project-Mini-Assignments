def change():

    #format round() to suit monitary system
    myround = lambda x : round(2 * x, 1)/2

    #inputs
    cost = float(input('Cost: '))
    amount_given = myround(float(input('Amount Given: ')))

    #create skeleton dictionary to store our change
    change_list = {2:0, 1:0, 0.5:0, 0.2:0, 0.1:0, 0.05:0}

    c = myround(amount_given - cost)

    for i in change_list:
        if c < i:
            change_list[i] = 0
        else:
            temp = c
            c = myround(c % i)
            change_list[i] = ((temp - c) / i)

    #correct syntax from e.g. 0.5 to 50c
    for i in [2, 1, 0.5, 0.2, 0.05]:
        if i >= 1:
            new_string = '$' + str(i)
            change_list[new_string] = change_list[i]
            del change_list[i]
        else:
            new_string = str(round(i * 100)) + 'c'
            change_list[new_string] = change_list[i]
            del change_list[i]

    #print header
    print('\n----- TRANS -----')
    print(f'Cost: \t\t{cost}')
    print(f'Amount Given:\t{amount_given}\n')
    print('----- CHANGE -----')

    print('coin: \t\tcount:')

    #print key and value neatly
    for item in change_list:
        if change_list[item] == 0:
            pass
        else:
            print(f'{item}\t\tx {int(change_list[item])}')

change()
