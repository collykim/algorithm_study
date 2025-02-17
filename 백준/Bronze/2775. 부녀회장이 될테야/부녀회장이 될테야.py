T = int(input()) 

for _ in range(T):
    k = int(input())  
    n = int(input())  


    floor = [i for i in range(1, n + 1)] # 0층 초기화 (0층 i호에는 i명이 거주)

    for _ in range(k):
        for j in range(1, n):
            floor[j] += floor[j - 1] 

    print(floor[-1])  
