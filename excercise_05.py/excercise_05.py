arrayList1 = []
for i in range(5):
  arrayList1.append(int(input(f'Enter a number : ')))
print(f'First List: {arrayList1}')
arrayList2 = []
for i in range(5):
  arrayList2.append(int(input(f'Enter a number : ')))
print(f'Second List: {arrayList2}')
x = set(arrayList1).intersection(arrayList2)
print(f'Common List: {list(x)}')