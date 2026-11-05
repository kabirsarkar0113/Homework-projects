print("enter the marks of 3 subjects\n")
m1 = int(input("m1 marks - "))
m2 = int(input("m2 marks - "))
m3 = int(input("m3 marks - "))
total = m1 + m2 + m3
avg = int(total/3)
valid_range = range(0,100)

if avg not in valid_range:
    print("invalid")
elif avg in range(91,100):
    print("grade is A")
elif avg in range(81,90):
    print("grade B")
elif avg in range(71,80):
    print("grade C")
elif avg in range(61,70):
    print("Grade D")
else:
    print("Grade E")

    