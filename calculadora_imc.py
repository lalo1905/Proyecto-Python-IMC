#Validamos que el nombre no este en blanco y solo contenga letras
while True:
    nombre = input("Ingresa tu nombre: ").strip()
    if nombre == "":
        print("ERROR: El campo no puede quedar vacio, Intentalo de nuevo")
    elif not nombre.replace(" ", " ").isalpha():
        print("ERROR: El nombre solo debe contener letras (sin numeros ni simbolos)")
    else:
        nombre = nombre.capitalize()
        break
  
#Validamos que el apellido paterno no este en blanco y solo contenga letras
while True:
    apellido_paterno = input("Ingresa tu apellido paterno: ").strip()
    if apellido_paterno == "":
        print("ERROR: El campo no puede quedar vacio, Intentalo de nuevo")
    elif not apellido_paterno.replace(" ", " ").isalpha():
        print("ERROR: El apellido solo debe contener letras (sin numeros ni simbolos)")
    else:
        apellido_paterno = apellido_paterno.capitalize()
        break

#Validamos que el apellido materno no este en blanco y solo contenga letras
while True:
    apellido_materno = input("Ingresa tu apellido materno: ").strip()
    if apellido_materno == "":
        print("ERROR: El campo no puede quedar vacio, Intentalo de nuevo")
    elif not apellido_materno.replace(" ", " ").isalpha():
        print("ERROR: El apellido solo debe contener letras (sin numeros ni simbolos)")
    else:
        apellido_materno = apellido_materno.capitalize()
        break

#validamos la edad asegurando que sea un numero entero
while True:
    try:
        edad = int (input("Ingresa tu edad: "))
        if edad > 0:
            break
        print("Error: La edad debe ser mayor a 0")
    except ValueError:
        print ("Error: Debes ingresar un numero entero valido") 

#Validamos el peso
while True:
    try:
        peso = float(input("Ingresa tu peso en Kg (Ej. 70.5): "))
        if peso > 0:
            break
        print("Error: La peso debe ser mayor a 0")
    except ValueError:
        print ("Error: Debes ingresar un numero  valido") 

while True:
    estatura = input("Ingresa tu estatura en metros (Ej: 1.75)").strip()
    if "." not in estatura:
        print("Debes ingresar la estatura en punto decimal obligatoriamente (Ej: 1.75)")
    else:
        try:
            estatura = float(estatura)
            if estatura > 0:
                break
            else:
                print("Error: la estatura debe ser mayor que 0")
        except ValueError:
            print("Error: debes ingresar un numero decimal valido (Ej: 1.75)")

#Aplicamos la formula del IMC
imc = peso / (estatura ** 2)

#Mostramos el resumen de los datos con f-strings al usuario
print("\n" + "="*35 )
print("\n--- RESUMEN DEL USUARIO ---")
print("="*35)
print(f"Nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
#:.2f redondea a 2 decimales
print(f"IMC: {imc:.2f}") 
print("="*35)


# enlace de github: https://github.com/lalo1905/Proyecto-Python-IMC
