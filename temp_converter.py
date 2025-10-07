def c_to_f(celsius):
    c =  float(celsius)
    F = (c * 9/5) + 32
    return float(F)
print(c_to_f(0))     # Expected: 32.0
print(c_to_f(100))   # Expected: 212.0
print(c_to_f(20))   # Expected: 68.0
