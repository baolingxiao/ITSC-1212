def num_checker(num:float):
    if num > 0 :
        return 1
    else :
        return -1

# Tests
print(num_checker(50))    # Expected: 1
print(num_checker(0))     # Expected: 1
print(num_checker(-3))    # Expected: -1
