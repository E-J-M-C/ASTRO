import re

#Ejercicio 1: Valida un correo que sea del IT de Cd. Altamirano
correo = "L34930049@cdaltamirano.tecnm.mx"
pattern = r"^L\d{8}@cdaltamirano\.tecnm\.mx$"
valid = re.search(pattern, correo)
if valid:
    print("El correo",(correo), "ha sido validado. ¡BIENVENIDO!")
else:
    print("El correo", (correo), "Es invalido, vuelve a intentarlo")
print("")
#Ejercicio 2: Tenemos una lista de archivos que necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt, file2.pdf, leonel.webp, secret.txt"
pattern = r"\b\w{1,100}\.txt\b"
valid = re.findall(pattern, files)
if valid:
    print("De los ficheros:", (files), "\nLos de extencion txt. son:", (valid))
else:
    print("No se encontraron ficheros con esa extencion")
print("")
#Ejercicio 3: Convinaciones de petrones
animales = "Perro, Gato, Lobo, Burro, Venado, Dinosaurio, Pescado, Pichon, Perico, Cotorro, Iguana"
print(animales)
pattern = r"P\w{1,20}|\b\w{1,20}a\b|.enad.|\b\w{4}\b|B\w{1,20}|\w$"
valid = re.findall(pattern, animales)
print(valid)
matches = re.finditer(pattern, animales)

for match in matches:
    print(match.group(), match.start(), match.end())
 

