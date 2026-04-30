n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def count_matches(a, b):
    return sum(1 for x, y in zip(a, b) if x == y)

print(count_matches(a, b))