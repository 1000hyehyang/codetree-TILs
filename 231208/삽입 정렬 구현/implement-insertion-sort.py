def insertSort(lst):
    n = len(lst)
    for i in range(1, n):
        j = i - 1
        key = lst[i]
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    
    for i in range(n):
        print(lst[i], end = ' ')

n = int(input())
lst = list(map(int, input().split()))

insertSort(lst)