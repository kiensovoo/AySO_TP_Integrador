# Se define una función que solicita datos e imprime los datos ingresados.
def solicitar_datos():
    """Solicita nombre, apellido, edad y ciudad al usuario."""
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    ciudad = input("Ingrese su ciudad: ")
    
    print("\nDatos ingresados:")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")
    print("-" * 40)

# Se inicia un bucle infinito que imrpimirá un menú de opciones.
while True:
    print("Menú:")
    print("1. Ingresar datos")
    print("2. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        solicitar_datos() # Llamado a la función de solicitar datos.
    elif opcion == "2":
        print("Saliendo del programa. ¡Hasta luego!")
        break # Se sale del bucle infinito
    else:
        print("Opción no válida. Intente de nuevo.")