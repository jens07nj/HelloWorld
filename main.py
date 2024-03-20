import random
x = random.randint(1 , 20)

print(f'hell{'o' * x} world')
ans = input('Print again?')
while ans != '':
    x = random.randint(1, 20)
    print(f'hell{'o' * x} world')
    ans = input('Print again?')