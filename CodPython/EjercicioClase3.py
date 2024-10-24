try:
    edad = int(input("Por favor, ingresa tu edad: "))
    
    # Clasificar al usuario según su edad
    if edad < 13:
        print("Eres un niño.")
    elif edad >= 13 and edad <= 17:
        print("Eres un adolescente.")
    elif edad >= 18 and edad <= 64:
        print("Eres un adulto.")
    else:
        print("Eres un adulto mayor.")
        
except ValueError:
    print("Por favor, ingresa un número válido.")
