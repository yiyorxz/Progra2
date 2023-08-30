def interfaz_biblioteca():
     while True: 
      print(" hola bienvenido a la biblioteca raton lolero ")
      print("selecciona la operacion que deseas realizar")
      print("opcion 1: añadir o eliminar libro del catalogo")
      print("opcion 2: registrarse")
      print("opcion 3: prestar y devolver libros")
      print("opcion 4: consultar libros disponibles")
      print("opcion 5: historial de prestamos")
      print("opcion 6: salir")
      valor = int(input("ingresa la opcion: "))
      if valor == 5:
         break
      
      if valor ==1:
         