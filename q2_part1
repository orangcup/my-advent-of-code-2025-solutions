def checkrepeat(word):
    for i in range(1, len(word)):
        if word[:len(word)//2] == word[len(word)//2:]:
            return True
    return False

def sum_invalid(min, max):
    lister = []
    for i in range(min, max + 1):
        if checkrepeat(str(i)):
            lister.append(i)
    return sum(lister)

with open("text.txt", "r") as file:
    stuff = file.read()
    big_list = 0
    stuff = stuff.split(",")
    for item in stuff:
        item = item.split("-")
        big_list += sum_invalid(int(item[0]), int(item[1]))
    print(big_list)
