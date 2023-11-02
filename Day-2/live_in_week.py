age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

weeks = 52
months = 12
days = 365
left_days = (90 - int(age)) * days
left_weeks = (90 - int(age)) * weeks
left_months = (90 - int(age)) * months


print(f"You have {left_days} days, {left_weeks} weeks, and {left_months} months left.")
