from arreglo import Arreglo  # Importa la clase Arreglo desde el archivo arreglo.py

class Main:
    def __init__(self):
        self.mi_arreglo = Arreglo()

    def mostrar_menu(self):
        while True:
            print("Menú:")
            print("1. Insertar elemento")
            print("2. Eliminar elemento")
            print("3. Modificar elemento")
            print("4. Mostrar arreglo")
            print("5. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                elemento = input("Ingrese el elemento a insertar: ")
                self.mi_arreglo.Insertar_Ordenado(elemento)
            elif opcion == "2":
                elemento = input("Ingrese el elemento a eliminar: ")
                self.mi_arreglo.Eliminar_Ordenado(elemento)
            elif opcion == "3":
                valor_a_buscar = input("Ingrese el elemento a buscar: ")
                valor_a_reemplazar = input("Ingrese el elemento de reemplazo: ")
                self.mi_arreglo.modificar(valor_a_buscar, valor_a_reemplazar)
            elif opcion == "4":
                print("Contenido del arreglo:")
                self.mi_arreglo.mostrar()
            elif opcion == "5":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, vuelva y seleccione una opción válida.")

if __name__ == "__main__":
    main = Main()
    main.mostrar_menu()
