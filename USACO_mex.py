n = int(input())
array = [int(x) for x in input().split()]
freq = [0] * (n + 1)
missing = 0

for x in array:
    freq[x] += 1

for i in range(n + 1):
    print(max(missing, freq[i]))
    if freq[i] == 0:
        missing += 1