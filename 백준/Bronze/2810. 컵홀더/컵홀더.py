n = int(input())
seat = input()

couple = seat.count("LL")

if couple <= 1:
    print(n)
else:
    print(n-couple+1)