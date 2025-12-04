def kill_lowest(word):
    for i in range(1, 10):
        if str(i) in word:
            x = word.find(str(i))
            return word[:x] + word[x+1:]
def slidingwindow(word):
    # worst implementation ever!!!
    for i in range(len(word)-1):
        if word[i] < word[i+1]:
            return word[:i] + word[i+1:]
        else:
            pass
    return word
    
num = 0
with open("text.txt", "r") as file:
  for line in file:
      for i in range(88):
          line = slidingwindow(line)
      if len(line) > 12:
          for i in range(len(line)-13):
              line = kill_lowest(line)
      num += int(line)
      print(line)
  print(num)
