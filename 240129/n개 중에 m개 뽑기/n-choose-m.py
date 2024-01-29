n, m = tuple(map(int, input().split())) # n개 중에 m개 고르기
answer = []

def print_answer():
    for elem in answer:
        print(elem, end = ' ')
    print()


def choose(cur_num, cnt):
    if cur_num == m:
        print_answer()
        return
    
    for i in range(cnt, n + 1):
        if i not in answer:
            answer.append(i)
            choose(cur_num + 1, i)
            answer.pop()

    return

choose(0, 1)