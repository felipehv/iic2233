### Distribución de puntajes

Requerimientos (**R**):

* **(4.0 pts)** R1: Metaclase `ReadOnly`. 2.0 pts por el coportamiento del `__init__` y 2.0 pts por restringir el acceso a los atributos.
* **(2.0 pts)** R2: Metaclase `Singleton`.

**Además, se descontará (0.2) puntos si no sigue formato de entrega.**

### Obtenido por el alumno
| R1 | R2 | Descuento |
|:---|:---|:----------|
| 2.0 | 2.0 | 0.2 |

| Nota |
|:-----|
| **4.8** |

### Comentarios

* Recuerda respetar PEP 8 (-0.2): debe haber dos líneas en blanco entre las funciones y clases; debe haber un espacio ante y después de una función dentro de las clases; debe haber un espacio después de **,**.
* No era necesario el ``__new__`` en el singleton.
* En R1 faltó agregar las restricciones. Para lograr ellos podías utilizar properties. 
* No era necesario agregar un ``__call__`` en ``RestrictedAccess``.