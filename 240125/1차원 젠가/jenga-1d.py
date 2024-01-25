n = int(input())

blocks = [
    int(input())
    for _ in range(n)
]

# 첫 번째 블록 제거
s1, e1 = map(int, input().split())
blocks = blocks[:s1-1] + blocks[e1:]

# 두 번째 블록 제거
s2, e2 = map(int, input().split())
blocks = blocks[:s2-1] + blocks[e2:]

# 중력에 의해 떨어진 블록 재정렬
blocks = [block for block in blocks if block != 0]

# 결과 출력
print(len(blocks))
for block in blocks:
    print(block)