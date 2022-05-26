# In 'X-DSPAM-Conference: 0.8475 ' extract value after ':'
# and convert it into a floating-point number

str = 'X-DSPAM-Conference: 0.8475 '
value = str[str.find(' ') : ]
value.strip()
value = float(value)
print(value)
