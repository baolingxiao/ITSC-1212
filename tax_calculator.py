def add_tax(price, tax_rate):
    t = float(tax_rate)
    p = float(price)
    Tax = p * t
    tt_tax = Tax + p
    return tt_tax



print(add_tax(50, 0.08))    # Expected: 54.0
print(add_tax(19.99, 0.07)) # Expected: 21.3893
print(add_tax(0, 0.10))     # Expected: 0.0
