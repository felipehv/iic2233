# -*- coding: utf8 -*-
from zlib import compress, decompress, crc32


class InstaPUC:

    @staticmethod
    def getData(filename):
        signature = None
        ihdr = {}
        idat = bytearray()
        iend = None
        with open(filename,'rb') as photo:
            foto = bytearray(photo.read())
            header = foto[0:8]
            foto = foto[8:]
        while True:
            largo = int.from_bytes(foto[0:4],byteorder="big")
            tipo_info = foto[4:8].decode("ascii")
            info = foto[8:8+int(largo)]
            if tipo_info == "IEND":
                iend = foto[0:8+largo]
                break
            elif tipo_info == "IHDR":
                ihdr["ancho"] = int.from_bytes(info[0:4],byteorder="big")
                ihdr["largo"] = int.from_bytes(info[4:8],byteorder="big")
                ihdr["color"] = int.from_bytes(info[9:10],byteorder="big")
            elif tipo_info == "IDAT":
                idat += info
            foto = foto[8+int(largo)+4:]
        ########################################
        #                                      #
        # Completar método.                    #
        # Extraer la metadata de la imagen PNG.#
        #                                      #
        ########################################
        return signature, ihdr, decompress(idat), iend

    @staticmethod
    def bytes2matrix(ihdr, idat):
        matriz=[]
        for i in range(ihdr['largo']):
            fila = []
            for j in range(ihdr['ancho']):
                fila.append('')
            matriz.append(fila)
            fila = []

        for j in range(ihdr["ancho"]):
            for i in range(ihdr["largo"]):

                matriz[i][j] = idat[i][j+1]
        ########################################
        #                                      #
        # Completar método.                    #
        # Transformar arreglo de bytes a una   #
        # matriz de pixeles.                   #
        #                                      #
        ########################################
        return matriz

    @staticmethod
    def matrix2string(matriz):
        """
        Este método transforma la matriz en un string de bytes.
        """
        out = b''
        for i in range(len(matriz)):
            out += (0).to_bytes(1, byteorder='big')
            for j in range(1, len(matriz[i])):
                for k in matriz[i][j]:
                    out += k.to_bytes(1, byteorder='big')
        return out

    @staticmethod
    def rotate(ihdr, matriz):
        salida = []
        for i in range(len(x[0])):
            salida.append([])
        for i in range(len(x)):
            for j in range(len(x[0])):
                salida[j].append(x[len(x)-1-i][j])

        return ihdr, salida

    @staticmethod
    def grey(ihdr, matriz):
        ihdr_nuevo = ihdr
        ihdr_nuevo['color'] = 0
        def promedio(tupla):
            return (tupla[0]+tupla[1]+tupla[2])/3
        salida = []
        for i in range(len(matriz)):
            salida.append([])
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                h = promedio(matriz[i][j])
                salida[i].append((h,h,h))
        ########################################
        #                                      #
        # Completar método.                    #
        # Cambiar cada pixel por el promedio   #
        # de las 3 componentes y modificar la  #
        # metadata.                            #
        #                                      #
        ########################################
        return ihdr_nuevo, salida

    @staticmethod
    def writeImage(outFile, signature, ihdr, idat, iend):
        idat = compress(idat, 9)
        ########################################
        #                                      #
        # Completar método.                    #
        # Escribe un nuevo archivo PNG con la  #
        # información entregada.               #
        # TIP: No es necesario hacer varios    #
        # chunks de IDAT.                      #
        #                                      #
        ########################################
        print("Tu imagen ha sido transformada exitosamente!")


if __name__ == '__main__':

    imagefile = 'MickeyMouse.png'  # Mushroom.png o MickeyMouse.png

    firma, ihdr, data, end = InstaPUC.getData(imagefile)

    matriz = InstaPUC.bytes2matrix(ihdr, data)
    """
    ihdr_gris, matriz_gris = InstaPUC.grey(ihdr, matriz)

    idat_gris = InstaPUC.matrix2string(matriz_gris)

    InstaPUC.writeImage(
        'image.png',
        firma,
        ihdr_gris,
        idat_gris,
        end)
    """
    """
    # Descomentar si se realiza el bonus

    ihdr_gris_rotado, matriz_gris_rotada = InstaPUC.rotate(
        ihdr_gris, matriz_gris)

    idat_gris_rotado = InstaPUC.matrix2string(matriz_gris_rotada)

    InstaPUC.writeImage(
        'image.png',
        firma,
        ihdr_gris_rotado,
        idat_gris_rotado,
        end)
    """
