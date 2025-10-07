def tip(amount, percent):
    a = float(amount)
    p = float(percent)
    tip_amount = a * p
    return float(tip_amount)

def total_with_tip(amount, percent):
    a = float(amount)
    p = float(percent)
    tip_amount = a * (1 + p)
    return float(tip_amount)

# Tests
print(tip(50, 0.2))             # Expected: 10.0
print(total_with_tip(50, 0.2))  # Expected: 60.0
print(total_with_tip(80, 0.15)) # Expected: 92.0
