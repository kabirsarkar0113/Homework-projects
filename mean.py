mean = 72
number_vals = 30
correct_val = 42
wrong_val = 36
sum = mean*number_vals
print("Sum of 30 vals is",sum)
new_sum = sum -(wrong_val - correct_val)
print("The new total is",new_sum)
actual_mean = new_sum/number_vals
print("The actual mean is",actual_mean)