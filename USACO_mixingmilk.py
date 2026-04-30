capacity = [0, 0, 0]
milk = [0, 0, 0]

for i in range(3):
    line = input()
    capacity[i], milk[i] = map(int, line.split())

for i in range(100):
    from_bucket = i % 3
    to_bucket = (i + 1) % 3

    amount_to_pour = min(milk[from_bucket], capacity[to_bucket] - milk[to_bucket])
    milk[from_bucket] -= amount_to_pour
    milk[to_bucket] += amount_to_pour

for i in milk:
    print(i)