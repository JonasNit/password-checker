import random
while True:
    print("1 - Passwort generieren")
    print("2 - Passwort anzeigen")
    print("3 - Beenden")

    choice = input("Auswahl: ")
    
    if choice == "1":
        passwordLength = int(input("Wie lange muss das Passwort sein?"))
        characters = input("Welche Zeichen sollen benutzt werden?")
        passwords = int(input("Wie viel Passwörter willst du haben?"))
        service = input("Für welchen Dienst soll das Passwort sein?")

    for i in range(passwords):
     password = ""
    
    for j in range(passwordLength):
        randomCharacter = random.choice(characters)
        password = password + randomCharacter
    print(service , "." , password)

    generated_password = password
    with open("passwords.txt", "a") as file:    file.write(generated_password + "\n")
    elif choice == "2": 
        with open("passwords.txt", "r") as file:
            passwords = file.read()
            print(passwords)
    elif choice == "3":
        break
 else:
     print("Ungültige Auswahl, bitte versuche es erneut.")   
