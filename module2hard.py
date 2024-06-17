import random
n = random.randint(3,20)
result = ''
list_pairs = []
for i in range(1,n):
    for j in range(1, n):
        if i == j:
            continue
        if n % (i + j) == 0:
            if [j,i] not in list_pairs:
                list_pairs.append([i,j])
                result += str(i) + str(j)
print(n)
print(result)
