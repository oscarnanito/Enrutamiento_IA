# -*- coding: utf-8 -*-
import heapq

# Base de conocimiento
grafo = {
    "Portal del Norte": {"Toberín": 3550},
    "Toberín": {
        "Portal del Norte": 3550,
        "Calle 146": 3550
    },
    "Calle 146": {
        "Toberín": 3550,
        "Calle 142": 3550
    },
    "Calle 142": {
        "Calle 146": 3550,
        "Prado": 3550
    },
    "Prado": {
        "Calle 142": 3550,
        "Calle 100": 3550
    },
    "Calle 100": {
        "Prado": 3550,
        "Héroes": 3550
    },
    "Héroes": {
        "Calle 100": 3550,
        "Calle 76": 3550
    },
    "Calle 76": {
        "Héroes": 3550,
        "Calle 57": 3550
    },
    "Calle 57": {
        "Calle 76": 3550,
        "Marly": 3550
    },
    "Marly": {
        "Calle 57": 3550,
        "Avenida Jiménez": 3550
    },
    "Avenida Jiménez": {
        "Marly": 3550,
        "Hortúa": 3550
    },
    "Hortúa": {
        "Avenida Jiménez": 3550,
        "Nariño": 3550
    },
    "Nariño": {
        "Hortúa": 3550,
        "Fucha": 3550
    },
    "Fucha": {
        "Nariño": 3550,
        "Santa Lucía": 3550
    },
    "Santa Lucía": {
        "Fucha": 3550,
        "Socorro": 3550
    },
    "Socorro": {
        "Santa Lucía": 3550,
        "Consuelo": 3550
    },
    "Consuelo": {
        "Socorro": 3550,
        "Molinos": 3550
    },
    "Molinos": {
        "Consuelo": 3550,
        "Danubio": 3550
    },
    "Danubio": {
        "Molinos": 3550,
        "Portal Usme": 3550
    },
    "Portal usme": {"Danubio": 3550}
}

# Heurística hasta portal usme
heuristica_hasta_portal_usme = {
    "Portal del Norte": 19,
    "Toberín": 18,
    "Calle 146": 17,
    "Calle 142 ": 16,
    "Prado": 15,
    "Calle 100 ": 14,
    "Héroes ": 13,
    "Calle 76 ": 12,
    "Calle 57": 11,
    "Marly": 10,
    "Avenida Jiménez": 9,
    "Hortúa": 8,
    "Nariño": 7,
    "Fucha": 6,
    "Santa Lucía": 5,
    "Socorro": 4,
    "Consuelo": 3,
    "Molinos": 2,
    "Danubio": 1,
    "Portal Usme": 0
}

# heurística
def heuristica(estacion):
    return heuristica_hasta_portal_usme.get(estacion, 999)

# A*
def a_estrella(grafo, inicio, objetivo):
    abiertos = []
    heapq.heappush(abiertos, (0, inicio))

    vino_de = {}

    g_score = {}
    for nodo in grafo:
        g_score[nodo] = float("inf")
    g_score[inicio] = 0

    f_score = {}
    for nodo in grafo:
        f_score[nodo] = float("inf")
    f_score[inicio] = heuristica(inicio)

    while abiertos:
        _, actual = heapq.heappop(abiertos)

        if actual == objetivo:
            ruta = [actual]

            while actual in vino_de:
                actual = vino_de[actual]
                ruta.append(actual)

            ruta.reverse()
            return ruta, g_score[objetivo]

        for vecino, costo in grafo[actual].items():
            costo_tentativo = g_score[actual] + costo

            if costo_tentativo < g_score[vecino]:
                vino_de[vecino] = actual
                g_score[vecino] = costo_tentativo
                f_score[vecino] = costo_tentativo + heuristica(vecino)

                heapq.heappush(abiertos, (f_score[vecino], vecino))

    return None

# IMPRIMIR 
def mostrar_ruta(origen, destino):
    resultado = a_estrella(grafo, origen, destino)

    if resultado:
        ruta, costo_total = resultado

        print("\n===== RESULTADO =====")
        print("Origen: " + origen)
        print("Destino: " + destino)
        print("Mejor ruta encontrada:")
        print(" -> ".join(ruta))
        print("Cantidad de tramos: " + str(len(ruta) - 1))
        print("Costo total: " + str(costo_total))
    else:
        print("\nNo se encontró una ruta entre esas estaciones.")

# IMPRIMIR
print ("Sistema inteligente de rutas de transporte masivo")
print ("Estaciones disponibles:")
for estacion in grafo:
    print ("- " + estacion)

#PEDIR DATOS
origen = raw_input("Ingrese la estación de origen: ")
destino = raw_input("Ingrese la estación de destino: ")

if origen not in grafo or destino not in grafo:
    print ("\nError: una o ambas estaciones no existen en la base de conocimiento.")
else:
    mostrar_ruta(origen, destino)
