
mapsize=[1.89,1.89,600.0,600.0]   ### 2x2 metros y 600x600 pixeles

def leer_datos(n_datos, mapsize):
    # Ruta del archivo de texto
    archivo = r"Caso_3\tray.txt"

    # Lista para almacenar todos los datos
    datos_completos = []

    # Lista para almacenar 1 de cada n datos
    datos_cada_n = []

    with open(archivo, "r") as file:
        # Leer el contenido del archivo línea por línea
        lineas = file.readlines()

        for linea in lineas:
            # Eliminar espacios en blanco y dividir los valores x, y
            valores = linea.strip().split("\t")
            x = float(valores[0])
            y = float(valores[1])

            # Agregar los datos completos a la lista
            datos_completos.append((x, y))

            # Agregar 1 de cada n datos a la lista
            if len(datos_completos) % n_datos == 0:
                datos_cada_n.append((x, y))

    # Guardar los datos seleccionados en un archivo de texto (Trayectoria para S2 parallax)
    with open(r"Caso_3\trays2.txt", "w") as file:
        factorx=(mapsize[0]/mapsize[2])*(2000)  ### 2000 steps of the robot S2 per meter
        factory=(mapsize[1]/mapsize[3])*(2000)
        for dato in datos_cada_n[0:len(datos_cada_n)]:
            linea = "{}\t{}\n".format(int(factorx*(dato[0]-datos_completos[0][0])), int(factory*(dato[1]-datos_completos[0][1])))
            file.write(linea)
    return datos_completos, datos_cada_n

# Ejemplo de uso
n_datos=100
datos_completos, datos_cada_n = leer_datos(n_datos,mapsize)

