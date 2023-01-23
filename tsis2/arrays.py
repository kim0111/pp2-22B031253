cars = ["Ford", "Volvo", "BMW"]
# y = cars[0]
cars[0] = "Toyota"
x = len(cars)
cars.append("Honda")

for x in cars:
  print(x)


cars.pop(1)#удалить второй элемент в массиве


print("\n")

for x in cars:
  print(x)
