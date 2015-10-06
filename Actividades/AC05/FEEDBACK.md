### Distribución de puntajes

Requerimientos (**R**):

* **(1.50 pts)** R1: Clase `Commit` y `Branch` correctas.
* **(1.50 pts)** R2: Método `pull` correcto.
* **(1.00 pts)** R3: Método `create_branch` correcto.
* **(2.0 pts)** R4: Método `checkout`.

**Además, se descontará (0.2) puntos si no sigue formato de entrega.**

### Obtenido por el alumno
| R1 | R2 | R3 | R4 | Descuento |
|:---|:---|:---|:---|:----------|
| 1.3  | 1.5  | 0.5  | 1.8  | 0         |

| Nota |
|:-----|
| **6.1** |

### Comentarios

* En ``Commit`` olvidaste agregar una **id** para cada instancia, solo creaste el de la clase (-0.2)
* ``create_branch`` la branch creada debería ser hija de la entregada por el otro argumento.
* ``checkout`` hay un error (-0.2):
```python
    def checkout(ide):
        files = set()
        for branch in self.hijos:
            for commit in branch.commits:
                if commit.ide <= ide:
                    for xfile in branch.files:
                        files.add(xfile)

            files.union(branch.checkout)  # ???
        return files
```
