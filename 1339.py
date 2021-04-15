# 단어수학
n = int(input())
alps = []

for i in range(n):
    alps.append(input())

dict = {}

for alp in alps:
    k = len(alp)-1
    for s in alp:
        if s in dict:
            dict[s] += pow (10, k)
        else:
            dict[s] = pow(10, k)
        k -= 1
nums = []

for value in dict.values():
    nums.append(value)
nums.sort(reverse=True)

result, t = 0, 9
for i in range(len(nums)):
    result += nums[i]*t
    t -= 1
print(result)