from Programme.utils.calculate_geometry import *

# Définition des sommets dans le plan 2D
vertices = [
    [0, 0],   # Sommet 0
    [0, 5],   # Sommet 1
    [3, 0]   # Sommet 2 (exemple supplémentaire)
]

# Exemple : longueur de l'arête entre les sommets 0 et 1
length = edge_length(vertices[0], vertices[1])
print(f"Longueur de l'arête entre le sommet 0 et le sommet 1 : {length}")