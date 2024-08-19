class Vehiculo:
    contador_vehiculo = 0

    def __init__(self, marca_del_vehiculo, modelo, estado):
        self.marca = marca_del_vehiculo  # PUBLICO
        self.modelo = modelo            # PUBLICO
        # PROTEGIDO -> sea accedido desde la clase misma o clases hijas
        self._estado = estado
        # PRIVADO -> solo sea accedido desde la clase misma
        self.__id_vehiculo = Vehiculo.contador_vehiculo + 1

        Vehiculo.contador_vehiculo += 1
        # name mangling -> python esta modificando el nombre del atributo, o metodo

    def mostrar_info(self):  # PUBLICO
        print(
            f"Marca: {self.marca}, Modelo: {self.modelo}, Estado: {self._estado}")

    @staticmethod
    def calcular_costo_reparacion(horas_trabajadas, tarifa_por_hora):  # PUBLICO
        return horas_trabajadas * tarifa_por_hora

    @classmethod
    def obtener_contador_vehiculos(cls):  # PUBLICO
        print(cls.contador_vehiculo)

    # PROTEGIDO -> sea accedido desde la clase misma o clases hijas
    def _realizar_inspeccion(self):
        print(f"Realizando la inspeccion del vehiculo {self.__id_vehiculo}...")

    # PRIVADO -> solo sea accedido desde la clase misma
    def __registrar_en_sistema(self):
        print(f"Registrando el vehiculo {self.__id_vehiculo} en el sistema...")


autito = Vehiculo("Toyota", "Etios", "Bueno")
auto = Vehiculo("Toyota", "Etios", "Bueno")

# print(autito.marca)                   # ES CORRECTO
# print(autito.modelo)                  # ES CORRECTO
# print(autito._estado)                 # NO ES CORRECTO
# print(autito._Vehiculo__id_vehiculo)  # NO ES NADA CORRECTO
# autito.mostrar_info()

# autito._realizar_inspeccion()

autito._Vehiculo__registrar_en_sistema()  # NO ES NADA CORRECTO