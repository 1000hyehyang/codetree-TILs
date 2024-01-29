k, n = tuple(map(int, input().split()))

answer = []

def print_answer():
    for elem in answer:
        print(elem, end = ' ')
    print()

def choose(cnt):
    if cnt == n:
        print_answer()
        return
    
    for num in range(1, k + 1):
        if cnt >= 2 and answer[-1] == num and answer[-2] == num:
            continue
        
        answer.append(num)
        choose(cnt + 1)
        answer.pop()

    return

choose(0)