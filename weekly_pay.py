def weekly_pay(hours_worked: int, hourly_wage: float)-> float:
    if hours_worked <= 40:
        return hours_worked * hourly_wage
    else:
        extra = hours_worked - 40
        return (40 * hourly_wage) + (extra * (1.5 * hourly_wage))

# Tests
print(weekly_pay(35, 20))   # Expected: 700.0 
print(weekly_pay(40, 15))   # Expected: 600
print(weekly_pay(45, 10))   # Expected: 475
