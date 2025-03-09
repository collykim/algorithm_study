x = input()
if len(x) == 1:  # 10보다 작은 수를 "0X" 형태로 변환
    x = "0" + x

tmp = x
i = 0

while True:
    new = str(int(tmp[0]) + int(tmp[1]))  # 각 자리 숫자의 합
    tmp = tmp[-1] + new[-1]  # 새로운 수 생성
    i += 1
    if tmp == x:  # 원래 수로 돌아오면 종료
        break

print(i)