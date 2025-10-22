# Frågar anvädaren om ett tal mellan 0-100

def get_score(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 100:
                return value
            else:
                print("Ange ett tal mellan 0-100")
        except ValueError:
            print("Du måste skriva i siffror ej bokstäver")

# Ta in tre poäng från användaren

tal1 = get_score("Ange första talet: ")
tal2 = get_score("Ange andra talet: ")
tal3 = get_score("Ange tredje talet: ")

# Räkna ut medelvärde 

medelvärde = (tal1 + tal2 + tal3) / 3

# Skriv ut resultat med max två decimaler

print(f"\nDitt genomsnittliga betyg är: {medelvärde:.2f}")

# Gratulationsmeddelande om genomsnittet är 93 eller högre

if medelvärde > 93:
    print("Fantastiskt resultat bra jobbat!")
else:
    print("Tack, beräkningen är klar")