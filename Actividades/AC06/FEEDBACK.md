### Distribución de puntajes

Requerimientos (**R**):

* **(1.00 pts)** R1: Correcta modelación de clases y relaciones
* **(0.75 pts)** R2: Correcto funcionamiento del ID
* **(1.50 pts)** R3: Lectura del archivo hasta línea correcta (con impresión del número de líneas leídas).
* **(0.75 pts)** R4: Es posible iterar correctamente sobre los pacientes de un Reporte
* **(1.00 pts)** R5: Retorar lista de color determinado correctamente
* **(1.00 pts)** R6: Impresión correcta de un paciente

**Además, se descontará (0.2) puntos si no sigue formato de entrega.**

### Obtenido por el alumno
| R1 | R2 | R3 | R4 | R5 | R6 | Descuento |
|:--------|:--------|:--------|:--------|:--------|:--------|:--------|
| 0.4 | 0.5 | 0.75 | 0.75 | 1.0 | 0.0 | 0.2 |

| Nota |
|:-----|
| **4.6** |

### Comentarios
No usaste pep8 :(, 
Tu tarea esta bien casi todo, pero tiene un error garrafal y es que no hiciste la clase paciente. Es necesaria para que funcione bien el programa, en las instancias guardas los valores de los atributos y defines el generador de id. así por ejemplo la funcion Retorna quedaría:
return [paciente for paciente in self.pacientes if paciente.color = “color deseado”]
Que es lo mismo que hiciste tu, pero te entrega instancias de paciente y no strings que no sirven de mucho.
saludos y suerte.