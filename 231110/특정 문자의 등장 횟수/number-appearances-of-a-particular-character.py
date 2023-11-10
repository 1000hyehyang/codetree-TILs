n = input()
ee = 0
eb = 0

for i in range(len(n)):
    if i < len(n) - 1 and n[i] == 'e':
        if n[i + 1] == 'e':
            ee += 1
        elif n[i + 1] == 'b':
            eb += 1

print(ee, eb)