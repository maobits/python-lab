"""
================================================================================
PROYECTO: PARADOJA DEL CUMPLEAÑOS – SIMULACIÓN DE PROBABILIDAD
Instituto Maobits
Arquitectura Mental y Tecnológica para Negocios

Fundador:
Mauricio Chara Hurtado
Empresario del sector de las ciencias de la computación

Perfil Profesional:
Empresario informático con más de 10 años de experiencia en el desarrollo
de soluciones tecnológicas, formación digital y transformación de procesos
mediante pensamiento estructurado, modelamiento y arquitectura lógica.

Lidero el modelo educativo Maobits, enfocado en arquitectura mental aplicada
al desarrollo tecnológico y empresarial.

Integrando desarrollo de software, producción audiovisual y marketing digital
para la transformación empresarial y educativa.

-------------------------------------------------------------------------------
CRÉDITOS DE OBRA BASE

Basado en el proyecto:
“Birthday Paradox Simulation”

Libro:
"The Big Book of Small Python Projects"

Autor:
Al Sweigart

Disponible en:
https://inventwithpython.com/bigbookpython/

Licencia:
Creative Commons
-------------------------------------------------------------------------------

DESCRIPCIÓN DEL PROYECTO

Este programa explora la famosa "Paradoja del Cumpleaños".

La paradoja demuestra que en un grupo relativamente pequeño de personas
es sorprendentemente probable que al menos dos compartan la misma fecha
de cumpleaños.

El programa realiza:

• Generación de cumpleaños aleatorios
• Búsqueda de coincidencias
• Simulación Monte Carlo
• Cálculo aproximado de probabilidades

Este proyecto introduce conceptos de:

• Simulación probabilística
• Modelamiento matemático
• Listas y conjuntos
• Comparación de datos
• Algoritmos de búsqueda
================================================================================
"""

# ------------------------------------------------------------------------------
# IMPORTACIÓN DE LIBRERÍAS
# ------------------------------------------------------------------------------

# datetime permite trabajar con fechas.
import datetime

# random permite generar valores aleatorios.
import random


# ------------------------------------------------------------------------------
# CONFIGURACIÓN DEL SISTEMA
# ------------------------------------------------------------------------------

# Número máximo de cumpleaños que puede generar el usuario.
MAX_CUMPLEANOS = 100

# Número total de simulaciones Monte Carlo.
TOTAL_SIMULACIONES = 100000


# ------------------------------------------------------------------------------
# FUNCIÓN: GENERAR CUMPLEAÑOS ALEATORIOS
# ------------------------------------------------------------------------------

def generar_cumpleanos(cantidad):
    """
    Genera una lista de fechas aleatorias que representan cumpleaños.

    Todas las fechas se generan dentro del mismo año para facilitar
    la comparación entre ellas.
    """

    lista_cumpleanos = []

    for i in range(cantidad):

        # Se define el inicio del año.
        inicio_anio = datetime.date(2001, 1, 1)

        # Se genera un número aleatorio de días dentro del año.
        dias_aleatorios = datetime.timedelta(random.randint(0, 364))

        # Se calcula la fecha final.
        cumpleanos = inicio_anio + dias_aleatorios

        # Se agrega la fecha a la lista.
        lista_cumpleanos.append(cumpleanos)

    return lista_cumpleanos


# ------------------------------------------------------------------------------
# FUNCIÓN: BUSCAR COINCIDENCIA DE CUMPLEAÑOS
# ------------------------------------------------------------------------------

def buscar_coincidencia(cumpleanos):
    """
    Busca si existe una fecha de cumpleaños repetida dentro de la lista.

    Retorna:
    - La fecha repetida si existe coincidencia
    - None si todos los cumpleaños son diferentes
    """

    # Si todos los cumpleaños son únicos
    if len(cumpleanos) == len(set(cumpleanos)):
        return None

    # Comparación entre cada cumpleaños
    for indice_a, cumple_a in enumerate(cumpleanos):
        for indice_b, cumple_b in enumerate(cumpleanos[indice_a + 1:]):

            if cumple_a == cumple_b:
                return cumple_a

    return None


# ------------------------------------------------------------------------------
# FUNCIÓN PRINCIPAL
# ------------------------------------------------------------------------------

def main():
    """
    Punto de entrada del programa.

    Controla todo el flujo de ejecución de la simulación.
    """

    print("""Paradoja del Cumpleaños – Simulación de Probabilidad

La paradoja del cumpleaños demuestra que en un grupo de personas
es sorprendentemente probable que al menos dos compartan
la misma fecha de cumpleaños.

Este programa realiza múltiples simulaciones aleatorias
para explorar esta probabilidad.

Esto se conoce como una simulación Monte Carlo.
""")

    # Tupla con los nombres de los meses.
    MESES = (
        "Ene", "Feb", "Mar", "Abr", "May", "Jun",
        "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"
    )

    # --------------------------------------------------------------------------
    # VALIDACIÓN DE ENTRADA DEL USUARIO
    # --------------------------------------------------------------------------

    while True:

        print(f"¿Cuántos cumpleaños deseas generar? (Máximo {MAX_CUMPLEANOS})")

        respuesta = input("> ")

        if respuesta.isdecimal() and (0 < int(respuesta) <= MAX_CUMPLEANOS):
            cantidad_personas = int(respuesta)
            break

    print()

    # --------------------------------------------------------------------------
    # GENERACIÓN DE CUMPLEAÑOS
    # --------------------------------------------------------------------------

    print("Aquí están los", cantidad_personas, "cumpleaños generados:")

    cumpleanos = generar_cumpleanos(cantidad_personas)

    for i, cumple in enumerate(cumpleanos):

        if i != 0:
            print(", ", end="")

        nombre_mes = MESES[cumple.month - 1]
        texto_fecha = f"{nombre_mes} {cumple.day}"

        print(texto_fecha, end="")

    print()
    print()

    # --------------------------------------------------------------------------
    # DETECTAR COINCIDENCIA
    # --------------------------------------------------------------------------

    coincidencia = buscar_coincidencia(cumpleanos)

    print("En esta simulación, ", end="")

    if coincidencia is not None:

        nombre_mes = MESES[coincidencia.month - 1]
        texto_fecha = f"{nombre_mes} {coincidencia.day}"

        print("varias personas tienen cumpleaños el", texto_fecha)

    else:

        print("no hay cumpleaños coincidentes.")

    print()

    # --------------------------------------------------------------------------
    # SIMULACIÓN MONTE CARLO
    # --------------------------------------------------------------------------

    print("Generando", cantidad_personas, "cumpleaños aleatorios",
          TOTAL_SIMULACIONES, "veces...")

    input("Presiona Enter para comenzar la simulación...")

    coincidencias = 0

    for i in range(TOTAL_SIMULACIONES):

        # Mostrar progreso cada 10.000 simulaciones
        if i % 10000 == 0:
            print(i, "simulaciones ejecutadas...")

        cumpleanos = generar_cumpleanos(cantidad_personas)

        if buscar_coincidencia(cumpleanos) is not None:
            coincidencias += 1

    print(TOTAL_SIMULACIONES, "simulaciones ejecutadas.")

    # --------------------------------------------------------------------------
    # CÁLCULO DE PROBABILIDAD
    # --------------------------------------------------------------------------

    probabilidad = round(coincidencias / TOTAL_SIMULACIONES * 100, 2)

    print("De", TOTAL_SIMULACIONES, "simulaciones con grupos de",
          cantidad_personas, "personas:")

    print("Hubo coincidencias de cumpleaños en",
          coincidencias, "casos.")

    print("Esto significa que la probabilidad aproximada de coincidencia es:")

    print(probabilidad, "%")

    print("¡Probablemente es más alta de lo que imaginabas!")


# ------------------------------------------------------------------------------
# EJECUCIÓN DEL PROGRAMA
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()