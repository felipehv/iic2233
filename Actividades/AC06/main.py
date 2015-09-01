class Reporte:
	i=0
	def __init__(self):
		self.pacientes = []
		self.colores = ['amarillo','azul','naranja','rojo','verde']

	def IDgen(self):
		i=0
		while True:
			yield str(i)+'\t'
			i+=1

	def Retornar(self,color):
		retorno = [paciente for paciente in self.pacientes 
		if paciente.split('\t')[4] == color]
		print(retorno)
		return retorno

	def comprobar_cantidad(self):
		for color in self.colores:
			if len(self.Retornar(self.colores)) < 10:
				continue
			else:
				return False
		return True


	def __iter__(self):
		return iter(self.pacientes)

def LineGen(reader):
	while True:
		yield reader.readline()






if __name__ == '__main__':
	with open('Reporte.txt','r') as reader:
		reporte = Reporte()

		lineas = LineGen(reader)

		ids = reporte.IDgen()

		iterador = iter(lineas)

		lineas_revisadas = 0
		while True:
			if reporte.comprobar_cantidad():
				linea = next(lineas)
				print(linea)
				color = linea.split('\t')[3]
				if not len(reporte.Retornar(color)) >= 10 and color in reporte.colores:
					reporte.pacientes.append(next(ids)+linea)
					lineas_revisadas += 1

			else:
				break
	for color in reporte.colores:
		print(reporte.Retornar(color))