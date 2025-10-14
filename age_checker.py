def age_checker(a:int):
    if a >= 18:
        print("You can vote")
    else :
        print("Too young to vote.")

a = int(input("Enter your age"))

age_checker(a)
