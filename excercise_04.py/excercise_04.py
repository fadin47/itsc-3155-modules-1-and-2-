x = int(input('Enter a number: '))
arrayList = []
for i in range(x):
  arrayList.append(int(input(f'Enter a number {i+1}: ')))
print(arrayList)
print(f'Average:  {sum(arrayList) / len(arrayList)}')