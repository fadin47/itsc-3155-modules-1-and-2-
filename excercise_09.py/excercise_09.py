arrayList = []
for i in range(5):
  arrayList.append(input(f'Enter a word {i+1} : '))
print(arrayList)
print(' '.join(arrayList))