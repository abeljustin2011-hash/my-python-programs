N = int(input())
sequence = input()

def find_shortest_unique_substring_length(s):
    for length in range(1, len(s) + 1):
        seen_substrings = set()
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring in seen_substrings:
                break
            seen_substrings.add(substring)
        else:
            return length
    return len(s)

print(find_shortest_unique_substring_length(sequence))