import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# total_chars = len(letters) + len(numbers) + len(symbols)

lettersLim = int(input("How many Letters do you want: "))
symbolsLim = int(input("How many Symbols do you want: "))
numsLim = int(input("How many Numbers do you want: "))
totalLength = lettersLim + symbolsLim + numsLim
passOld = []
randomPlace = 0

for x in range(lettersLim):
    randomPlace = random.randint(0, len(letters)-1)
    passOld.append(letters[randomPlace])
for x in range(symbolsLim):
    randomPlace = random.randint(0, len(symbols)-1)
    passOld.append(symbols[randomPlace])
for x in range(numsLim):
    randomPlace = random.randint(0, len(numbers)-1)
    passOld.append(numbers[randomPlace])

random.shuffle(passOld)
password = ""
for x in range(0, len(passOld)):
    # print(passOld[x], end='') That's One way to print it
    password += passOld[x]
print(password)
