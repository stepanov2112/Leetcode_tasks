a_list = list(map(int, input().split()))

cnt = 0

if len(a_list) > 1:
    for i in range(1, len(a_list)):
        if a_list[i] > a_list[i-1]:
            cnt += 1
print(cnt)