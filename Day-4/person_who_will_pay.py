# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

import random
# Total_Name_lenght = len(names)
# rand_num = random.randint(0, Total_Name_lenght - 1) # this -1 is mean that we are counting from 0 to final cumber exp if 4 names it will be counted as 3
# final_Person_to_pay = names[rand_num]

# or we can use this code
person_who_will_pay = random.choice(names)

print(f"{person_who_will_pay} is going to buy the meal today!")