print("pool entry chk\n")

age = int(input("How old are you?"))
swim = input("Can swim'?")

if age < 18 and swim == "no":
    print("Get out!")
elif age > 18 and not swim == "yes":
    print("YOur choice")
elif age < 12 or swim == "no":
    print("Access denied")

else:
    print("swim")


