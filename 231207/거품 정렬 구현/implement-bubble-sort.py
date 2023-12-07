def bubbleSort(lst):
    n = len(lst)

    for i in range(n):
        bubble = False
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                bubble = True
        if not bubble:
            break

    for i in range(n):
        print(lst[i], end = ' ')

n = int(input())
lst = list(map(int, input().split()))

bubbleSort(lst)