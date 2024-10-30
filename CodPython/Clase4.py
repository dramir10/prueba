class Automovil:

    def __init__(self, marca_a, modelo, velocidad_max):
        self.__marca = marca_a
        self.__modelo = modelo
        self.__velocidad = 0
        self.__velocidad_maxima = velocidad_max
        self.__color = "Blanco"

    def set_color(self, color_nuevo):
        self.__color = color_nuevo
    
    def get_color(self):
        return self.__color
    
    def acelerar(self, kms):
        velocidad_aux = self.__velocidad + kms
        if velocidad_aux <= self.__velocidad_maxima:
            self.__velocidad = velocidad_aux
        else:
            self.__velocidad = self.__velocidad_maxima
    
    def get_velocidad(self):
        return self.__velocidad

fordka = Automovil("Ford", "Ka", 170)
print(fordka.get_velocidad())
print(fordka.get_color())

fordka.set_color("Rojo")
print(fordka.get_color())

fordka.acelerar(20)            #   <-----Acelerando
print(fordka.get_velocidad())
fordka.acelerar(60)
print(fordka.get_velocidad())
fordka.acelerar(30)
print(fordka.get_velocidad())
fordka.acelerar(50)
print(fordka.get_velocidad())
fordka.acelerar(-20)           #   <-----Frenando
print(fordka.get_velocidad())



class Perro:
    def __init__(self, nombre, raza, edad):
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad

    def ladrar(self):
        print(f"{self.__nombre} está ladrando!")

    def jugar(self):
        print(f"{self.__nombre} quiere jugar!")

    def comer(self):
        print(f"{self.__nombre} está comiendo!")
        
        
    def get_nombre(self):
        return self.__nombre

    def get_raza(self):
        return self.__raza

    def get_edad(self):
        return self.__edad



mi_perro = Perro("Bubby", "Husky", 2)
mi_perro.ladrar()
mi_perro.jugar()
mi_perro.comer()
