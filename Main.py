import re
from Arreglo import Arreglo  # Importa la clase Arreglo desde el archivo arreglo.py

class Main:
    def __init__(self):
        self.mi_arreglo = Arreglo()

    def mostrar_menu(self):
        solo_letras = r'^[a-zA-Z]$'

        while True:
            print("Menú:")
            print("1. Insertar elemento")
            print("2. Eliminar elemento")
            print("3. Modificar elemento")
            print("4. Borrar arreglo")
            print("5. Mostrar arreglo")
            print("6. Creditos")
            print("7. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                elemento = input("Ingrese el elemento a insertar: ")
                if re.match(solo_letras, elemento):
                    self.mi_arreglo.Insertar_Ordenado(elemento)
            elif opcion == "2":
                elemento = input("Ingrese el elemento a eliminar: ")
                if re.match(solo_letras, elemento):
                    self.mi_arreglo.Eliminar_Ordenado(elemento)
            elif opcion == "3":
                valor_a_buscar = input("Ingrese el elemento a buscar: ")
                valor_a_reemplazar = input("Ingrese el elemento de reemplazo: ")
                if re.match(solo_letras,valor_a_buscar) and re.match(solo_letras,valor_a_reemplazar):
                    self.mi_arreglo.modificar(valor_a_buscar, valor_a_reemplazar)
            elif opcion == "4":
                self.mi_arreglo.Borrar_Arreglo()
            elif opcion == "5":
                print("Contenido del arreglo:")
                self.mi_arreglo.mostrar()
            elif opcion == "6":
                print("Alfredo Cholico -- 22170184")
                print("Omar Alejandro Gonzales Sandoval -- 22170116")
                print("Jose Angel Gabriel Tovar Uribe -- 22170097")
            elif opcion == "7":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, vuelva y seleccione una opción válida.")

if __name__ == "__main__":
    main = Main()
    main.mostrar_menu()
