n, t = tuple(map(int, input().split()))
tri_a = list(map(int, input().split()))
tri_b = list(map(int, input().split()))
tri_c = list(map(int, input().split()))

for _ in range(t):
    # 왼쪽 변에서 가장 오른쪽에 있는 숫자를 따로 temp값에 저장
    temp = tri_a[n - 1]
    
    # 왼쪽 변 채우기
    for i in range(n - 1, 0, -1):
        tri_a[i] = tri_a[i - 1]
    tri_a[0] = tri_c[n - 1]
    
    # 오른쪽 변의 가장 오른쪽에 있는 숫자를 따로 temp값에 저장
    temp_2 = tri_b[n - 1]

    # 오른쪽 변 채우기
    for i in range(n - 1, 0, -1):
        tri_b[i] = tri_b[i - 1]

    # 오른쪽 변의 첫 번째 숫자를 채운다.
    tri_b[0] = temp
    
    # 밑변 채우기
    for i in range(n - 1, 0, -1):
        tri_c[i] = tri_c[i - 1]

    # 밑변의 첫 번째 숫자를 채운다.
    tri_c[0] = temp_2
    
    

# 출력
for elem in tri_a:
    print(elem, end=" ")
print()

for elem in tri_b:
    print(elem, end=" ")
print()

for elem in tri_c:
    print(elem, end=" ")