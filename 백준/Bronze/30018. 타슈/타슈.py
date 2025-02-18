N = int(input())

A = input().split()
B = input().split()


count = 0 
for i in range(N):
    if int(A[i]) > int(B[i]):
        count += int(A[i]) - int(B[i])
    else:
        pass

print(count)