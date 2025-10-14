def age_checker(a:int):
    if a >= 18:
        return "You can vote"
    else :
        return "Too young to vote."

a = int(input("Enter your age"))

print(age_checker(a))
