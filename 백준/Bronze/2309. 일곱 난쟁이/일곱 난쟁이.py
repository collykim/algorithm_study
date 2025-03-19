# 7개의 숫자의 합이 100이되야함 
n_list = []
for _ in range(9):
    n = int(input())
    n_list.append(n)

n_list.sort()
k = sum(n_list) - 100 # 총합과 100의 차이를 구해서 차이만큼의 숫자를 n_list에서 찾는다. #k는 총합과 100의 차이 

found = False
for i in range(9):
    for j in range(i + 1, 9):
        if n_list[i] + n_list[j] == k:
            fake1, fake2 = n_list[i], n_list[j]
            found = True
            break  # 내부 루프 탈출
    if found:
        break  # 외부 루프 탈출
n_list.remove(fake1)
n_list.remove(fake2)

for i in n_list:
    print(i)