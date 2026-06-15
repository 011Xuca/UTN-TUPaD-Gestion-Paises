import csv

# Campos del CSV: definen el orden de columnas para lectura/escritura
campos = ["nombre", "poblacion", "superficie", "continente"]

# Carga los paises desde el archivo CSV y los devuelve como lista de diccionarios
def cargar_paises(nombre_archivo):
    paises = []
    
    try:
        with open(nombre_archivo, "r", encoding = "utf-8") as archivo:
            for fila in csv.DictReader(archivo):
                try:
                    # Convierte y limpia los datos de cada fila
                    paises.append({
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip(),
                    })
                except Exception:
                    # Ignora filas con datos invalidos (ej: poblacion no numerica)
                    print(f"Aviso: fila invalida ignorada: {fila}")
    except FileNotFoundError:
        # Si el archivo no existe, se continua con una lista vacia
        print(f"No se encontro '{nombre_archivo}'. Se inicia con lista vacia.")
        
    return paises

# Guarda la lista de paises en el archivo CSV
def guardar_paises(nombre_archivo, paises):
    try:
        with open(nombre_archivo, "w", encoding = "utf-8", newline = "") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames = campos)
            escritor.writeheader()
            escritor.writerows(paises)
        return True
    
    except Exception as error:
        # Captura cualquier error de escritura (permisos, disco, etc)
        print(f"Error al guardar: {error}")
        return False