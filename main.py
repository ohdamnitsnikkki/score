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

tal1 = get_number("Ange första talet: ")
tal2 = get_number("Ange andra talet: ")
tal3 = get_number("Ange tredje talet: ")