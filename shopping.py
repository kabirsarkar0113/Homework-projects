# ================================
# SHOPPING DISCOUNT CALCULATOR
# ================================

# ---------- PART 1: retry loop ----------
valid = False
# YOUR CODE HERE
# Start a while loop that runs while valid is False (while not valid).
while not valid:
    
    # ---------- PART 2: input and calculation ----------
    # YOUR CODE HERE
    # Start a try block. Inside it:
    #   Ask for the bill, and turn it into a number with float().
    #   Ask for the discount percent, and turn it into a number with float().
    #   Ask for the number of people, and turn it into a whole number with int().
    #   Work out the discount amount, the final bill and what each person pays.
    try:
        bill = float(input("whats the bill?"))
        perc = float(input("whats the discount%?"))
        ppl = int(input("whats the number of people?"))

        discount = bill * perc / 100
        final = bill - discount
        
    # ---------- PART 3: handle errors ----------
    # YOUR CODE HERE
    # except ValueError: print a message about typing numbers only.
    # except ZeroDivisionError: print a message that people cannot be 0.
    except ValueError:
        print("numbers only")
    except ZeroDivisionError:
        print("ppl cant be 0")
    # ---------- PART 4: else and finally ----------
    # YOUR CODE HERE
    # else: print the final bill and what each person pays, then set valid = True.
    # finally: print "Attempt finished."
    else:
        print("total:", final)
        print("each person pays" , final/ppl)
        valid = True
    finally:
        print("boeing")