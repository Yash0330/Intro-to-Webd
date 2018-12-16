from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space , quantity = input().rpartition(' ')
    if item not in d:
        d[item] = int(quantity)
    else:
        d[item] += int(quantity)
for i, q in d.items():
    print(i, q)




