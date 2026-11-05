print("school day planner")
print("answer 3 quesions and i will plan your day\n")

day = input("What day is today?").strip().capitalize()
weather = input("what is the weather - sunny/rainy/cloudy ").strip().lower()
work = input("your homework complete? yes|no ").strip().lower()

#if elif else to clarify day
if day in ("Saturday", "Sunday"):
    print("Day type is a weekend. Enjoy")

elif day == "Monday":
    print("day type first day of the week. Plan your week ahead")

elif day == "Friday":
    print("last school day. plan weekend")

elif day in ("Tuesday" ,"Wednesday" ,"Thursday"):
    print("regular school day stay focused")

else:
    print("Invalid")

#AND operator
if weather == "sunny" and work == "yes":
    print("Since the homework is completed lets play outside")

#OR operator
if weather == "rainy" or weather == "cloudy":
    print("Have an umbrella when you head out")

#NOT operator
if not (work == "yes"):
    print("Finish your hw before heading out")

#combining operastors
if weather == "rainy" and not (work == "yes"):
    print("Stay home and complete hw")

elif weather == "sunny" and work == "completed" and not (day in ("Sunday", "Saturday")):
    print("prepare for the school day")

elif weather == "sunny" and day in ("Saturday", "Sunday"):
    print("have fun in weekend")

else:
    print("Decide yourself")

