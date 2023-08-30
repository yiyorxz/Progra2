class Libro:
    def __init__(self,titulo,autor,N_paginas):
        self.titulo= titulo
        self.autor= autor
        self.N_paginas= N_paginas
        self.disponible = True
    

class Usuario:
    def __init__(self,nombre,ID_usuario):
        self.nombre = nombre
        self.ID_usuario = ID_usuario


class Prestamo:
    def __init__(self,libro,usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = None
        self.fecha_devolucion = None


class Catalogo_Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    
    def agregar_libro(self,libro):
        self.libros.append(libro)

    def eliminar_libro(self,libro):
     if libro in self.libros:
      self.libros.remove(libro)

    def Registro_usuario(self,usuario):
       self.usuarios.append(usuario)

    def prestar_libro(self,libro,usuario):
       if libro in self.libros and libro.disponible:
          libro.disponible = False
          prestamo = Prestamo(libro,usuario)
          prestamo.fecha_prestamo = (input("ingrese fecha de solicitud: "))
          self.prestamos.append(prestamo)
          return prestamo
       else:
          print("el libro no esta disponible")
          return None
       
    def devolver_libro(self,prestamo):
       prestamo.libro.disponible = True
       prestamo.fecha_devolucion = (input("ingrese fecha devolucion"))

    def consulta(self):
       libros_disponibles = [libro for libro in self.libros if libro.disponible]
       return libros_disponibles
   
    def agregar_consola(self):
       titulo = input("ingrese titulo del libro: ")
       autor = input("ingrese nombre del autor del libro: ")
       N_paginas = int(input("ingrese numero de paginas del libro: "))
       libro = Libro(titulo,autor,N_paginas)
       self.agregar_libro(libro)
       print(f"el libro '{titulo}' ha sido agregado al catalogo :) ")