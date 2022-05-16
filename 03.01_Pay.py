# Have user enter values for Hours and Rate and respond with Pay
# Hours over 40 are paid 1.5x Rate

h = input('Enter hours: ')
r = input('Enter rate:  ')

# Convert all input to float
h = float(h)
r = float(r)

# Safeguard from negative input
if h < 0 or r < 0:
    # print('Invalid entry. Please try again.')
    p = 0.0

elif h > 40 :
    p = (h - 40) * 1.5 * r
    # print('(Overtime pay of', p, 'included)')
    p = p + 40 * r
else :
    p = h * r

print('Pay:', p)
