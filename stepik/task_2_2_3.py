a = list(map(int, input().split()))

b = a.copy()
if len(a)>1:
    for i in range(len(a)//2):
        b[2*i], b[2*i+1] = a[2*i+1], a[2*i]

for i in b:
    print(i, end=' ')