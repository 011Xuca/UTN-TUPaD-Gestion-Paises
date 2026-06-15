# Agrega un nuevo pais a la lista
def agregar_pais(paises, nombre, poblacion, superficie, continente):
    paises.append({
        "nombre": nombre.strip().title(),
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente.strip().title(),
    })

# Busca un pais por nombre y actualiza su poblacion y superficie
def actualizar_pais(paises, nombre, poblacion, superficie):
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            pais["poblacion"] = poblacion
            pais["superficie"] = superficie
            return True
    return False

# Busca paises cuyo nombre contenga el texto ingresado
def buscar_pais(paises, texto):
    texto = texto.lower()
    return [p for p in paises if texto in p["nombre"].lower()]

# --- Filtros ---

# Filtra paises que pertenecen a un continente especifico
def filtrar_por_continente(paises, continente):
    return [p for p in paises if p["continente"].lower() == continente.lower()]

# Filtra paises dentro de un rango de poblacion
def filtrar_por_poblacion(paises, minimo, maximo):
    return [p for p in paises if minimo <= p["poblacion"] <= maximo]

# Filtra paises dentro de un rango de superficie
def filtrar_por_superficie(paises, minimo, maximo):
    return [p for p in paises if minimo <= p["superficie"] <= maximo]

# Ordena los paises por nombre alfabeticamente
def ordenar_por_nombre(paises, descendente=False):
    return sorted(paises, key=lambda p: p["nombre"].lower(), reverse=descendente)

# Ordena los paises por poblacion
def ordenar_por_poblacion(paises, descendente=False):
    return sorted(paises, key=lambda p: p["poblacion"], reverse=descendente)

# Ordena los paises por superficie
def ordenar_por_superficie(paises, descendente=False):
    return sorted(paises, key=lambda p: p["superficie"], reverse=descendente)

# Calcula estadisticas generales sobre la lista de paises
def calcular_estadisticas(paises):
    if not paises:
        return None
    
    poblaciones = [p["poblacion"] for p in paises]
    superficies = [p["superficie"] for p in paises]

    # Cuenta cuantos paises hay por cada continente
    conteo = {}
    for p in paises:
        conteo[p["continente"]] = conteo.get(p["continente"], 0) + 1

    return {
        "mayor_poblacion": max(paises, key=lambda p: p["poblacion"]),
        "menor_poblacion": min(paises, key=lambda p: p["poblacion"]),
        "promedio_poblacion": sum(poblaciones) / len(paises),
        "promedio_superficie": sum(superficies) / len(paises),
        "por_continente": conteo,
    }