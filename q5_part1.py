ranges = []
ingredients = []

with open("text.txt", "r") as file:
  for line in file:
    if line != "\n":
      if "-" in line:
        ranges.append(line.strip())
      else:
        ingredients.append(int(line.strip()))


counter = 0
for num in ingredients:
  for i in ranges:
    yes = False
    start, end = map(int, i.split("-"))
    if num >= start and num <= end:
      counter += 1
      break

print(counter)
