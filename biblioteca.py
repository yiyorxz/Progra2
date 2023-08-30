from datetime import datetime

class Libro:
    def __init__(self, titulo, autor, N_paginas):
        self.titulo = titulo
        self.autor = autor
        self.N_paginas = N_paginas
        self.disponible = True

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

class Usuario:
    def __init__(self, nombre, ID_usuario):
        self.nombre = nombre
        self.ID_usuario = ID_usuario

class Prestamo:
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = None
        self.fecha_devolucion = None

class Catalogo_Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, titulo):
        libros_restantes = [libro for libro in self.libros if libro.titulo != titulo]
        if len(libros_restantes) < len(self.libros):
            self.libros = libros_restantes
            print(f"El libro '{titulo}' ha sido eliminado del catálogo.")
        else:
            print(f"No se encontró el libro '{titulo}' en el catálogo.")

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario {usuario.nombre} registrado con éxito.")

    def prestar_libro(self, titulo, nombre_usuario):
        libro = next((libro for libro in self.libros if libro.titulo == titulo), None)
        usuario = next((usuario for usuario in self.usuarios if usuario.nombre == nombre_usuario), None)

        if libro and usuario:
            if libro.disponible:
                libro.disponible = False
                prestamo = Prestamo(libro, usuario)
                prestamo.fecha_prestamo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.prestamos.append(prestamo)
                print(f"El libro '{titulo}' ha sido prestado a {nombre_usuario}.")
            else:
                print("El libro no está disponible.")
        else:
            print("Libro o usuario no encontrado.")

    def devolver_libro(self, titulo, nombre_usuario):
        prestamo = next((prestamo for prestamo in self.prestamos if prestamo.libro.titulo == titulo and prestamo.usuario.nombre == nombre_usuario), None)
        if prestamo:
            prestamo.libro.disponible = True
            prestamo.fecha_devolucion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"El libro '{titulo}' ha sido devuelto por {nombre_usuario}.")
        else:
            print(f"No se encontró ningún registro de préstamo para el libro '{titulo}' y el usuario '{nombre_usuario}'.")

    def consultar_libros_disponibles(self):
        libros_disponibles = [libro for libro in self.libros if libro.disponible]
        return libros_disponibles

    def historial_prestamos(self):
        if self.prestamos:
            print("Historial de préstamos:")
            for prestamo in self.prestamos:
                print(f"Usuario: {prestamo.usuario.nombre}, Libro: {prestamo.libro.titulo}, "
                      f"Fecha de préstamo: {prestamo.fecha_prestamo}, Fecha de devolución: {prestamo.fecha_devolucion}")
        else:
            print("No hay registros de préstamos.")

    def agregar_libro_consola(self):
        titulo = input("Ingrese título del libro: ")
        autor = input("Ingrese nombre del autor del libro: ")
        N_paginas = int(input("Ingrese número de páginas del libro: "))
        libro = Libro(titulo, autor, N_paginas)
        self.agregar_libro(libro)
        print(f"El libro '{titulo}' ha sido agregado al catálogo.")

def interfaz_biblioteca():
    biblioteca = Catalogo_Biblioteca()

    while True:
        print("\nBienvenido a la Biblioteca Ratón Lolero")
        print("Selecciona la operación que deseas realizar:")
        print("1. Añadir o eliminar libro del catálogo")
        print("2. Registrarse")
        print("3. Prestar y devolver libros")
        print("4. Consultar libros disponibles")
        print("5. Historial de préstamos")
        print("6. Salir")

        opcion = input("Ingresa el número de la opción que deseas: ")

        if opcion == '6':
            break

        if opcion == '1':
            print("\n1. Añadir libro al catálogo")
            print("2. Eliminar libro del catálogo")
            subopcion = input("Selecciona una opción: ")

            if subopcion == '1':
                biblioteca.agregar_libro_consola()
            elif subopcion == '2':
                titulo = input("Ingresa el título del libro a eliminar: ")
                biblioteca.eliminar_libro(titulo)
            else:
                print("Opción no válida.")

        elif opcion == '2':
            nombre = input("Ingresa tu nombre: ")
            ID_usuario = input("Ingresa tu ID de usuario: ")
            usuario = Usuario(nombre, ID_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == '3':
            print("\n1. Prestar libro")
            print("2. Devolver libro")
            subopcion = input("Selecciona una opción: ")

            if subopcion == '1':
                titulo = input("Ingresa el título del libro a prestar: ")
                nombre_usuario = input("Ingresa tu nombre de usuario: ")
                biblioteca.prestar_libro(titulo, nombre_usuario)
            elif subopcion == '2':
                titulo = input("Ingresa el título del libro a devolver: ")
                nombre_usuario = input("Ingresa tu nombre de usuario: ")
                biblioteca.devolver_libro(titulo, nombre_usuario)
            else:
                print("Opción no válida.")

        elif opcion == '4':
            libros_disponibles = biblioteca.consultar_libros_disponibles()
            if libros_disponibles:
                print("\nLibros disponibles:")
                for libro in libros_disponibles:
                    print(libro)
            else:
                print("No hay libros disponibles en este momento.")

        elif opcion == '5':
            biblioteca.historial_prestamos()

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    interfaz_biblioteca()