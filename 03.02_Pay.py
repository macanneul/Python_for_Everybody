# Same as 03.01_Pay.py but exit program if user enters anything other than numbers

try :                   # Try to convert h to float
    h = float(input('Enter hours: '))
except :
    print('Error, please enter numeric input')
    quit()

try :                   # Try to convert r to float
    r = float(input('Enter rate:  '))
except :
    print('Error, please enter numeric input')
    quit()

if h < 0 or r < 0:      # Safeguard from negative input
    # print('Invalid entry')
    p = 0.0
elif h > 40 :
    p = (h - 40) * 1.5 * r
    # print('(Overtime pay of', p, 'included)')
    p = p + 40 * r
else :
    p = h * r

print('Pay:', p)
