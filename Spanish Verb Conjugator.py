# INPUT
valido = False

# Agregamos un ciclo while para que siga preguntando si hay un error
while not valido:
    verbo = input("Ingrese verbo regular en infinitivo: ")
    
    # PROCESS
    # Limpiamos espacios extra
    verbo = verbo.strip().lower()
    
    pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

    terminaciones = {
        'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
        'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
        'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
    }

    # Validamos que el usuario no haya escrito un texto muy corto o vacío
    if len(verbo) < 2:
        print("Error: El texto es demasiado corto. Intenta de nuevo.\n")
    # Validamos que solo tenga letras (sin números ni símbolos)
    elif not verbo.isalpha():
        print("Error: Ingrese solo letras, sin números ni espacios intermedios.\n")
    else:
        # Sacamos la raíz y la terminación
        raiz = verbo[:-2]
        terminacion = verbo[-2:]

        # Manejo de Errores (Error Handling)
        try:
            terminaciones_verbo = terminaciones[terminacion]
            valido = True 
        except KeyError:
            # Si el diccionario no encuentra 'ar', 'er' o 'ir', intentar de nuevo
            print(f"Error: La palabra '{verbo}' no termina en 'ar', 'er' o 'ir'. Intenta de nuevo.\n")


# OUTPUT
print(f"\nConjugación de {verbo}:")
for i in range(len(pronombres)):
    print(pronombres[i] + " " + raiz + terminaciones_verbo[i])
