y_cord = []
with open("text.txt", "r") as file:
  for line in file:
      y_cord.append(line)

ylen = len(y_cord)
xlen = len(y_cord[0])-1 #to account for the \n char


def check_adj(x,y):
    adj = [(x,y-1), (x,y+1), (x-1,y), (x+1,y), (x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)]
    adj = [i for i in adj if i[0] >= 0 and i[0] < xlen and i[1] >= 0 and i[1] < ylen]
    counter = 0
    for i in adj:
        if y_cord[i[1]][i[0]] == "@":
            counter += 1
    return (counter < 4)

rolls = 0
rolls_this_turn = 1
# coords come in yx instead of xy rip
while rolls_this_turn != 0:
    rolls_this_turn = 0
    for y in range(ylen):
        for x in range(xlen):
            if y_cord[y][x] == "@" and check_adj(x,y):
                    rolls += 1
                    rolls_this_turn += 1
                    y_cord[y] = y_cord[y][:x] + "." + y_cord[y][x+1:]
            else:
                pass
    if rolls_this_turn == 0:
        break

print(rolls)
