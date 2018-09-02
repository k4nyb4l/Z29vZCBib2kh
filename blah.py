import twitter
from itertools import cycle

def bal(key):
    keylength = len(key)

    S = range(256)

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]

    return S

def ka(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]

        K = S[(S[i] + S[j]) % 256]
        yield K

def ny(key):
    S = bal(key)
    return ka(S)

api = twitter.Api(consumer_key='************',
                consumer_secret='***********',
                access_token_key='**********',
                access_token_secret='*********')

key = bytearray("***************")

l = bal(key)
text = 'TEST'
blah = ''.join(chr(ord(c)^d) for c,d in zip(text,cycle(l)))
print(blah)
status = api.PostUpdate(blah)
print(status.text)
