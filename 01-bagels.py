"""
================================================================================
PROYECTO: BAGELS – JUEGO DE LÓGICA DEDUCTIVA
Instituto Maobits
Arquitectura Mental y Tecnológica para Negocios

Fundador:
Mauricio Chara Hurtado
Empresario del sector de las ciencias de la computación

Perfil Profesional:
Empresario informático con más de 10 años de experiencia en el desarrollo
de soluciones tecnológicas, formación digital y transformación de procesos
mediante pensamiento estructurado, modelamiento y arquitectura lógica.
Lidero el modelo educativo Maobits, enfocando la arquitectura mental y
tecnológica aplicada a los negocios.

Integrando desarrollo de software, producción audiovisual y marketing digital
para la transformación empresarial y educativa.

-------------------------------------------------------------------------------
CRÉDITOS DE OBRA BASE

Basado en el proyecto “Bagels”
del libro “The Big Book of Small Python Projects”
Autor: Al Sweigart
Disponible en: https://inventwithpython.com/bigbookpython/
Licencia: Creative Commons
-------------------------------------------------------------------------------

Descripción:
Juego de lógica deductiva donde el usuario debe adivinar un número secreto
de N dígitos sin repetir, utilizando pistas de inferencia lógica:
- Pico
- Fermi
- Bagels

Este proyecto se utiliza como modelo de arquitectura mental aplicada.
================================================================================
"""

# ------------------------------------------------------------------------------
# IMPORTACIÓN DE LIBRERÍAS
# ------------------------------------------------------------------------------

# Importamos la librería random para generar números aleatorios.
import random


# ------------------------------------------------------------------------------
# CONFIGURACIÓN DEL SISTEMA (CONSTANTES)
# ------------------------------------------------------------------------------

# Número de dígitos que tendrá el número secreto.
NUM_DIGITOS = 3

# Número máximo de intentos permitidos.
MAX_INTENTOS = 10


# ------------------------------------------------------------------------------
# FUNCIÓN PRINCIPAL (CONTROLADOR DEL SISTEMA)
# ------------------------------------------------------------------------------

def main():
    """
    Punto de entrada del programa.
    Controla el flujo general del juego.
    """

    print(f"""
Bagels – Juego de Lógica Deductiva

Estoy pensando en un número de {NUM_DIGITOS} dígitos sin repetir.
Intenta adivinar cuál es.

Cuando diga:
Pico   -> Un dígito correcto en posición incorrecta.
Fermi  -> Un dígito correcto en posición correcta.
Bagels -> Ningún dígito es correcto.
""")

    # Bucle principal del sistema (permite múltiples partidas)
    while True:

        # Generar número secreto
        numero_secreto = obtener_numero_secreto()

        print("He pensado un número.")
        print(f"Tienes {MAX_INTENTOS} intentos para adivinarlo.")

        # Inicializar contador de intentos
        intentos = 1

        # Bucle interno: controla número de intentos
        while intentos <= MAX_INTENTOS:

            intento = ""

            # ------------------------------------------------------------------
            # VALIDACIÓN DE ENTRADA
            # ------------------------------------------------------------------
            # Se repite hasta que el usuario ingrese exactamente
            # la cantidad correcta de dígitos y solo números.
            while len(intento) != NUM_DIGITOS or not intento.isdecimal():
                print(f"Intento #{intentos}:")
                intento = input("> ")

            # Obtener pistas del intento
            pistas = obtener_pistas(intento, numero_secreto)
            print(pistas)

            # Verificar si ganó
            if intento == numero_secreto:
                break

            # Incrementar contador
            intentos += 1

            # Verificar si se acabaron los intentos
            if intentos > MAX_INTENTOS:
                print("Se acabaron los intentos.")
                print(f"El número secreto era {numero_secreto}.")

        # Preguntar si desea jugar nuevamente
        print("¿Quieres jugar otra vez? (si/no)")
        if not input("> ").lower().startswith("s"):
            break

    print("¡Gracias por jugar!")


# ------------------------------------------------------------------------------
# FUNCIÓN: GENERAR NÚMERO SECRETO
# ------------------------------------------------------------------------------

def obtener_numero_secreto():
    """
    Genera un número secreto sin dígitos repetidos.
    """

    # Crear lista de dígitos del 0 al 9
    numeros = list("0123456789")

    # Mezclar aleatoriamente los dígitos
    random.shuffle(numeros)

    # Construir número secreto
    numero_secreto = ""
    for i in range(NUM_DIGITOS):
        numero_secreto += numeros[i]

    return numero_secreto


# ------------------------------------------------------------------------------
# FUNCIÓN: MOTOR DE INFERENCIA (PISTAS)
# ------------------------------------------------------------------------------

def obtener_pistas(intento, numero_secreto):
    """
    Compara el intento con el número secreto
    y devuelve las pistas correspondientes.
    """

    # Si coincide exactamente → victoria
    if intento == numero_secreto:
        return "¡Correcto! Has adivinado el número."

    pistas = []

    # Comparación posición por posición
    for i in range(NUM_DIGITOS):

        # Coincidencia exacta
        if intento[i] == numero_secreto[i]:
            pistas.append("Fermi")

        # Dígito correcto pero posición incorrecta
        elif intento[i] in numero_secreto:
            pistas.append("Pico")

    # Si no hay coincidencias
    if not pistas:
        return "Bagels"

    # Ordenar pistas (evita dar información por posición)
    pistas.sort()

    # Unir lista en string final
    return " ".join(pistas)


# ------------------------------------------------------------------------------
# EJECUCIÓN DEL PROGRAMA
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()