n, l = map(int, input().split())
hole = list(map(int, input().split()))
hole.sort()

start = hole[0]
count = 1

for i in hole[1:]:
    if i in range(start, start+l):
        continue
    else:
        start = i
        count += 1
print(count)