import random

def shifter(text, k):
    result = ""
    for char in text:
        asciicode = ord(char) #get ascii value of number
        chartemp = (asciicode + k - 65) #ascii value + shift - ascii value of A to get postion in the aphabet
        result += chr(chartemp % 26 + 65) #use modulo get remainder, then add back to A ascii value, this will "wrap around" value 
    return result

def unshifter(i):
    for i in range(0,i-1):
        print(shifter("UDWYDUUHYDW",i),", ", i, "\n")  

def RandSubMap(n = 26):
    alpha = [65] * n
    beta = [0] * n
    for i in range(0,n):
        alpha[i] = chr(alpha[i] + i)
    
    for i in range(0,n):
        temp = chr(random.randint(33,126)) #exclding syntaxing and DEL
        if temp not in beta:
            beta[i] = temp
        else:
            beta[i] = inList(temp, beta) # if rando already in arr, swap with sumn not in arr

    for i in range(0,n):
        print(alpha[i],", ",beta[i])

    hashmap = dict(zip(alpha,beta))
    return hashmap

def inList(chacha,slide):
    temp = chr(random.randint(33,126)) #exclding syntaxing and DEL
    if temp not in slide:
        if temp != chacha:
            i = slide.index(chacha)
            slide[i] = temp
        else: inList(temp,slide)

    return temp


def encodeRand(hashmap, plain):
    cypher = []
    for c in plain:
        if c in hashmap:
            cypher.append(hashmap[c])
        else:
            cypher.append(c)
    return ''.join(cypher) #make into str


def decodeMapped(hashmap, cypher):
    # invert hashmap
    invmap = {v: k for k, v in hashmap.items()}
    return encodeRand(invmap, cypher)

    

#1.
    # A
print(shifter("UNIVERSITYOFPITTSBURGH",5))
    # B
unshifter(26)

#3.
    # A
hashmap = RandSubMap()
cypher = encodeRand(hashmap, 'PITTSBURGH',)
print(cypher)
plain = decodeMapped(hashmap, cypher)
print(plain)

