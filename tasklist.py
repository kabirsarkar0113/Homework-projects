total_chores = 4
original_count = total_chores
print(f"You have got {total_chores} chores to finish")
completed_count = 0
chore_number = 1   

while chore_number <= total_chores:
    if chore_number == 1:
        next_chore = "make your bed"
    elif chore_number == 2:
        next_chore = "clean the floor"
    elif chore_number == 3:
        next_chore = "feed the pet"
    else:
        next_chore = "wash the dishes"
    answer = input("have you finished: " + next_chore + "yes/no : ")
    if answer == "yes":
        completed_count += 1
        chore_number += 1
        print("great you have finished a chore.chores remaining",)
    else:
        print("finish it and check again")
    print("remaining chores are: ", total_chores - completed_count)

print("\nthe chores are completed")
print("\nchore checklist summary")
print("original_count:",original_count)
print("completed_count:",completed_count)
print("remaining_chores:",total_chores - completed_count)