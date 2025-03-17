while True:
    n = int(input())
    if n == -1:
        break
    measure = []

    #약수를 구하는 코드 
    for i in range(1, n):
        if n % i == 0:
            measure.append(i)
        else:
            pass

        
    if sum(measure) == n:
        print(f"{n} = {' + '.join(map(str,measure))}")
    else:
        print(f"{n} is NOT perfect.")