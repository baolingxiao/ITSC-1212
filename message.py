def full_name(first, last):
    f = str(first)
    l = str(last)
    A = f + " " + l
    return A

def welcome_message(first, last):
    f = str(first)
    l = str(last)
    A = f + l
    w = "Welcome, " + A + "!"
    return str(w)
# Tests
print(full_name("Ada", "Lovelace"))         # Expected: "Ada Lovelace"
print(welcome_message("Ada ", "Lovelace"))   # Expected: "Welcome, Ada Lovelace!"
print(welcome_message("Alan ", "Turing"))    # Expected: "Welcome, Alan Turing!"
