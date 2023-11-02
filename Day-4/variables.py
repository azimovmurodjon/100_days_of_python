# There are two variables, a and b
a = input()
b = input()
# Create a third variable to help switch the values
temp = b
b = a
a = temp

print("a: " + a)
print("b: " + b)