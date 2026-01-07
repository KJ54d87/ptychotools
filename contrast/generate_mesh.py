from math import cos, sin, pi, radians
import numpy as np
import matplotlib.pyplot as plt


def generate_mesh(size: int, x: float, y: float, V1_length: float, V1_degree: float, V1_min: int, V1_max: int, V2_length: float, V2_degree: float, V2_min: int, V2_max: int):


    V1_angle = radians(V1_degree)
    V2_angle = radians(V2_degree)

    mesh_basis = np.array([[V1_length*cos(V1_angle), V1_length*sin(V1_angle)], [V2_length*cos(V2_angle), V2_length*sin(V2_angle)]])

    POINT1 = np.array([x,y], dtype = float)

    big_mesh = np.array([POINT1+mesh_basis[0]*i+mesh_basis[1]*j for i in range(V1_min, V1_max) for j in range(V2_min, V2_max)])
    
    return big_mesh

def calc_dist(pt: [int]):
    return pt[0]**2 + pt[1]**2

def generate_circle_mesh(x, y, r):
    #make a circle at origin and translate later
    square = np.array([[x,y] for x in range(-r, r) for y in range(-r, r)])
    
    #print(square.shape)
    calc_dist_vectorized = np.vectorize(calc_dist, signature = "(2) -> ()")
    dist = calc_dist_vectorized(square)
    
    circle_mask = dist < r**2
    
    circle = square[circle_mask]
    
    circle = circle + [x, y]
    return circle