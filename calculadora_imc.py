#Con input capturamos los datos de texto
nombre = input("Ingresa tu nombre: ").capitalize()

apellido_paterno = input("Ingresa tu apellido paterno: ").capitalize()

apellido_materno = input("Ingresa tu apellido materno: ").capitalize()

#Con input capturamos los datos de texto y con int los comvertimos a numero entero
edad = int (input("Ingresa tu edad: "))

#con float convierte el texto a decimales 
peso = float(input("Ingresa tu peso en Kg (Ej. 70.5): "))

estatura = float(input("Ingresa tu estatura en metros (Ej. 1.75): "))

#Aplicamos la formula del IMC
imc = peso / (estatura ** 2)

#Mostramos el resumen de los datos con f-strings al usuario
print("\n" + "="*35 )
print("\n--- RESUMEN DEL USUARIO ---")
print("="*35)
print(f"Nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Estatura {estatura} m")
#:.2f redondea a 2 decimales
print(f"IMC: {imc:.2f}") 
print("="*35)


# enlace de github: https://github.com/lalo1905/Proyecto-Python-IMC
