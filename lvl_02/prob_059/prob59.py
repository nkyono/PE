'''
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). 
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, 
then XOR each byte with a given value, taken from a secret key. 
The advantage with the XOR function is that using the same encryption key on the cipher text, 
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. 
The user would keep the encrypted message and the encryption key in different locations, and without both "halves", 
it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. 
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. 
The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters.
Using p059_cipher.txt, a file containing the encrypted ASCII codes, 
and the knowledge that the plain text must contain common English words, 
decrypt the message and find the sum of the ASCII values in the original text.
'''
# two ways to do this, we can brute force it (never a good idea for cryptography) or do something more clever
# I think this is a good place to try and use letter frequency

'''
a	0.08167	n	0.06749
b	0.01492	o	0.07507
c	0.02782	p	0.01929
d	0.04253	q	0.00095
e	0.12702	r	0.05987
f	0.02228	s	0.06327
g	0.02015	t	0.09056
h	0.06094	u	0.02758
i	0.06966	v	0.00978
j	0.00153	w	0.02360
k	0.00772	x	0.00150
l	0.04025	y	0.01974
m	0.02406	z	0.00074
'''

def getMax(freq):
    maxFreq = -1
    for x in freq:
        if freq[x] > maxFreq:
            maxFreq = x
    return maxFreq

def getFreq(arr):
    total = len(arr)
    num = {}
    for x in arr:
        if x in num:
            num[x] = num[x] + 1
        else:
            num[x] = 1
    freq = {}
    for x in num:
        freq[x] = num[x] / total

    for x in freq:
        print(x, freq[x])
    print('-----------------')
    return freq

def test():
    assert 65 ^ 42 == 107
    assert 65 ^ 65 == 0
    assert 107 ^ 42 == 65
    f = open("lvl_02/prob_059/p059_cipher.txt",'r')
    line = f.readline()
    line = line.split(',')

    key_index = [[],[],[]]
    for x in range(len(line)):
        line[x] = int(line[x])
        key_index[x%3].append(line[x])

    key = []
    for x in key_index:
        # print(x)
        freq = getFreq(x)
        maxFreq = getMax(freq)

    # kinda just looked at frequencies produced and guessed a key 
    # e == 101, 101 ^ 101 == 0
    # x == 120, 101 ^ 29 == 120 (this was 2nd guess, first was 101 ^ 88 which wouldn't for, but ' '== 32 and 32 ^ 88 == 120)
    # p == 112, 32 ^ 80 == 112 (tried, e, a, ' ' for most frequent character, 'p' was first char that fit key criteria)
    key = [ord('e'), ord('x'), ord('p')]
    plain = []
    for x in range(len(line)):
        plain.append(line[x] ^ key[x%3])
    print(''.join(map(chr,plain)))
    sum = 0
    for x in plain:
        sum = sum + x
    print(sum)


if __name__ == '__main__':
    import time
    start = time.time()
    test()
    print("time:", time.time()-start)