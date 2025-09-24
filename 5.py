
n = int(input("¿Cuántas palabras deseas ingresar?: "))

palabras = []
for i in range(n):
    palabra = input(f"Ingrese la palabra {i+1}: ").lower()
    palabras.append(palabra)


palindromas = []
for palabra in palabras:
    if palabra == palabra[0:8:-1]:  
        palindromas.append(palabra)

print("\nPalabras ingresadas:", palabras)
if palindromas:
    print("Palabras palíndromas encontradas:", palindromas)
else:
    print("No se encontraron palabras palíndromas.")
