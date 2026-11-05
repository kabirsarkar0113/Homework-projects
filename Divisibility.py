numn = int(input("Enter a numerator: "))
numd = int(input("Enter a denominator: "))

if numn%numd == 0:
    print("\n" + str(numn) + " Is divisible by " + str(numd))
else:
    print("\n" + str(numn) + " Is not divisible by " + str(numd))