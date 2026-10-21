#Con input capturamos los datos de texto
nombre = input("Ingresa tu nombre: ")

apellido_paterno = input("Ingresa tu apellido paterno: ")

apellido_materno = input("Ingresa tu apellido materno: ")

#Con input capturamos los datos de texto y con int los comvertimos a numero entero
edad = int (input("Ingresa tu edad: "))

#con float convierte el texto a decimales 
peso = float(input("Ingresa tu peso en Kg (Ej. 70.5): "))

estatura = float(input("Ingresa tu estatura en metros (Ej. 1.75): "))

#Aplicamos la formula del IMC
imc = peso / (estatura ** 2)

#Mostramos el peso final al usuario
print("\n--- RESULTADOS ---")
print(f"Hola {nombre} {apellido_paterno}, tu IMC es: {imc}")
