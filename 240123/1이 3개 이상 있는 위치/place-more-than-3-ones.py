n = int(input())

# arr_2d = []
# for _ in range(n):
#     arr_2d.append(list(map(int, input().split())))

# n개의 줄에 걸쳐 각 줄마다 각각의 행에 해당하는 n개의 숫자가 공백을 사이에 두고 주어짐.

arr_2d = [ 
    list(map(int, input().split()))
    for _ in range(n)
]


# 격자 범위를 넘어가 index 오류 방지
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


ans = 0
for x in range(n):
    for y in range(n):
        # (x, y) 칸에 대해서
        # 인접한 칸에 숫자 1이 3개 이상 있는지 확인
                  # 동 서 남 북 (x, y)칸 기준 1칸씩 옮기는 방향
        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and arr_2d[nx][ny] == 1:
                cnt += 1
            
        # (x, y) 인접한 칸에 있는 1의 개수가 3 이상이라면
        # 답을 갱신
        if cnt >= 3:
            ans += 1

print(ans)