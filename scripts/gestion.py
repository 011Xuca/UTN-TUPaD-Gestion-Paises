def agregar_pais(paises, nombre, poblacion, superficie, continente):
    paises.append({
        "nombre": nombre.strip(),
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente.strip(),
    })

def actualizar_pais(paises, nombre, poblacion, superficie):
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            pais["poblacion"] = poblacion
            pais["superficie"] = superficie
            return True
    return False

def buscar_pais(paises, texto):
    texto = texto.lower()
    return [p for p in paises if texto in p["nombre"].lower()]

# --- Filtros ---
def filtrar_por_continente(paises, continente):
    return [p for p in paises if p["continente"].lower() == continente.lower()]

def filtrar_por_poblacion(paises, minimo, maximo):
    return [p for p in paises if minimo <= p["poblacion"] <= maximo]

def filtrar_por_superficie(paises, minimo, maximo):
    return [p for p in paises if minimo <= p["superficie"] <= maximo]

def ordenar_por_nombre(paises, descendente=False):
    return sorted(paises, key=lambda p: p["nombre"].lower(), reverse=descendente)

def ordenar_por_poblacion(paises, descendente=False):
    return sorted(paises, key=lambda p: p["poblacion"], reverse=descendente)

def ordenar_por_superficie(paises, descendente=False):
    return sorted(paises, key=lambda p: p["superficie"], reverse=descendente)

def calcular_estadisticas(paises):
    if not paises:
        return None
    
    poblaciones = [p["poblacion"] for p in paises]
    superficies = [p["superficie"] for p in paises]

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