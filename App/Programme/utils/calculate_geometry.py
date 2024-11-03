import math

#avoir la longeur entre chaque sommet 

def edge_length(vertex1: list[int], vertex2: list[int]) -> float:

    return math.sqrt(
        (vertex2[0] - vertex1[0])**2 +
        (vertex2[1] - vertex1[1])**2
    )


