arrayList = []
valid = True
while valid:
  x = input('Enter a number or QUIT to quit: ')
  if x == 'QUIT':
    break
  arrayList.append(int(x))
even = [i for i in arrayList if i % 2 == 0]
print(even)