print("Floyds triangle pattern: ")
row = int(input("Enter the number of rows you want: "))
number = 0

for i in range(1,row+1):
    for j in range(1,i+1):
        number += 1
        print(number,end="")
        
    print()