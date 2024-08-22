class Inventario:
    def __init__(self):
        self.materiales = {}
    
    def agregar_material(self):
        while True:
            #Pedir al usuario ingresar los datalles del material
            nombre = input('Agregar el nombre del material\r\n').strip()
            grosor = input('Agregar el grosor el material\r\n').strip()
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

            print(f' Material {nombre} {grosor} {color} agregado o actualizado en el inventario.')

            #Preguntar al usuario si quiere agregar otro material 
            otro_material = input('¿Deseas agregar otro material?(s/n):\r\n').strip().lower()
            if otro_material != 's':
                break # Salir del bucle si el usuario no quiere agregar mas 
    
    
                    
        


mi_inventario = Inventario()
mi_inventario.agregar_material()
print(mi_inventario.materiales)