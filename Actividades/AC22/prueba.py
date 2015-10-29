with open("MickeyMouse.png",'rb') as photo:
    foto = bytearray(photo.read())
    header = foto[0:8]
    foto = foto[8:]
    while len(foto) > 0:
        largo = int.from_bytes(foto[0:4],byteorder="big")
        tipo_info = foto[4:8]
        info = foto[8:8+int(largo)]
        foto = foto[8+largo:]
        if info is "IHDR":
            


