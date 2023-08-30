class Catalogo_Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)

    def Registro_usuario(self, usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, libro, usuario):
        if libro in self.libros and libro.disponible:
            libro.disponible = False
            prestamo = Prestamo(libro, usuario)
            prestamo.fecha_prestamo = input("Ingrese fecha de solicitud: ")
            self.prestamos.append(prestamo)
            return prestamo
        else:
            print("El libro no está disponible")
            return None

    def devolver_libro(self, prestamo):
        prestamo.libro.disponible = True
        prestamo.fecha_devolucion = input("Ingrese fecha devolución: ")

    def consulta(self):
        libros_disponibles = [libro for libro in self.libros if libro.disponible]
        return libros_disponibles

    def agregar_consola(self):
        titulo = input("Ingrese título del libro: ")
        autor = input("Ingrese nombre del autor del libro: ")
        N_paginas = int(input("Ingrese número de páginas del libro: "))
        libro = Libro(titulo, autor, N_paginas)
        self.agregar_libro(libro)
        print(f"El libro '{titulo}' ha sido agregado al catálogo :) ")

def interfaz_biblioteca():
    biblioteca = Catalogo_Biblioteca()

    while True:
        print("Hola, bienvenido a la biblioteca Ratón Lolero")
        print("Selecciona la operación que deseas realizar:")
        print("Opción 1: Añadir o eliminar libro del catálogo")
        print("Opción 2: Registrarse")
        print("Opción 3: Prestar y devolver libros")
        print("Opción 4: Consultar libros disponibles")
        print("Opción 5: Historial de préstamos")
        print("Opción 6: Salir")

        valor = int(input("Ingresa la opción: "))

        if valor == 6:
            break

        if valor == 1:
            print("\n1. Añadir libro al catálogo")
            print("2. Eliminar libro del catálogo")
            opcion = int(input("Selecciona una opción: "))

            if opcion == 1:
                biblioteca.agregar_consola()
            elif opcion == 2:
                # Agrega lógica para eliminar un libro del catálogo si lo deseas
                pass
            else:
                print("Opción no válida.")

        elif valor == 2:
            nombre = input("Ingresa tu nombre: ")
            ID_usuario = input("Ingresa tu ID de usuario: ")
            usuario = Usuario(nombre, ID_usuario)
            biblioteca.Registro_usuario(usuario)
            print(f"Usuario {nombre} registrado con éxito.")

        elif valor == 3:
            # Agrega lógica para prestar y devolver libros si lo deseas
            pass

        elif valor == 4:
            libros_disponibles = biblioteca.consulta()
            if libros_disponibles:
                print("\nLibros disponibles:")
                for libro in libros_disponibles:
                    print(f"- {libro.titulo} (Autor: {libro.autor}, Páginas: {libro.N_paginas})")
            else:
                print("No hay libros disponibles en este momento.")

        elif valor == 5:
            # Agrega lógica para mostrar el historial de préstamos si lo deseas
            pass

        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    interfaz_biblioteca()
