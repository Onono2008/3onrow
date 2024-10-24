document.addEventListener("DOMContentLoaded", () => {
    const celdas = document.querySelectorAll(".celda");
    let turno = 1;

    // Inicializa el tablero vacío
    const tablero = Array(6).fill(null).map(() => Array(7).fill(null));

    // Maneja los clics en las celdas
    celdas.forEach(celda => {
        celda.addEventListener("click", () => {
            const columna = parseInt(celda.getAttribute("data-col"));

            // Encuentra la primera fila disponible en la columna
            for (let fila = 5; fila >= 0; fila--) {
                if (!tablero[fila][columna]) {
                    tablero[fila][columna] = turno;
                    document.querySelectorAll(".fila")[fila].children[columna].setAttribute("data-player", turno);

                    // Cambiar de turno
                    turno = turno === 1 ? 2 : 1;
                    break;
                }
            }
        });
    });
});
