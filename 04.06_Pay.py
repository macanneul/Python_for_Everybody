# Rewrite 03.01_Pay.py by creating a function called computepay which takes
# two parameters: hours, rate

def computepay(hours, rate) :
    if hours > 40 :
        pay = (hours -40) * 1.5 * rate
        # print('(Overtime pay of', p, 'included)')
        p = pay + 40 * rate
    else :
        p = hours * rate
    print('Pay:', p)

def paycal() :
    h = float(input('Enter Hours: '))
    r = float(input('Enter Rate:  '))
    # Safeguard from negative input
    if h < 0.0 or r < 0.0 :
        print('Invalid entry. Please try again.')
        paycal()
    else :
        computepay(h, r)
        
paycal()
