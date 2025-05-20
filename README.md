Solucionador de Laberintos con DFS y BFS
Descripción:
Este proyecto implementa un solucionador de laberintos que utiliza dos algoritmos clásicos de búsqueda: Depth-First Search (DFS) y Breadth-First Search (BFS). El programa genera laberintos aleatorios y permite visualizar en tiempo real cómo estos algoritmos exploran las celdas para encontrar la ruta desde el punto inicial hasta el final.

Características Principales:
Generación de laberintos usando DFS recursivo (garantiza un camino único).

Resolución con DFS (rápido, pero no siempre encuentra el camino más corto).

Resolución con BFS (encuentra el camino más corto, explora en capas).

Interfaz visual interactiva con Pygame.

Controles simples para regenerar laberintos y cambiar algoritmos.

Tecnologías:
Python 3.13.3 + Pygame (para gráficos).

Instalación:
Clona el repositorio:

bash
git clone https://github.com/tu-usuario/Maze-Solver-DFS-BFS.git
Instala Pygame:

bash
pip install pygame
Uso:
Tecla R: Generar nuevo laberinto.

Tecla S: Iniciar/resolver con el algoritmo seleccionado.

Tecla D: Usar DFS (Búsqueda en Profundidad).

Tecla B: Usar BFS (Búsqueda en Anchura).

Visualización:
Verde: Punto de inicio.

Rojo: Punto final.

Azul: Celdas visitadas durante la búsqueda.

Amarillo: Camino solución encontrado.
