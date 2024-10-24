# Inicialización del tablero (6 filas x 7 columnas)
FILAS = 6
COLUMNAS = 7
tablero = [[' ' for _ in range(COLUMNAS)] for _ in range(FILAS)]

def imprimir_tablero():
    # Imprimir el tablero con las fichas
    for fila in tablero:
        print('| ' + ' | '.join(fila) + ' |')
    print('-' * (COLUMNAS * 4 - 1))  # Línea divisoria entre filas

def colocar_ficha(fila, columna, ficha):
    if tablero[fila][columna] == ' ':
        tablero[fila][columna] = ficha
        return True
    else:
        return False

def verificar_victoria(ficha):
    # Comprobar filas, columnas y diagonales para una victoria
    # Comprobar filas
    for fila in range(FILAS):
        for col in range(COLUMNAS - 3):
            if tablero[fila][col] == ficha and tablero[fila][col+1] == ficha and tablero[fila][col+2] == ficha and tablero[fila][col+3] == ficha:
                return True

    # Comprobar columnas
    for col in range(COLUMNAS):
        for fila in range(FILAS - 3):
            if tablero[fila][col] == ficha and tablero[fila+1][col] == ficha and tablero[fila+2][col] == ficha and tablero[fila+3][col] == ficha:
                return True

    return False

def tablero_lleno():
    for fila in tablero:
        if ' ' in fila:
            return False
    return True

# Juego principal
def juego():
    jugador_actual = 'X'  # Jugador 1 usa 'X'
    while True:
        imprimir_tablero()
        print(f"Turno del jugador {jugador_actual}")

        # Pedir la posición al jugador
        fila = int(input("Ingresa la fila (0-5): "))
        columna = int(input("Ingresa la columna (0-6): "))

        # Intentar colocar la ficha
        if colocar_ficha(fila, columna, jugador_actual):
            # Verificar si hay victoria
            if verificar_victoria(jugador_actual):
                imprimir_tablero()
                print(f"¡El jugador {jugador_actual} ha ganado!")
                break

            # Cambiar de turno
            jugador_actual = 'O' if jugador_actual == 'X' else 'X'

            # Verificar si el tablero está lleno
            if tablero_lleno():
                imprimir_tablero()
                print("¡El tablero está lleno! Es un empate.")
                break
        else:
            print("Posición inválida, intenta de nuevo.")

# Ejecutar el juego
juego()
