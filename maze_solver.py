import pygame
import random
from collections import deque

# Configuración de colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)

# Dimensiones de la ventana
ANCHO = 800
ALTO = 600

# Tamaño del laberinto (en celdas)
FILAS = 30
COLUMNAS = 30

# Tamaño de cada celda
ANCHO_CELDA = ANCHO // COLUMNAS
ALTO_CELDA = ALTO // FILAS

class Laberinto:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Laberinto DFS/BFS")
        self.reloj = pygame.time.Clock()
        
        # Inicializar laberinto
        self.laberinto = []
        self.inicio = (1, 1)
        self.final = (FILAS - 2, COLUMNAS - 2)
        
        # Variables de estado
        self.solucion = []
        self.visitados = set()
        
        # Generar laberinto inicial
        self.generar_laberinto()
    
    def generar_laberinto(self):
        # Crear matriz llena de paredes
        self.laberinto = [[1 for _ in range(COLUMNAS)] for _ in range(FILAS)]
        
        # Función recursiva para generar el laberinto con DFS
        def cavar(fila, columna):
            self.laberinto[fila][columna] = 0
            direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            random.shuffle(direcciones)
            
            for df, dc in direcciones:
                nueva_fila = fila + df * 2
                nueva_col = columna + dc * 2
                
                if (0 <= nueva_fila < FILAS and 
                    0 <= nueva_col < COLUMNAS and 
                    self.laberinto[nueva_fila][nueva_col] == 1):
                    self.laberinto[fila + df][columna + dc] = 0
                    cavar(nueva_fila, nueva_col)
        
        # Comenzar a cavar desde una posición impar
        cavar(1, 1)
        
        # Asegurar inicio y final
        self.laberinto[self.inicio[0]][self.inicio[1]] = 0
        self.laberinto[self.final[0]][self.final[1]] = 0
    
    def dibujar(self):
        self.pantalla.fill(NEGRO)
        
        for fila in range(FILAS):
            for col in range(COLUMNAS):
                color = NEGRO
                if self.laberinto[fila][col] == 0:
                    color = BLANCO
                if (fila, col) == self.inicio:
                    color = VERDE
                elif (fila, col) == self.final:
                    color = ROJO
                elif (fila, col) in self.solucion:
                    color = AMARILLO
                elif (fila, col) in self.visitados:
                    color = AZUL
                
                pygame.draw.rect(
                    self.pantalla,
                    color,
                    (col * ANCHO_CELDA, fila * ALTO_CELDA, ANCHO_CELDA, ALTO_CELDA)
                )
        
        pygame.display.flip()
    
    def resolver_dfs(self):
        pila = [(self.inicio, [self.inicio])]
        self.visitados = set()
        self.solucion = []
        
        while pila:
            (fila, col), camino = pila.pop()
            
            if (fila, col) == self.final:
                self.solucion = camino
                return True
            
            if (fila, col) in self.visitados:
                continue
            
            self.visitados.add((fila, col))
            
            # Actualizar visualización
            self.dibujar()
            pygame.display.update()
            self.reloj.tick(20)
            
            # Explorar vecinos
            for df, dc in [(-1,0), (0,1), (1,0), (0,-1)]:
                nf = fila + df
                nc = col + dc
                if (0 <= nf < FILAS and 
                    0 <= nc < COLUMNAS and 
                    self.laberinto[nf][nc] == 0 and 
                    (nf, nc) not in self.visitados):
                    pila.append(((nf, nc), camino + [(nf, nc)]))
        
        return False
    
    def resolver_bfs(self):
        cola = deque([(self.inicio, [self.inicio])])
        self.visitados = set([self.inicio])
        self.solucion = []
        
        while cola:
            (fila, col), camino = cola.popleft()
            
            if (fila, col) == self.final:
                self.solucion = camino
                return True
            
            # Actualizar visualización
            self.dibujar()
            pygame.display.update()
            self.reloj.tick(20)
            
            # Explorar vecinos
            for df, dc in [(-1,0), (0,1), (1,0), (0,-1)]:
                nf = fila + df
                nc = col + dc
                if (0 <= nf < FILAS and 
                    0 <= nc < COLUMNAS and 
                    self.laberinto[nf][nc] == 0 and 
                    (nf, nc) not in self.visitados):
                    self.visitados.add((nf, nc))
                    cola.append(((nf, nc), camino + [(nf, nc)]))
        
        return False

def main():
    lab = Laberinto()
    ejecutando = True
    algoritmo = "dfs"  # 'dfs' o 'bfs'
    resuelto = False
    
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    lab = Laberinto()
                    resuelto = False
                elif evento.key == pygame.K_s and not resuelto:
                    if algoritmo == "dfs":
                        resuelto = lab.resolver_dfs()
                    else:
                        resuelto = lab.resolver_bfs()
                elif evento.key == pygame.K_d:
                    algoritmo = "dfs"
                    print("Usando DFS")
                elif evento.key == pygame.K_b:
                    algoritmo = "bfs"
                    print("Usando BFS")
        
        lab.dibujar()
        lab.reloj.tick(30)
    
    pygame.quit()

if __name__ == "__main__":
    main()
