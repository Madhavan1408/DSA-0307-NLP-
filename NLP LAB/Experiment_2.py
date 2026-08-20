def fsa_ends_with_ab(string):
    state = 0
    for ch in string:
        if state == 0:
            state = 1 if ch == 'a' else 0
        elif state == 1:
            state = 2 if ch == 'b' else (1 if ch == 'a' else 0)
        elif state == 2:
            state = 1 if ch == 'a' else 0
    return state == 2

test_strings = ["ab", "aab", "abb", "aabb", "ba", "abab", "cab", "xyz", "a", "b"]

for s in test_strings:
    result = fsa_ends_with_ab(s)
    print(f"String '{s}' -> {'Accepted' if result else 'Rejected'}")

