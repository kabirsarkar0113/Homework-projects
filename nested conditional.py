print("Welcome to ride builder")

choice = int(input("1 for bike 2 for car"))

if choice == 1:
    bike = int(input("1 for mountain bike 2 for scooter"))
    if bike == 1:
        print("mountains")
    elif bike == 2:
        print("scooters")
    else:
        print("error")
elif choice == 2:
    car = int(input("1 for Suv 2 for sedan"))
    if car == 1:
        print("family car")
    elif car == 2:
        print("city rider")
    else:
        print("error")
else:
    print("error")