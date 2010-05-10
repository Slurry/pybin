#!/usr/bin/env python3.1

def getint(n, m):
    try:
        i = int(n)
        b = int(m)
    except ValueError:
        print('bad values')
    else:
        if (i >= 1) == (i <= b):
            return i
        else:
            print('number is out of range. ' + str(b) + ' is max')

def analizerandomness(duration, depth, selection):
    # analysis of selection randomness
    randomnessEval = 0
    values = range(1,depth + 1)
    for n in values:
        occurance = selection.count(n)
        randomnessEval += abs(occurance - duration)
    return int(randomnessEval)



print('*******************************************************************')
print('Enter a few random numbers, and I will analize your intuitive prowis.')
print('*******************************************************************')
duration, depth = '', ''

while not depth:
    depth = getint(input('What is the max number to use for your guess. 3 is a good place to start :'),10)

while not duration:
    duration = getint(input('How many guesses would you like to evaluate (in multiples of ' + str(depth) +  ' ). 2 is a good place to start :'),10)
    
print('Here are your instructions.\nFor the next ' + str(duration * depth) + \
' promps, enter a random number from 0 to ' + str(depth) + '.')
count = 1
exitflag = False
selection = []
while exitflag == False:
    n = input('Enter number ' + str(count) + ' :')
    if n == '':
        exitflag = True
    else:
        number = getint(n, depth)
        if number:
            selection.append(number)
            count += 1
            if count > duration * depth:
                exitflag = True

randomness = analizerandomness(duration, depth, selection)
worst = str(duration * depth + duration)
print('Your Randomness score is ' + str(randomness) + '\non a scale of 0 - '+ worst  +'. 0 being the best.')

