N = int(input())
time = list(map(int, input().split()))
time.sort() #오름차순 정렬 (앞의 순서의 대기시간을 줄이기 위해서)

count = 0
sum = 0

for i in time:
    count += int(i)
    sum += count
print(sum)