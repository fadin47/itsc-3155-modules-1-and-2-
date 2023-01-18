arrayList = []
for i in range(10):
  arrayList.append(int(input(f'Enter a number {i+1} : ')))
once = [i for i in arrayList if arrayList.count(i) == 1]
print(once)