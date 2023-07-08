import random
print("----------Welcome to the password Generator---------")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                      'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
                      'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                      'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
symbols = ['`', '!', '@', '#', '$', '%', '&', '*', ' - ']

user = int(input("How many letter you want in your password? : \n"))
num = int(input("How many number you want in your number? : \n"))
symbol = int(input("How many symbol ? \n "))
result = ""
for i in range(1, user+1):
    char = random.choice(alphabet)
    result += char
for j in range(1, num+1):
    char = random.choice(numbers)
    result += char
for k in range(1, symbol+1):
    char = random.choice(symbols)
    result += char
print(result)






