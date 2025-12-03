def findbig(word):
    for i in range(9, 0, -1):
        if str(i) in word:
            if len(word[word.find(str(i)):-2]) < 1:
                pass
            else:
                return str(i), word[word.find(str(i))+1:]

def findsmall(word):
    for i in range(9, 0, -1):
        if str(i) in word:
            return str(i)

num = 0
with open("text.txt", "r") as file:
    for line in file:
        n1, sub = findbig(line)
        n2 = findsmall(sub)
        n3 = int(n1+n2)
        num += n3
    print(num)
