# variable to hold solution
product = 1

# Get user input for the base and exponent

base = int(input("What is the base of your problem? "))
exponent = int(input("What is the exponent? "))

# Write a loop to run the exponent times and multiply by the base
for l in range(exponent):
    product *= base

# Print out the solution
print(product)