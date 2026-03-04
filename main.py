import random

passwordLength = int(input("Wie lange muss das Passwort sein?"))
characters = input("Welche Zeichen sollen benutzt werden?")
passwords = int(input("Wie viel Passwörter willst du haben?"))

for i in range(passwords):
    password = ""
    
    for j in range(passwordLength):
        randomCharacter = random.choice(characters)
        password = password + randomCharacter
    print(i + 1, ".", password)
    

