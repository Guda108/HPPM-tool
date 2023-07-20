import cv2
import csv
import matplotlib.pyplot as plt
import numpy as np
# Parámetros de umbral y radio mínimo

umbral = 90
radio_minimo = 27
radio_maximo = 80
param=-900.1
rad_robot=30   
imagen = "Caso_2\Caso2a.jpeg"

def enhance_contrast(image):
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar la ecualización de histograma adaptativo
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5, 5))
    equalized = clahe.apply(gray)

    return equalized

def detect_edges(image, umbral):
    # Aplicar umbral adaptativo para obtener una imagen binaria
    _, binary = cv2.threshold(image, umbral, 255, cv2.THRESH_BINARY_INV)

    # Encontrar contornos en la imagen binaria
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Crear una imagen en blanco para mostrar los bordes de los objetos detectados
    edges = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

    # Lista para almacenar los datos de los círculos
    circle_data = []

    # Iterar sobre los contornos encontrados
    for contour in contours:
        # Obtener el centro y el radio del círculo mínimo que encierra el contorno
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)

        # Verificar el radio mínimo
        if (radius >= radio_minimo) and (radius < radio_maximo):
            # Dibujar el círculo en la imagen de salida
            cv2.circle(output, center, radius, (0, 255, 0), 2)
            
            # Dibujar los bordes del objeto en la imagen de bordes
            cv2.drawContours(edges, [contour], 0, (0, 255, 0), 2)
            # Guardar los datos del círculo en la lista
            circle_data.append([x, y, radius+((rad_robot)*scale_factor)])

    return edges, circle_data



# Cargar la imagen
#image = cv2.imread(imagen)
# Cargar la imagen sin invertir el eje Y
image_original = cv2.imread(imagen)
image = cv2.flip(image_original, 0)

# Ajustar el tamaño de la imagen para una visualización adecuada
height, width = image.shape[:2]
print(height, width)
if height > 600 or width > 600:
    scale_factor = max(600 / height, 600 / width)
    image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)
else: 
    scale_factor = max(600 / height, 600 / width)
# Mejorar el contraste de la imagen en color utilizando la corrección gamma
gamma = 1.5  # Ajusta este valor según tus necesidades
gray = enhance_contrast(image)

# Convertir la imagen a escala de grises
##gray = cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2GRAY)

# Aplicar umbral adaptativo para obtener una imagen binaria
_, binary = cv2.threshold(gray, umbral, 255, cv2.THRESH_BINARY_INV)

# Encontrar contornos en la imagen binaria
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Crear una copia de la imagen original para dibujar los círculos
output = image.copy()

# Crear una imagen en blanco para mostrar los bordes de los objetos detectados
edges = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

# Lista para almacenar los datos de los círculos
circle_data = []

# Iterar sobre los contornos encontrados
for contour in contours:
    # Obtener el centro y el radio del círculo mínimo que encierra el contorno
    (x, y), radius = cv2.minEnclosingCircle(contour)
    center = (int(x), int(y))
    radius = int(radius)
    
    # Verificar el radio mínimo
    if (radius >= radio_minimo) and (radius < radio_maximo):
        # Dibujar el círculo en la imagen de salida
        cv2.circle(output, center, radius, (0, 255, 0), 2)
        
        # Dibujar los bordes del objeto en la imagen de bordes
        cv2.drawContours(edges, [contour], 0, (0, 255, 0), 2)
        # Guardar los datos del círculo en la lista
        circle_data.append([x, y, radius+(rad_robot*scale_factor)])

# Mostrar la imagen original con los círculos
cv2.imshow("Detected Objects", output)

# Guardar los datos de los círculos en un archivo CSV
with open('Caso_2\circle_data.txt', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(circle_data)  # Escribir los datos de los círculos

obsta_data=[]
for i in range (len(circle_data)):
    obsta_data.append(circle_data[i].append(param))
print("obsta-list=", obsta_data)

with open("Caso_2\obstaculos1.txt", "w") as file:
    for sublist in circle_data:
        line = "\t".join(str(element) for element in sublist)
        file.write(line + "\n")

# Mostrar la imagen de los bordes de los objetos detectados
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()


