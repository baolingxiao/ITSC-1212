def age_checker(a: int)-> str:
    if a < 18 :
        return "Too young to vote!"
    elif a >= 18 and a < 21:
        return "You can vote!"
    elif a >= 21 and a < 65:
        return "You can drink and vote!"
    else:
        return "You can vote, drink and retire soon!"

a = int(input("Please Enter your age for check vote"))

print(age_checker(a))
