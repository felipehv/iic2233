import unittest
from main import *
def Verificador(rut):
	verificador = rut[-1]
	rut = rut[0:-2]
	rut = rut[::-1]
	suma = 0
	numeros = [2,3,4,5,6,7]
	for i in range(len(rut)):
		suma += int(rut[i]) * numeros[i%6]

	resto = suma%11
	if 11-resto == 10:
		num = 'k'
	elif 11-resto == 11:
		num= "0"
	num= str(11-resto)
	return num == verificador

class AC13(unittest.TestCase):
	
	def setUp(self):
		self.archivos = []
		for n in listdir('Trabajos'):
			self.archivos.append(Corrector(n))

	def test_revisar_nombre(self):
		self.assertTrue(self.archivos[0].revisar_nombre())
		self.assertTrue(self.archivos[1].revisar_nombre())
		self.assertTrue(self.archivos[2].revisar_nombre())
		self.assertFalse(self.archivos[3].revisar_nombre())

	def test_revisarFormato(self):
		self.assertTrue(self.archivos[0].revisar_formato(self.archivos[0].nombre.split('.')[1]))
		self.assertTrue(self.archivos[1].revisar_formato(self.archivos[1].nombre.split('.')[1]))
		self.assertTrue(self.archivos[2].revisar_formato(self.archivos[2].nombre.split('.')[1]))
		self.assertFalse(self.archivos[3].revisar_formato(self.archivos[3].nombre.split('.')[1]))

	def test_revisarVerificador(self):
		rut=[i.nombre.split('_')[0] for i in self.archivos]
		self.assertEqual(self.archivos[0].revisar_verificador(rut[0]),Verificador(rut[0]))
		self.assertEqual(self.archivos[1].revisar_verificador(rut[1]),Verificador(rut[1]))
		self.assertEqual(self.archivos[2].revisar_verificador(rut[2]),Verificador(rut[2]))
		self.assertEqual(self.archivos[3].revisar_verificador(rut[3]),Verificador(rut[3]))

	def test_revisarOrden(self):
		pass

	def test_descontar(self):
		pass

	def test_getPalabras(self):
		pass

	def test_get_descuento(self):
	    for i in range(len(self.archivos)):
	        self.assertIsInstance(self.archivos[i].get_descuento, int)
	        if self.archivos[i].revisar_nombre() and self.archivos[i].palabras < 500:
	            self.assertEqual(self.archivos[i].get_descuento, 1.5)

	def tearDown(self):
		pass





if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(AC13)
	unittest.TextTestRunner().run(suite)