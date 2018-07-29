Input = raw_input("what do you want to translate?  ")
i = 0
xx = []

while i<len(Input):
    bi = Input[i]
    cbi = ord(bi)- i +1
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