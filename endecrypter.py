def encrypt(txt, key):
    ip = key
    pss = ""
    for i in ip:
        if i in "1234567890":
            pss = pss + str(ord(i)-48)
        else:
            pss = pss + str(ord(i))
    password = pss
    enc = ''
    k = 0
    d = 0
    for i in range(len(txt)):
        if i <= (len(password)-1):
            k = int(password[i])
            d = ord(txt[i])+k
            if d > 126:
                d = (d % 126)+32
                enc = enc + chr(d)
            else:
                enc = enc + chr(d)
        if i > (len(password)-1):
            k = int(password[((i+1) % len(password))-1])
            d = ord(txt[i])+k
            if d > 126:
                d = (d % 126)+32
                enc = enc + chr(d)
            else:
                enc = enc + chr(d)
    return (enc)

def decrypt(enc, key):
    ip = key
    pss = ""
    for i in ip:
        if i in "1234567890":
            pss = pss + str(ord(i)-48)
        else:
            pss = pss + str(ord(i))
    password = pss

    deenc = ""
    k = 0
    d = 0
    for i in range(len(enc)):
        if i <= (len(password)-1):
            k = int(password[i])
            d = ord(enc[i])-k
            if d < 32:
                z = d % 126
                d = (126 + z)-32
                deenc = deenc + chr(d)
            else:
                deenc = deenc + chr(d)
        if i > (len(password)-1):
            k = int(password[((i+1) % len(password))-1])
            d = ord(enc[i])-k
            if d < 32:
                z = d % 126
                d = (126 + z)-32
                deenc = deenc + chr(d)
            else:
                deenc = deenc + chr(d)
    return(deenc)

# p = "abc123"
# t = "hello darkness my old friend"
# x = encrypt(t, p)
# print(x)
# y = decrypt(x , p)
# print(y)