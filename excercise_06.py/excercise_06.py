grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
column = int(input("Enter a col num from 1 to 5: ")) -1
row = int(input("Enter a row num from 1 to 5: ")) -1
grid[row][column] = 1
for i in grid:
  print(' '.join(map(str, i)))