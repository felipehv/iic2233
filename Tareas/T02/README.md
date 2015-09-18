# Tarea 2

** Classes.py **
*En la libreria classes se puede encontrar la clase Puerto, que junta
todas las caracteristicas de un nodo dentro de la red.
*Casi todos los atributos son evidentes, pero explico algunos:
*self.n : es la cantidad de iteraciones que lleva un puerto en cierta
salida. Al llegar a 5 (porque asi lo defini), cambia a otra conexion.
*self.complete: Indica si el puerto ya recorrio 5 veces cada puerto, 
para dejar de agregar puertos a las listas de salida.
*self.lastconnection: indica la ultima conexion efectiva de un puerto.
*self.listas2: tiene lista de tamaño = cantidad_conexiones de un puerto.
para poder agregar los puertos en cada conexion.
*ActualizarLista(): actualiza la listas2 al obtener la cantidad de 
conexiones.
*Connect(): recibe como parametro func, que es la funcion conectar.
Realiza las comprobaciones necesarias para poder recorrer 5 veces cada
puerto en orden. Una vez que llega a self.complete = True, pasa por un
puerto a la vez.

**Estructuras.py**
*Es exactamente una lista, pero menos eficiente
*class myList(): clase de lista con metodos para poder recorrer, imprimir,
obtener y agregar elementos, comparar e iterar.
*class listObject(): nodo de la lista.

**Ciclos.py**
*Contiene funciones para calcular los ciclos de bummer.

**Main.py**
*En la primera parte, se recorre conectandose a todos los puertos de banner,
hasta encontrar todos los puertos de la red. La variable maximus, indica el
maximo valor de nodo que se ha encontrado.
*Si un puerto no esta en la lista_de_puertos, entonces se le agrega como 
instancia de puerto, con todas sus caracteristicas y se suma 1 a los 
puertos encontrados para llevar la cuenta.
*Se guarda el puerto anterior en puertoanterior para poder hacer 
comparaciones con el puerto actual y verificar si se tiene que agregar a la
lista de salidas o entradas.
**A veces se cae por exceso de recursion dependiendo del tamaño y la
configuracion de la red.

*La ruta a bummer parte desde el nodo 0 e itera a traves de las salidas del
primer nodo, para buscar un camino hasta banner. Si se encuentra con un nodo
que no es banner, busca nuevamente en las iteraciones hasta encontrarse con
banner. Si en algun momento se llega a un nodo sin salida a banner, el
recorrido ya no sirve.

**Siendo las 6 de la mañana del 18 de septiembre, me voy a dormir, piedad=(**





| Nº Alumno    | Nombre              | Email UC      |
|:-------------|:--------------------|:--------------|
| 14632640     | Felipe Haase        | fahaase@uc.cl |
