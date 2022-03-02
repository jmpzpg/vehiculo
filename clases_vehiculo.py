
class Vehiculo():
    def __init__(self, nom='', vel_max=120, kilom=0) -> None:
        self.__nombre = nom
        self.__velocidad_maxima = vel_max
        self.__kilometraje = kilom
    
    def get_nombre(self):
        return self.__nombre
    def get_velocidad_maxima(self):
        return self.__velocidad_maxima
    def get_kilometraje(self):
        return self.__kilometraje

    def __str__(self) -> str:
        return f'Vehículo: {self.__nombre}, con velocidad máxima de {self.__velocidad_maxima} km/h y Kilometraje de {self.__kilometraje} kilómetros'
    
class Bus(Vehiculo):
    def __init__(self, nom='', vel_max=120, kilom=0, capacidad=50) -> None:
        super().__init__(nom, vel_max, kilom)
        self.__capacidad = capacidad
    
    def get_capacidad(self):
        return self.__capacidad
    def set_capacidad(self, cap=50):
        self.__capacidad = cap

    def __str__(self) -> str:
        return super().__str__() + f', con capacidad para {self.__capacidad} personas'

