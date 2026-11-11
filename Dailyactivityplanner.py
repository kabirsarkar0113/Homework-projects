# ================================
# DAILY ACTIVITY PLANNER
# ================================

# ---------- PART 1: homework time ----------
# YOUR CODE HERE
# Ask for the homework time in minutes.
# Turn the answer into a whole number with int().
hw_time = int(input("hw time in mins"))
# ---------- PART 2: choose a plan ----------
# YOUR CODE HERE
# If the homework time is more than 60, set plan to "start homework now"
# and print "That is a long homework session."
# Otherwise, set plan to "finish homework quickly"
# and print "That is a short homework session."
if hw_time > 60:
    plan = "start hw now"
    print("Thats a long session")
else:
    plan = "finish quickly"
    print("Thats very short")
# ---------- PART 3: free time ----------
# YOUR CODE HERE
# Ask: Is there free time after homework? (yes/no)
# If the answer is "yes", print a reminder to pick a hobby.
# If the answer is anything else, print nothing.
ask = input("is there free time aft hw? yes/no ? ").lower()
if ask == "yes":
    print("Here is a reminder to pick hobby")
else:
    print("nothing")
# ---------- PART 4: summary ----------
print("===== DAILY PLAN =====")
# YOUR CODE HERE
# Print the homework minutes, the plan and the free time answer.
print(hw_time)
print(plan)
print("free time yes or no - ",ask)