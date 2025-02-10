N, H = input().split()
card = input().split()

N = int(N)
H = int(H)

count = 0  # 사용한 카드 개수
for i in card:
    H -= int(i)
    count += 1
    if H <= 0:
        print(count)
        break
            # 상대가 죽으면 카드 개수 반환
else:
    print(-1)