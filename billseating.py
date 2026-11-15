def total(amount,tip):
    total = amount * (1+0.01 * tip)
    total = round(total,2)
    print("pay", total)
    return total

# PART 2: Call the function with positional arguments
total(150, 20)
 
 
# PART 3: Define a recursive function with a docstring
def seating_arrangements(guests):
    '''This is a recursive function to find the number of seating arrangements for guests.'''
 
    if guests == 0 or guests == 1:
        return 1

    else:
        return guests * seating_arrangements(guests - 1)
 
# PART 4: Access and print the docstring
print(seating_arrangements.__doc__)
 
# PART 5: Display seating arrangement results
print("Seating arrangements for 1 guest:", seating_arrangements(1))
print("Seating arrangements for 2 guests:", seating_arrangements(2))
print("Seating arrangements for 3 guests:", seating_arrangements(3))
print("Seating arrangements for 5 guests:", seating_arrangements(5))
