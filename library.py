choice = input("fiction or non fiction").lower().strip()

if choice == "fiction":
    fic = int(input(" 1 science fiction or 2 horror fiction"))
    if fic == 1 or 2:
        print("nice")
elif choice == "non fiction":
    print("nice")
else:
    print("error")