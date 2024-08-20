import random

class mascotaVirtual:
    def __innit__(self,nombre)
        self.nombre=nombre
        self.hambre=0
        self.felicidad=0

    def alimentar(self):
        Nuevo_hambre=self.hambre
        Nuevo_hambre-=random.randint(10,15)
        if Nuevo_hambre <=0:
            self.hambre.set=0
            print("Mascota esta llena, no puede comer mas")    
        else:
            self.hambre.set=Nuevo_hambre
        nueva_felicidad=self.felicidad
        nueva_felicidad-=random.randint(5,10)
        if nueva_felicidad <= 0:
            self.felicidad.set=0
        else:
            self.felicidad.set=nueva_felicidad
    
    def jugar(self):
        nueva_hambre=self.hambre

        if nueva_hambre <=70:
        
            nueva_felicidad=self.felicidad
            nueva_felicidad+=random.randint(10,25)
            print("estoy muy feliz")
            if nueva_felicidad>100:
                nueva_felicidad=100
            nueva_hambre+=random.ranint(10,15)
            if nueva_hambre>100:
                nueva_hambre=100
                print("tengo mucha hambre")
            self.hambre.set=nueva_hambre
        else:
            print("tengo mucha hambre para jugar ahora")
        
    def estado_animo(self):
        estado=self.estado_animo
        hambre=self.hambre
        felicidad=self.felicidad
    #    if 
