import os
import matplotlib.pyplot as plt
import myro

environment_size=[600,600] ### size in cm

####-----------------Input Data-----------------
imagen=r"Caso_2\Caso2a.jpeg"
n_obstacles=27
slope1=1
slope2=4
rad_hyper=0.1
init_point=[100,100]   ## [x,y] pos
end_point=[400,540]
n_hyper_max=15000
file_slopes=r"Caso_2\pendientes.txt"


### slopes file
with open(file_slopes, "w") as file:
    file.write(str(n_obstacles)+ "\n")
    file.write(str(rad_hyper)+ "\n")
    file.write(str(slope1)+ "\n")
    file.write(str(slope2)+ "\n")
    file.write(str(n_hyper_max)+ "\n")
    file.write(str(init_point[0])+ "\n")
    file.write(str(init_point[1])+ "\n")
    file.write(str(end_point[0])+ "\n")
    file.write(str(end_point[1])+ "\n")

# obstacles data
ruta_obstaculos = r"Caso_2\obstaculos1.txt"

# homotopy tool path
ruta_exe = r"Caso_2\HPPM_v1.exe"

# output data
ruta_datos = r"Caso_2\tray.txt"

# n executions
num_ejecuciones = 1

# Lista para almacenar los datos del archivo de texto
homotopy_path = []

# Lista para almacenar los obstáculos
obstaculos = []

for _ in range(num_ejecuciones):
    os.system(ruta_exe)

    # Leer el archivo de datos generado
    with open(ruta_datos, 'r') as archivo:
        lineas = archivo.readlines()
        
        # Extraer los datos de cada línea y almacenarlos en la lista
        for linea in lineas:
            elementos = linea.strip().split('\t')
            x = float(elementos[0])
            y = float(elementos[1])
            homotopy_path.append((x, y))

    # Leer el archivo de obstáculos
    with open(ruta_obstaculos, 'r') as archivo_obstaculos:
        lineas_obstaculos = archivo_obstaculos.readlines()
        
        # Extraer los datos de cada línea y almacenarlos en la lista de obstáculos
        for linea_obstaculo in lineas_obstaculos:
            elementos_obstaculo = linea_obstaculo.strip().split('\t')
            x_obstaculo = float(elementos_obstaculo[0])
            y_obstaculo = float(elementos_obstaculo[1])
            radio_obstaculo = float(elementos_obstaculo[2])
            obstaculos.append((x_obstaculo, y_obstaculo, radio_obstaculo))

# Graficar los datos y obstáculos
x_vals = [dato[0] for dato in homotopy_path]
y_vals = [dato[1] for dato in homotopy_path]

##plt.scatter(x_vals, y_vals, color='blue', label='homotopy_path')

for obstaculo in obstaculos:
    x_obstaculo, y_obstaculo, radio_obstaculo = obstaculo
    circulo = plt.Circle((x_obstaculo, y_obstaculo), radio_obstaculo, color='red', fill=False)
    plt.gca().add_patch(circulo)

plt.scatter(x_vals, y_vals, color='blue', label='homotopy_path')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Homotopy path')
plt.legend()

fig_image = plt.imread(imagen)
alto_px, ancho_px, _ = fig_image.shape
print("tamano=", alto_px, ancho_px)
rezise=max(600/alto_px, 600/ancho_px)
plt.imshow(fig_image, extent=[0, ancho_px*rezise, 0, alto_px*rezise]) ##, aspect='auto', origin='lower'
plt.show()




fig_image = plt.imread(imagen)
alto_px, ancho_px, _ = fig_image.shape
print("tamano=", alto_px, ancho_px)
plt.imshow(fig_image, extent=[0, ancho_px*rezise, 0, alto_px*rezise]) ##, aspect='auto', origin='lower'
plt.show()


