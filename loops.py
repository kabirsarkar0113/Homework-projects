# ================================
# POWER CALCULATOR
# ================================

print("=== Power Calculator ===")

# ---------- PART 1: ask the two questions ----------
# YOUR CODE HERE
# Ask for the base number and store it in  base
# Ask for the power and store it in  exponent
# Wrap both in int() — you cannot multiply text.
base = int(input("base number"))
exponent = int(input("exponent"))

# ---------- PART 2: the running total ----------
# YOUR CODE HERE
# Create a variable called  result  and start it at 1.
# Think about why 1 and not 0 before you write it. The hint below explains.
result = 1

# ---------- PART 3 + 4: the loop that multiplies ----------
# YOUR CODE HERE
# for i in range(1, exponent + 1):
#     multiply result by base and store it back in result
#     print which step you are on and what result is now
for i in range(1, exponent + 1):
    result = result * base
    print("Step", i, ": result =", result)

# ---------- PART 5: the answer ----------
# YOUR CODE HERE
print("\nAnswer:", base, "to the power", exponent, "=", result)