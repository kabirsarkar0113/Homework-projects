# Random Fun Calculator

# PART 1: Import random and math modules
import random
import math

# PART 2: Generate a random lucky number using randint()
piyo = random.randint(1,67)
print(piyo)
# PART 3: Turn a random number into a random choice
vehicles = ["car","bus","ariplane"]
random =   random.choice(vehicles)
print(random)

# PART 5: Use math module functions
decimal_number = float(input("\nEnter a decimal number: "))
print("cieling and floor", math.ceil(decimal_number) , math.floor(decimal_number))
# PART 6: Use copysign()
x = 10
y = -5
print("Copy sign result:", math.copysign(x, y))

# PART 7: Use fabs()
negative_number = int(input("Enter a negative number: "))
print("Absolute value:", math.fabs(negative_number))

# PART 8: Use gcd()
num1 = int(input("Enter first number for GCD: "))
num2 = int(input("Enter second number for GCD: "))

print("GCD is:", math.gcd(num1, num2))
