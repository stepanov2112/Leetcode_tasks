a = list(map(int, input().split()))

cnt = 1
for i in range(1, len(a)):
    if a[i] != a[i-1]:
        cnt += 1 

print(cnt)

#2 2 5 5 5 5 8 10 10