def length_diff(word1, word2):
    w1 = str(word1)
    w2 = str(word2)
    lens = abs(len(w1) - len(w2))
    return int(lens)

# Tests
print(length_diff("computer", "science"))  # Expected: 1
print(length_diff("cat", "elephant"))      # Expected: 5
print(length_diff("data", "data"))         # Expected: 0
