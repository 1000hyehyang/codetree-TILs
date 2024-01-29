n= int(input()) # n 자릿수
cnt = 0  # 아름다운 수의 개수 

def beautiful(idx): 
    
    if idx == n :      
        global cnt 
        cnt +=1
        return
    
    for num in range(1,5) :
        if idx + num > n: 
            break

        beautiful(idx + num)

beautiful(0)  
print(cnt)