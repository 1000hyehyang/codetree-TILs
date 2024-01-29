n, m = tuple(map(int, input().split()))

numbers = list(map(int, input().split()))
answer = []

max_num = 0

def print_xor():
    global max_num
    lst = []
    
    for elem in answer:
        lst.append(int(elem))
    
    for i in range(len(lst)):
        temp = lst[0]
        xor = temp ^ lst[i]
        temp = xor

    max_num = max(max_num, xor)
    
    return max_num



def choose(cur_num, cnt):
    if cur_num == n:
        if cnt == m:
            print_xor()
        return

    answer.append(numbers[cur_num])
    choose(cur_num + 1, cnt + 1)
    answer.pop()

    choose(cur_num + 1, cnt)


choose(0, 0)

print(max_num)