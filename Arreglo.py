class Arreglo:
    def __init__(self):
        self.Max = 20
        self.A = [None] * self.Max
        self.N = -1
        self.uppercase = []  # Lista para letras mayúsculas
        self.lowercase = []  # Lista para letras minúsculas

    def Borrar_Arreglo(self):
        self.N = -1
        self.uppercase = []  # Limpiar la lista de mayúsculas
        self.lowercase = []  # Limpiar la lista de minúsculas

    def Insertar_Ordenado(self, elemento):
        if self.N == self.Max - 1:
            print("El arreglo está lleno")
        else:
            # Clasificar el elemento en mayúsculas o minúsculas
            if elemento.isupper():
                self.uppercase.append(elemento)
            else:
                self.lowercase.append(elemento)

            # Ordenar ambas listas
            self.uppercase.sort()
            self.lowercase.sort()

            # Combinar las listas ordenadas en el arreglo principal
            self.A[:len(self.uppercase)] = self.uppercase
            self.A[len(self.uppercase):len(self.uppercase) + len(self.lowercase)] = self.lowercase

            self.N = len(self.uppercase) + len(self.lowercase) - 1  # Actualizar la posición N

    def mostrar(self):
        elementos = []
        for i in range(self.N + 1):
            elementos.append(self.A[i])
        resultado = ' '.join(map(str, elementos))
        print(resultado)

    def modificar(self, valor_a_buscar, valor_a_reemplazar):
        if valor_a_buscar in self.A:
            self.Eliminar_Ordenado(valor_a_buscar)
            self.Insertar_Ordenado(valor_a_reemplazar)
        else:
            print(f"Elemento no fue encontrado")
