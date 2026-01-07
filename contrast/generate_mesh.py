from math import cos, sin, pi, radians
import numpy as np
import matplotlib.pyplot as plt


def generate_mesh(size: int, x: float, y: float, V1_length: float, V1_degree: float, V1_min: int, V1_max: int, V2


    V1_angle = radians(V1_degree)
    V2_angle = radians(V2_degree)

    mesh_basis = np.array([[V1_length*cos(V1_angle), V1_length*sin(V1_angle)], [V2_length*cos(V2_angle), V2_lengt

    POINT1 = np.array([x,y], dtype = float)

    big_mesh = np.array([POINT1+mesh_basis[0]*i+mesh_basis[1]*j for i in range(V1_min, V1_max) for j in range(V2_
    
    return big_mesh

