import csv

campos = ["nombre", "poblacion", "superficie", "continente"]

def cargar_paises(nombre_archivo):
    paises = []
    
    try:
        with open(nombre_archivo, "r", encoding = "utf-8") as archivo:
            for fila in csv.DictReader(archivo):
                try:
                    paises.append({
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip(),
                    })
                except Exception:
                    print(f"Aviso: fila invalida ignorada: {fila}")
    except FileNotFoundError:
        print(f"No se encontro '{nombre_archivo}'. Se inicia con lista vacia.")
        
    return paises

def guardar_paises(nombre_archivo, paises):
    try:
        with open(nombre_archivo, "w", encoding = "utf-8", newline = "") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames = campos)
            escritor.writeheader()
            escritor.writerows(paises)
        return True
    
    except Exception as error:
        print(f"Error al guardar: {error}")
        return False
