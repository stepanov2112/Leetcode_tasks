a = list(map(int, input().split()))

print(a[-1], end=' ')
for i in range(len(a)-1):
    print(a[i], end=' ')