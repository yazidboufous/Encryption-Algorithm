def keystream():
    # We generate the State array:
    S = [i for i in range(256)]

    # we generate the temporary vector by stretching the short key:
    import random
    K=[]  #(Short key)
    for i in range(5):
        a=random.randint(0,10)
        K.append(a)   # (Short key)

    T = []
    for i in range(256):
        for j in K:
            T.append(j)

    # Key-Scheduling Algorithm:
    # We swap the order of bytes inside of the S array using the temporary vector T:
    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo random generation algorithm:
    # We generate the keystream that we will use to encrypt (it has the same lenght of the plain text).
    global text
    text=input('Enter your text:')
    length = []
    for i in text:
            length.append(i)

    j = 0
    i=0
    key=[]
    while i<len(length):
        i=(i+1)%256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        key.append(S[t])

    #convert the keystream into binary:
    global binary_keystream
    binary_keystream=[]
    for i in key:
        binary_keystream.append(bin(i))
#perform the xor operation between each charceter in the text and the keystream it is assigned to it :

def xor():
#convert plain text into binary:
    binary_text=[]
    for i in text:
            binary_text.append(bin(ord(i)))

    global xor1
    xor1=[]
    for i,j in zip(binary_text,binary_keystream):
            x=eval(i)^eval(j)
            xor1.append(x)

    #now convert the binary to characters:
    global encrypted
    encrypted=''
    for i in xor1 :
        encrypted+=chr(i)
    print(encrypted)

def encrypt():
    keystream()
    print('The encrypted text is:')
    xor()


encrypt()

##########################################################################################################

for i in range(3):
    print('')

def decrypt():
    xor2=[]
    for i,j in zip(xor1,binary_keystream):
        a=eval(bin(i))^eval(j)
        xor2.append(a)

    decrypted=''
    for i in xor2:
        decrypted+=chr(i)
    print('The decrypted text is:')
    print(decrypted)

decrypt()