from typing import List

def insertionSort(array) -> List[int]:
  for x in range(1,array.length-1):
    selection = x
    for y in range(x-1,-1,-1):
      if (array[y] > array[x]):
        array[y],array[x] = array[x],array[y]
        selection -=1
  return array
      
      
      

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
