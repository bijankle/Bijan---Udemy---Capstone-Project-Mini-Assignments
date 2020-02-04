#see solution for more rules: https://bitbucket.org/desertwebdesigns/learn_python/src/master/Numbers/credit_card.py
'''
if (int(cc[:2]) >= 51 and int(cc[:2]) <= 55 and len(cc) == 16) or \
    (int(cc[0]) == 4 and (len(cc) == 13 or len(cc) == 16)) or \
    ((int(cc[:2]) == 34 or int(cc[:2]) == 37) and len(cc) == 15) or \
    (int(cc[:4]) == 6011 and len(cc) == 16):
  if val_cc(cc) % 10 == 0:
      print "%s is a valid credit card number" % cc
  else:
      print "%s is NOT a valid credit card number" % cc
else:
    print "%s is NOT a valid credit card number" % cc
'''


def credit_card_validator():

    #my_card_num = ''.join(input('please input your card number: ').split('-'))
    my_card_num = '4519-9121-5601-6182'.split('-')
    my_card_num = ''.join(my_card_num)
    print(my_card_num)
    card_sum = 0

    for i in range(0, len(my_card_num) - 1, 2):
        j = int(my_card_num[i])
        j *= 2
        if j > 9:
            card_sum += int(str(j)[0]) + int(str(j)[1])

        else:
            card_sum += j

    for i in range(1, len(my_card_num), 2):
        card_sum += int(my_card_num[i])

    if card_sum == 70:
        print('Your card is from ')

    else:
        print(card_sum)
        return False




print(credit_card_validator())
