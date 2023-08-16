import csv
import os
import datetime

# Lee el archivo profesores_asignaturas.txt para obtener la información de profesores y asignaturas
profesores_asignaturas = []
with open('profesores_asignaturas.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        profesor, materia = line.strip().split(',')
        profesores_asignaturas.append((profesor, materia))

# Lee la duración de cada clase, hora de inicio y hora de fin desde preCons.txt
with open('preCons.txt', 'r') as config_file:
    duracion_clase = int(config_file.readline().strip())
    hora_inicio = config_file.readline().strip()
    hora_fin = config_file.readline().strip()

# Crea una carpeta llamada "preExpanded"
os.makedirs('preExpanded', exist_ok=True)

# Genera un archivo CSV para cada profesor en el horario
for profesor, materia in profesores_asignaturas:
    archivo_profesor = os.path.join('preExpanded', f'{profesor}.csv')
    with open(archivo_profesor, 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        
        # Escribe las filas de encabezados
        writer.writerow(['hora_inicio', 'hora_fin', 'materia', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes'])
        
        # Genera las filas del horario con valores iniciales de 0
        hora_actual = hora_inicio
        while hora_actual < hora_fin:
            hora_fin_actual = (datetime.datetime.strptime(hora_actual, '%H:%M') + datetime.timedelta(minutes=duracion_clase)).strftime('%H:%M')
            writer.writerow([hora_actual, hora_fin_actual, materia, 0, 0, 0, 0, 0])
            hora_actual = hora_fin_actual

print("Archivos generados en la carpeta preExpanded.")
