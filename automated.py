import json

archivo_version = 'VERSION'
archivo_json = 'model_aibom.json'

# Se lee el archivo json
with open(archivo_json, 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)

# Función para leer una línea específica de un archivo (VERSION)
def leer_linea(archivo, numero_linea):
    with open(archivo, 'r') as file:
        for current_line, line in enumerate(file, 1):
            if current_line == numero_linea:
                return line.strip()

linea_a_cambiar = leer_linea(archivo_version, 1)

# Se cambia la version del modelo
datos['model_details']['version'] = linea_a_cambiar

# Se escriben los cambios en el archivo json
with open(archivo_json, 'w', encoding='utf-8') as archivo:
    json.dump(datos, archivo, indent=2)

# Only for testing
print(datos['model_details']['version'])