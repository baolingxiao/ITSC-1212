def cool_check(word: str, number: int)-> str:
    if len(word) >= 5 and number % 2 == 0:
        return "cool"
    elif len(word) < 5 or number % 2 != 0:
        return "less cool"


# Tests
print(cool_check("apple",4))      # Expected: "cool"
print(cool_check("hi",8))         # Expected: "less cool" 
print(cool_check("great", 3))     # Expected: "less cool"
print(cool_check("grape", 2))     # Expected: "cool"
