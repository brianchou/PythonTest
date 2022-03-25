'''
print('Hello World!!!')

print('*' * 20)

word = "1abccba1"

print(word)

n = len(word)

print('Word Length : ' + str(n))

i = 0
x = 0
while i < ((n/2)+1):
    if word[i] == word[n-1]:
        pass
    else:
        x += 1
    i = i + 1
    n = n-1

if x != 0:
    print("非對稱字串")
else:
    print("對稱字串")
'''

num1 = 100
num2 = 90
average = (num1+num2) / 2.0
print(average)