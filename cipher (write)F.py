y =raw_input("what do you want to write?  ")
i = 0
xx = []

while i<len(y):
    bi = y[i]
    cbi = ord(bi) + i -1
    if cbi > 126:
        u = cbi - 94
    elif cbi < 32:
        u = cbi + 94
    else:
        u = cbi
    new = chr(u)
    xx.append(new)
    i += 1

a = ''.join(xx)
print a

e = raw_input("did you finish? ")

