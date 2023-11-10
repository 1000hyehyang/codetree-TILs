n = int(input())
arr = []

for i in range(n):
    op = input().split()
    if op[0] == 'push_back':
        op[1] = int(op[1])
        arr.append(op[1])
    elif op[0] == 'pop_back':
        del arr[-1]
    elif op[0] == 'size':
        print(len(arr))
    elif op[0] == 'get':
        op[1] = int(op[1])
        print(arr[op[1] - 1])