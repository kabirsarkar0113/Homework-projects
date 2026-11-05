totalnotes_100 = totalnotes_50 = totalnotes_20 = totalnotes_10 = totalnotes_5 = totalnotes_1 = 0
customer = 0
total_dispensed = 0
serving = True

while serving:      # outer while loop 1 customer per loop
    name = str(input("name: "))
    amount = int(input(f"Hello, {name} enter the amount you want to withdraw: "))
    if amount <= 0:
        print("invalid amount please enter a positive number")
        continue
    print(f"\nDispensing {amount} units for {name}: ")

    remainingval = amount
    idx = 1
    while idx <= 6:  #this is the inner while loop which breaks the amount into notes
        if idx == 1:
            currency_value = 100
        elif idx == 2:
            currency_value = 50
        elif idx == 3:
            currency_value = 20
        elif idx == 4:
            currency_value = 10
        elif idx == 5:
            currency_value = 5
        else:
            currency_value = 1
        count = remainingval // currency_value
        if count > 0:
            print(f"{count}x{currency_value} - unit notes = {count*currency_value}")
            remainingval = remainingval - count*currency_value
            if currency_value == 100:
                totalnotes_100 = totalnotes_100 + count
            elif currency_value == 50:
                totalnotes_50 = totalnotes_50 + count
            elif currency_value == 20:
                totalnotes_20 = totalnotes_20 + count
            elif currency_value == 10:
                totalnotes_10 = totalnotes_10 + count
            elif currency_value == 5:
                totalnotes_5 = totalnotes_5 + count
            else:
                totalnotes_1 = totalnotes_1 + count
        idx += 1
    customer += 1
    total_dispensed += amount
    print("transaction completed for -",name)
    nextcustomer = input("is there another customer?[yes|no]: ").strip().lower()
    if nextcustomer != "yes":
        serving = False