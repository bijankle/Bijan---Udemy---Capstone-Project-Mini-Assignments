from threading import Timer
import datetime

#user input timer/alarm
def alarm_timer():

    #alarm feature
    def alarm():

        #user input loop - hrs, mins
        while True:

            try:
                input_hour = int(input('Input alarm time - Hours (24 hr format): '))

            except:
                print('Input error! Try again!')
                continue

            else:
                if 0 <= input_hour <= 24:
                    break

                else:
                    print('input hrs must be between 0 and 24')
                    continue

        if input_hour == 24:
            input_min = 0

        else:

            while True:

                try:
                    input_min = int(input('Input alarm time - Mins: '))

                except:
                    print('Input error! Try again!')
                    continue

                else:

                    if 0 <= input_min < 60:
                        break
                    else:
                        print('input min must be between 0 and 60')
                        continue

        #form is tuple (24hr hrs, mins, sec, fractions of sec)
        current_time = datetime.time.now()

        #calculate time difference
        if current_time[0] > input_hour:
            time_dif = (24 - current_time[0] + input_hour)*60*60 + (60 - current_time[1] + input_min)*60 - current_time[2]

            #create and start timer
            t = Timer(time_dif, print('Alarm Set!'))
            t.start()
            t.join()

            #print upon timer end
            print('TIME!')


    def timer():

        #user input loop - hrs, mins, secs
        while True:
            try:
                hrs = int(input('Input no. hrs: '))

            except:
                print('Input error! Try again!')
                continue

            else:

                if 0 <= hrs:
                    break
                else:
                    print('input min must be positive int')
                    continue

        while True:
            try:
                mins = int(input('Input no. mins: '))

            except:
                print('Input error! Try again!')
                continue

            else:

                if 0 <= mins < 60:
                    break
                else:
                    print('input min must between 0 and 60')
                    continue

        while True:
            try:
                secs = int(input('Input no. secs: '))

            except:
                print('Input error! Try again!')
                continue

            else:

                if 0 <= secs < 60:
                    break
                else:
                    print('input secs must between 0 and 60')
                    continue

        #set and start timer
        t = Timer(hrs * 60 * 60 + mins * 60 + secs, print('Timer Set!'))
        t.start()
        t.join()

        #print when timer stops
        print('TIME!')

    #user input loop - timer or alarm feature choice
    while True:

        input1 = input('\nSelect timer or alarm (t/a): ').lower()

        if input1 == 't':

            timer()
            break

        elif input1 == 'a':

            alarm()
            break

        else:
            print('Input must be a string starting with t or a!')
            continue

#run my function
alarm_timer()

