numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primers = [2, 3, 5, 7, 11, 13]
not_primers = [4, 6, 8, 9, 10, 12, 14, 15]
print(primers)
print(not_primers)

for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for k in range(2, i):
        if i % k == 0:
            is_prime = False
            break
    if is_prime == True:
        primers.append(i)
    else:
        not_primers.append(i)

print(primers)
print(not_primers)

