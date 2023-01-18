#https://stackoverflow.com/questions/6614891/turning-a-list-into-nested-lists-in-python
#takes string input from user
#splits the string into individual letters
#takes the first 3 letters in the string and splits it from the rest by placing it in an arraylist and continues to the next 3 letters placing everything inside the array till there are no more letters
#prints it out

split = input('Enter a string: ')
split = [*split]
stringsplit = [split[i:i+3] for i in range(0, len(split), 3)]
print(stringsplit)