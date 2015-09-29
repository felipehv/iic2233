import unittest
from main import *
def Verificador(rut):
	rut = rut[::-1]
	suma = 0
	numeros = [2,3,4,5,6,7]
	for i in range(len(rut)):
		suma += int(rut[i]) * numeros[i%6]

	resto = suma%11
	if num == 10:
		return 'k'
	elif numm == 11:
		return "0"
	return str(11-resto)


class AC13(unittest.TestCase):
	
	def setUp(self):
		self.archivos = []
		for n in listdir('Trabajos'):
			self.archivos.append(Corrector(n))

	def test_revisar_nombre(self):
		"""
		self.assertTrue(self.archivos[0].revisar_nombre())
		self.assertTrue(self.archivos[1].revisar_nombre())
		self.assertTrue(self.archivos[2].revisar_nombre())
		self.assertFalse(self.archivos[3].revisar_nombre())
"""
	def test_revisarFormato(self):
		"""
		self.assertTrue(self.archivos[0].revisar_formato(self.archivos[0].nombre.split('.')[1]))
		self.assertTrue(self.archivos[1].revisar_formato(self.archivos[1].nombre.split('.')[1]))
		self.assertTrue(self.archivos[2].revisar_formato(self.archivos[2].nombre.split('.')[1]))
		self.assertFalse(self.archivos[3].revisar_formato(self.archivos[3].nombre.split('.')[1]))
"""
	def test_revisarVerificador(self):
		rut=[i.nombre.split('_')[1] for i in self.archivos]
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

	def test_getDescuento(self):
		pass

	def tearDown(self):
		pass





if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(AC13)
	unittest.TextTestRunner().run(suite)