# enumerate
for i,char in enumerate('Helllooo'):
    print(i, char)

for i,char in enumerate((1,2,3)):
    print(i, char)

# Exercise is to print the index of 50

for i,char in enumerate(list(range(100))):
    if char == 50:
         print(f'index of 50 is: {i}')
