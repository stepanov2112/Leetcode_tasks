print('hello world!')
s = list(input())
nums = [int(i) for i in s]
final = []
if len(nums) == 5:
    final += nums[:-6:-1]
elif len(nums) == 6:
    print(nums[:-6:-1])
    final.append(nums[0])
    final += nums[:-6:-1]
final2 = [str(i) for i in final]
print(int(''.join(final2)))

