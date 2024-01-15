l = int(input())
x_list , y_list = [], []
for i in range(l):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
one, two, three, four = 0, 0, 0, 0
for i in range(l):
    if x_list[i] > 0:
        if y_list[i] > 0:
            one += 1
        elif y_list[i] < 0:
            four += 1
    elif x_list[i] < 0:
        if y_list[i] > 0:
            two += 1
        elif y_list[i] < 0:
            print(x_list[i], y_list[i])
            three += 1
print(f'Первая четверть: {one}')
print(f'Вторая четверть: {two}')
print(f'Третья четверть: {three}')
print(f'Четвертая четверть: {four}')