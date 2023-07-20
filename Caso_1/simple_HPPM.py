import os
import matplotlib.pyplot as plt

environment_size=[600,600] ### size in cm

####-----------------Input Data-----------------
n_obstacles=3          ###Obstacles in the environment
slope1=1
slope2=4
rad_hyper=0.3          ### hyperspheres radius (step size)
init_point=[0.0,0.0]   ## init point
end_point=[600.0,500.0]    ## goal point
n_hyper_max=1500   ### Max steeps
file_slopes=r"Caso_1\pendientes.txt"


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
ruta_obstaculos = r"Caso_1\obstacles.txt"

# homotopy tool path
ruta_exe = r"Caso_1\HPPM_v1.exe"

# output data
ruta_datos = r"Caso_1\tray.txt"


# Lista para almacenar los datos del archivo de texto
homotopy_path = []

# Lista para almacenar los obstáculos
obstaculos = []

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
plt.show()


