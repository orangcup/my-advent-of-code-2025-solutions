tick = 50
direction = ""
rotate = 0
counter = 0
with open("text.txt", "r") as file:
    for line in file:
        direction = line[0]
        rotate = int(line[1:])

        if direction == "L":
            for i in range(rotate):
                tick -= 1
                tick %= 100
                if tick == 0:
                    counter += 1
                
        if direction == "R":
            for i in range(rotate):
                tick += 1
                tick %= 100
                if tick == 0:
                    counter += 1
    print(counter)
