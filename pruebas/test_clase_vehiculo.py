import unittest
from clases_vehiculo import Bus, Vehiculo

class TestClaseVehiculo(unittest.TestCase):
    def test_existencia(self):
        v = Vehiculo()
        self.assertIsNotNone(v)

    def test_existencia_con_atributos(self):
        v = Vehiculo('moto', 100, 0)
        self.assertEqual(v.get_nombre(), 'moto')
        self.assertEqual(v.get_velocidad_maxima(), 100)
        self.assertEqual(v.get_kilometraje(), 0)
    
class TestClaseBus(unittest.TestCase):    
    def test_existencia_bus_con_atributos(self):
        b = Bus('escolar', 80, 40000)
        self.assertEqual(b.get_nombre(), 'escolar')
        self.assertEqual(b.get_velocidad_maxima(), 80)
        self.assertEqual(b.get_kilometraje(), 40000)