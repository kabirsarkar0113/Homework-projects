#CODE HERE
# Ask for the homework time in minutes.
# Turn the answer into a whole number with int().
tabodi = int(input("YO man what your homework time in mins"))
# ---------- PART 2: choose a plan ----------
# YOUR CODE HERE
# If the homework time is more than 60, set plan to "start homework now"
# and print "That is a long homework session."
# Otherwise, set plan to "finish homework quickly"
# and print "That is a short homework session."
if tabodi > 60:
    plan = "Do homework now"
    print("boeing")
else:
    plan = "im done"
    print("car!")
# ---------- PART 3: free time ----------
# YOUR CODE HERE
# Ask: Is there free time after homework? (yes/no)
# If the answer is "yes", print a reminder to pick a hobby.
# If the answer is anything else, print nothing.
piyo = str(input("you free now?"))
if piyo == "yes":
    print("hobby")
else:
    print("airbus")
# ---------- PART 4: summary ----------
print("===== DAILY PLAN =====")
print("Homework minutes:", tabodi)
print("Plan:", plan)
print("Free time:", piyo)
