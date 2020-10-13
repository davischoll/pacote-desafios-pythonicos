nome = 'henrique'

print(nome, len(nome))

"""
i = 0

while i < len(nome):
    print(nome[i])
    i += 1

-------

for i in range(len(nome)):
    print(nome[i])

-------

for i, c in enumerate(nome):
    if c == 'e':
        continue
    print(i, c)
"""

s = 'babble'
first = s[0]

for i, c in enumerate(s):
    #    print(''.join('*' if c == first and i != 0 else c))
    if c == first and i != 0:
        print(''.join(['*']))
    else:
        print(''.join([c]))
