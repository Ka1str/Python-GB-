import itertools

# А)
num_list = []
for el in itertools.count(3):
    if el > 10:
        break
    print(el)

# B)
my_list = ['яблоко', 'груша', 'апельсин']
c = 0

for el in itertools.cycle(my_list):
    if c == len(my_list) * 3:
        break
    print(el)
    c += 1
