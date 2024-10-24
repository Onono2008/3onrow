# Tres en raya para dos jugadores

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    print("\n")
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)

# Función para verificar si hay un ganador
def comprobar_victoria(tablero, jugador):
    # Comprobar filas, columnas y diagonales
    for fila in tablero:
        if fila.count(jugador) == 3:
            return True
    for col in range(3):
        if [tablero[f][col] for f in range(3)].count(jugador) == 3:
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False

# Función para comprobar si el tablero está lleno (empate)
def comprobar_empate(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True

# Función para el flujo del juego
def jugar():
    # Crear un tablero vacío
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"
    
    while True:
        imprimir_tablero(tablero)
        print(f"Turno de {jugador_actual}")
        
        # Solicitar movimiento
        try:
            fila = int(input("Selecciona la fila (0, 1, 2): "))
            columna = int(input("Selecciona la columna (0, 1, 2): "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue
        
        # Verificar si la casilla está vacía
        if tablero[fila][columna] != " ":
            print("Esta casilla ya está ocupada. Elige otra.")
            continue
        
        # Hacer el movimiento
        tablero[fila][columna] = jugador_actual
        
        # Comprobar si el jugador actual ha ganado
        if comprobar_victoria(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡El jugador {jugador_actual} ha ganado!")
            break
        
        # Comprobar si hay empate
        if comprobar_empate(tablero):
            imprimir_tablero(tablero)
            print("¡Es un empate!")
            break
        
        # Cambiar de jugador
        jugador_actual = "O" if jugador_actual == "X" else "X"

# Iniciar el juego
if __name__ == "__main__":
    jugar()
