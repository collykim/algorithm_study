x, y, w, h = list(map(int, input().split()))
line = []
line.append(abs(0-x))
line.append(abs(0-y))
line.append(abs(w-x))
line.append(abs(h-y))

print(min(line))