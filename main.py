l = input().split()

print(*list(map(lambda x: 255-int(x),l)))