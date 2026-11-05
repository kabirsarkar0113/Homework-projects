word1 = str(input("enter a word to get the reversed string - "))
word2 = ("")

for i in word1:
    word2 = i + word2
    print(word2)
print("\nactual word- ",word1)
print("reversed word ",word2)