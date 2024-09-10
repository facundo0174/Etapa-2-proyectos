
class Inventario:
    def __init__(self):
        self.materiales = {
                'Madera': {
        '10mm': {
            'Rojo': {'num_laminas': 5, 'num_cuadrantes': 3},
            'Azul': {'num_laminas': 2, 'num_cuadrantes': 1}
        },
        '20mm': {
            'Verde': {'num_laminas': 6, 'num_cuadrantes': 4}
        }
    },
    'Metal': {
        '5mm': {
            'Plata': {'num_laminas': 8, 'num_cuadrantes': 2},
            'Oro': {'num_laminas': 1, 'num_cuadrantes': 1}
        }
    },
    'Plástico': {
        '2mm': {
            'Blanco': {'num_laminas': 10, 'num_cuadrantes': 5},
            'Negro': {'num_laminas': 7, 'num_cuadrantes': 3}
        }
    },
    'Vidrio': {
        '3mm': {
            'Transparente': {'num_laminas': 4, 'num_cuadrantes': 2}
        }
    }
        }
    #AGREGAR MATERIAL AL INVENTARIO 
    def agregar_principal(self):
        while True:
            #Pedir al usuario ingresar los datalles del material
            nombre = input('Agregar el nombre del material\r\n').strip()
            while not nombre:  #Verifica si se ingreso datos o esta vacio  
                print('Error: El Nombre no puede estar vacio.')
                nombre = input('Agregar el nombre del material\r\n').strip()
            grosor = input('Agregar el grosor el material\r\n').strip()
            while not grosor:
                print('Error: El Grosor no pude estar vacio.')
                grosor = input('Agregar el grosor el material\r\n').strip()
            color = input('Agregar el color del material\r\n').strip()    
            while not color:
                print('Error: El Color no puede estar vacio.')
                color = input('Agregar el color del material\r\n').strip()

            #Validación de entrada 
            try:
                num_laminas = int(input('Agregar el número de láminas\r\n').strip())
                num_cuadrantes = int(input('Agregar el número de cuadrantes\r\n').strip())
                if num_laminas < 0 or num_cuadrantes < 0:
                    raise ValueError('El número de láminas y cuadrantes debe ser positivo.')
            except ValueError as e:
                print(f'Error: {e}')
                continue # Reinicio del ciclo en caso de Error 
            #Confirmacion de datos ingresados
            if self.confirmacion_datos(nombre, grosor, color, num_laminas, num_cuadrantes):
                #Guardando en el Inventario
                self.agregar_material_dicc( nombre, grosor, color, num_laminas, num_cuadrantes) 
            #Preguntar al usuario si desea continuar guardando Materiales
            while True:
                confirmacion = input(f'Desea agregar otro Material?(s/n)\r\n').strip().lower()
                if confirmacion == 's': 
                    break
                elif confirmacion == 'n':
                    return
                else:
                    print('Debe ingresar "s" para si o "n" para no.') 
    #Confirmacion de datos ingresados
    def confirmacion_datos(self, nombre, grosor, color, num_laminas,num_cuadrantes):
        #Confirmar si los datos ingresados son correctos 
        while True:
            confirmacion = input(
                f'Confirmar si los datos ingresados del Material son correctos: Nombre:{nombre} con un Grosor:{grosor} y un Color:{color},'
                f'Láminas:{num_laminas}, Cuadrantes:{num_cuadrantes}(s/n).\r\n'
                f'Si ya no desea ingresar el Material, ingrese "x" para salir.\r\n'
            ).strip().lower()
            if confirmacion == 's': 
                return True # Confirmación
            elif confirmacion == 'n':
                print('No se agrego el Material al Inventario.')
                return False # No se guarda el Material
            elif confirmacion == 'x':
                print('Saliendo..')
                return 
            else:
                print('Debe ingresar "s" para si o "n" para no.') 
    #Material guardado en el Inventario
    def agregar_material_dicc(self, nombre, grosor, color, num_laminas, num_cuadrantes):
        #Verificar si el nombre ya existe para ese material
        if nombre not in self.materiales:
            self.materiales[nombre] = {}
        #Verificar si el grosor ya existe para ese material
        if grosor not in self.materiales[nombre]:
            self.materiales[nombre][grosor] = {}
        #Verificar si el color ya existe para ese material  
        if color not in self.materiales[nombre][grosor]:
            self.materiales[nombre][grosor][color] = {'num_laminas':num_laminas, 'num_cuadrantes':num_cuadrantes}
        else:
            # Si ya existe, sumamos las laminas y cuadrantes 
            self.materiales[nombre][grosor][color]['num_laminas'] += num_laminas
            self.materiales[nombre][grosor][color]['num_cuadrantes'] += num_cuadrantes
        
        print(f'El Material:{nombre} con un Grosor:{grosor} y un Color:{color} se agrego al Inventario.')


    #ELIMINAR EL MATERIAL DEL INVENTARIO 
    def eliminar_materiales(self):
        while True:
            print('\nOpciones:')
            print('1. Eliminar un Material por el Nombre, Grosor y Color')
            print('2. Eliminar un Material por el Nombre y el Grosor')
            print('3. Eliminar un Material por el Nombre y el Color')
            print('4. Salir')
            try:
                opcion = int(input('Seleccionar una Opción (1-4):\r\n').strip())
            except ValueError:
                print('Opción no válida. Por favor, elija una opción entre el 1 y 4.')
                continue #Omite el resto del código y vuelve al inicio del bucle
            if opcion == 1:
                datos = self.recoger_datos_elim_completo()#Usa los valores almacenados en la tupla
                if datos:
                    nombre,grosor,color = datos
                    self.eliminar_material(nombre, grosor, color)
            elif opcion == 2:
                nombre,grosor = self.recoger_datos_elim_grosor()
                self.eliminar_nombre_grosor(nombre, grosor) 
            elif opcion == 3:
                nombre,color = self.recoger_datos_elim_color()
                self.eliminar_nombre_color(nombre,color)
            elif opcion == 4:
                print('Saliendo...')
                break
            else:
                print('Opción no válida. Por favor, elija una opción entre el 1 y 4.')
    #Confirmacion de datos ingresados para Eliminar el Material
    def confir_datos_eliminacion(self):
        while True:
            pregunta ='Los datos del Material ingresados son correctos?(s/n)\r\n'
            pregunta += 'Volver al menu de eliminacion de Materiales(x).\r\n'
            confirmar = input(pregunta).strip().lower()
            if confirmar == 's':
                return True
            elif confirmar == 'n':
                return False
            elif confirmar == 'x':
                return 'menu'
            else:
                print('Error: Tiene que ingresar (s/n) o si quiere volver al Menu de Eliminar Materiales(x).')

    #Recoger datos del Usuario para eliminar el Material
    def recoger_datos_elim_completo(self):
        while True:
            elim_nombre = input('Ingresar el Nombre del Material a Eliminar:\r\n')
            while not elim_nombre:
                print('Error: El Nombre no puede estar vacio.')
                elim_nombre = input('Ingresar el Nombre del Material a Eliminar:\r\n')
            elim_grosor = input('Ingresar el Grosor del Material a Eliminar:\r\n')
            while not elim_grosor:
                print('Error: El Grosor no puede estar vacio.')
                elim_grosor = input('Ingresar el Grosor del Material a Eliminar:\r\n')
            elim_color = input('Ingresar el Color del Material a Eliminar:\r\n')
            while not elim_color:
                print('Error: El Color no puede estar vacio.')
                elim_color = input('Ingresar el Color del Material a Eliminar:\r\n')
            confirmacion = self.confir_datos_eliminacion()
            if confirmacion:
                return elim_nombre,elim_grosor,elim_color # return devuelve los valores almacenados como una tupla
            elif confirmacion == 'menu':
                return None
    #Ingresar datos de Eliminacion del Material por Nombre y Grosor
    def recoger_datos_elim_grosor(self):
        elim_nombre = input('Ingresar el Nombre del Material a Eliminar:\r\n')
        while not elim_nombre:
            print('Error: El Nombre no puede estar vacio.')
            elim_nombre = input('Ingresar el Nombre del Material a Eliminar:\r\n')
        elim_grosor = input('Ingresar el Grosor del Material a Eliminar:\r\n')
        while not elim_grosor:
            print('Error: El Grosor no puede estar vacio.')
            elim_grosor = input('Ingresar el Grosor del Material a Eliminar:\r\n')
        return elim_nombre,elim_grosor # return devuelve los valores almacenados como una tupla
    #Ingresar datos de Eliminacion del Material por Nombre y Color
    def recoger_datos_elim_color(self):
        elim_nombre = input('Ingresar el Nombre del Material a Eliminar:\r\n')
        while not elim_nombre:
            print('Error: El Nombre no puede estar vacio.')
            elim_nombre = input('Ingresar el Nombre del Material a Eliminar:\r\n')
        elim_color = input('Ingresar el Color del material a Eliminar:\r\n')
        while not elim_color:
            print('Error: El Color no puede estar vacio.')
            elim_color = input('Ingresar el Color del material a Eliminar:\r\n')
        return elim_nombre, elim_color
    #Eliminar el Material por (Nombre, Grosor y Color)    
    def eliminar_material(self,nombre, grosor, color):
        if nombre in self.materiales:
            if grosor in self.materiales[nombre]:
                if color in self.materiales[nombre][grosor]:
                    del self.materiales[nombre][grosor][color]
                    print(f'El Material:{nombre} con un Grosor:{grosor} y un Color:{color} se elimino del Inventario')
                    #Verisicar si grosor esta Vacio
                    if not self.materiales[nombre][grosor]:
                        del self.materiales[nombre][grosor]
                        print(f'El Material: {nombre} con un Grosor:{grosor} se elimino del Inventario por falta de unidades')
                    if not self.materiales[nombre]:
                        del self.materiales[nombre]
                        print(f'El Material:{nombre} se elimino del Inventario por falta de unidades')
                else:
                    print(f'El Material:{nombre} con un Grosor:{grosor} no existe en el Inventario con ese Color({color})')
            else:
                print(f'El Material:{nombre} no existe en el Inventario con ese Grosor:{grosor}')
        else:
            print(f'El Material:{nombre} no existe en el inventario')
    #Elminar el Material por (Nombre y Grosor)
    def eliminar_nombre_grosor(self,nombre,grosor):
        if nombre in self.materiales:
            if grosor in self.materiales[nombre]:
                del self.materiales[nombre][grosor]
                print(f'El Material:{nombre} de Grosor:{grosor} se elimino del Inventario.')
                #Verificacion de Nombres si no tiene grosores 
                if not self.materiales[nombre]:
                    del self.materiales[nombre]
                    print(f'El Material:{nombre} se elimino del Inventario por falta de unidades')
            else:
                print(f'El Material:{nombre} con un Grosor:{grosor} no existe en el Inventario')
        else:
            print(f'El Material:{nombre} no existe en el inventario')
    #Eliminar el Material  por el (Nombre y Color)
    def eliminar_nombre_color(self,nombre,color):
        if nombre in self.materiales: #Busca en el diccionario el material 
            for grosor in list(self.materiales[nombre].keys()): # Convierte las claves en una lista y a su vez es un seguro para evitar errores o dañar al diccionario mientras iteras
                #Elimina el material del color especifico
                if color in self.materiales[nombre][grosor]:
                    del self.materiales[nombre][grosor][color]
                    print(f'El Material:{nombre} de color:{color} se elimino del Inventario')
                    #Verifica si el grosor ya no tiene mas colores 
                    if not self.materiales[nombre][grosor]:
                        #Si en el caso de que no hay mas colores en ese grosor y esta vacio el diccionario, elimina el grosor 
                        del self.materiales[nombre][grosor]
                        print(f'El Material:{nombre} de Grosor:{grosor} se elimino por falta de unidades')
                        #verifica si el material ya no tienen un grosor y esta vacio, elemina el material 
                    if not self.materiales[nombre]:
                        #Si no tiene un grosor en ese material se eliminara el material porque no hay unidades
                        del self.materiales[nombre]
                        print(f'El Material:{nombre} fue eliminado por falta de unidades')
                    break
                else:
                    print(f'El Material:{nombre} del Color:{color}, no existe en el Inventario ')
        else:
            print(f'El Material:{nombre} no existe en el Inventario')


mi_inventario = Inventario()
print(mi_inventario.materiales)
mi_inventario.eliminar_materiales()
print(mi_inventario.materiales)
