n = int(input())
ans = 0
seq = []


def is_beautiful():
    # 연달아 같은 숫자가 나오는 시작 위치를 잡습니다.
    i = 0 # 현재까지 확인한 수열의 위치
    while i < n:
        # 현재 위치에서 시작하는 연속된 숫자들이 수열을 초과하면 아름다운 수가 아니다.
        if i + seq[i] - 1 >= n:
            return False
            
        # 현재 위치부터 seq[i]만큼의 길이만큼의 범위에서 숫자가 모두 같은지 확인한다.
        for j in range(i, i + seq[i]):
            if seq[j] != seq[i]:
                return False
            
        i += seq[i]
        
    return True


def count_beautiful_seq(cnt):
    global ans
    
    if cnt == n:
        if is_beautiful():
            ans += 1
        return
	
    for i in range(1, 5):
        seq.append(i)
        count_beautiful_seq(cnt + 1)
        seq.pop()


count_beautiful_seq(0)
print(ans)