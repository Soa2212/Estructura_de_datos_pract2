class Arreglo:
    def __init__(self):
        self.Max = 20
        self.A = [None] * self.Max
        self.N = -1

    def Buscar_Ordenado(self, elemento):
        self.N += 1
        index = self.N
        while index > 0 and elemento < self.A[index - 1]:
            self.A[index] = self.A[index - 1]
            index -= 1
        self.A[index] = elemento

    def Insertar_Ordenado(self, elemento):
        if self.N == self.Max - 1:
            print("El arreglo está lleno")
        else:
            self.Buscar_Ordenado(elemento)


    def Eliminar_Ordenado(self, elemento):
        if elemento in self.A:
            while elemento in self.A:
                index = self.A.index(elemento)
                for i in range(index, self.N):
                    self.A[i] = self.A[i + 1]
                self.A[self.N] = None
                self.N -= 1
        else:
            print(f"Elemento no encontrado")

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
            print(f"Elemento no encontrado")
    

mi_arreglo = Arreglo()

mi_arreglo.Insertar_Ordenado(3)
mi_arreglo.Insertar_Ordenado(1)
mi_arreglo.Insertar_Ordenado(2)

mi_arreglo.mostrar()
mi_arreglo.Insertar_Ordenado(4)
mi_arreglo.Insertar_Ordenado(1)

mi_arreglo.mostrar()


mi_arreglo.modificar(2, 4)
mi_arreglo.mostrar()
mi_arreglo.Eliminar_Ordenado(3)
mi_arreglo.mostrar()



