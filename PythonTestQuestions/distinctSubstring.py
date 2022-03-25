## print('Hello World!')

'''
freq = [False] * 26

print(freq)
'''

'''
S = dict()

print (S)

s = 'a'

S[s] = 1

print (S)
'''

def distinctSubstring(s):
    D = dict()
    
    for i in range(len(s)):
        freq = [False] * 26

        S = ""

        #print(len(s))

        #print('####')

        #print(i)

        #print ('===')

        for j in range(i, len(s)):

            #print (j)

            #print ('***')
            
            pos = ord(s[j]) - ord('a')
            
            if  (freq[pos] == True):
                break

            freq[pos] = True

            S += s[j]

            D[S] = 1
    
    print(D)

    return len(D)

f = 'abc'

number = distinctSubstring(f)

'''
S = dict()
s = 'number'

S[s] = number

print(S)
'''

