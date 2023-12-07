def selectionSort(lst):
    n = len(lst)
    for i in range(n - 1):
        least = i
        for j in range(i, n):
            if lst[j] < lst[least]:
                least = j
        lst[i], lst[least] = lst[least], lst[i]
    
    for i in range(n):
        print(lst[i], end = ' ')

n = int(input())
lst = list(map(int, input().split()))

selectionSort(lst)