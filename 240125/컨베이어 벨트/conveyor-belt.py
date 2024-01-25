n, t = map(int,input().split())

belt = []

for _ in range(2):
    belt += list(map(int,input().split()))

for i in range(t):
    temp = belt[-1]
    belt[1:2*n] = belt[0:2*n-1]
    belt[0] = temp

for index, i in enumerate(belt):
    if index == n:
        print()
    print(i,end=' ')