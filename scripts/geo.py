import json
from random import random
from sys import argv
from math import sqrt, sin, cos, radians, isclose


def get_eq_poly_verts(radius: float, num_sides: int, x_offset: float = 0, y_offset: float = 0):
    angle = 360.0 / num_sides
    verts = []
    i = 0
    while i < num_sides:
        rads = radians(angle*i)
        x = radius * cos(rads) + x_offset
        y = radius * sin(rads) + y_offset
        verts.append((x, y))
        i += 1
    return verts


def distance_between(c1, c2):
    x1=c1[0]
    x2=c2[0]
    y1=c1[1]
    y2=c2[1]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test(verts, r):
    i = 0
    while i < len(verts):
        a = verts[i]
        b = verts[i-1]
        print(
            isclose(a[0]**2 + a[1]**2, r), 
            isclose(b[0]**2 + b[1]**2, r), 
            round(distance_between(a, b), 5)
        )
        i += 1


r = 0.1
sides = 3
verts = get_eq_poly_verts(r, sides)
out = {
    "objects": [
        {
            "id": 0,
            "name": "small",
            "vertices": verts,
            "indices": [0, 1, 2]
        }
    ],
}

instances = []

for i in range(-8, 10, 2):
    x = i/10
    for j in range(-8, 10, 2):
        y = j/10
        instances.append({
            "objectId": 0,
            "position": [x, y],
            "rotation": random() * 360,
            "velocity": [0, 0]
        })

out["instances"] = instances

with open("../models/objects.json", "w") as f:
    json.dump(out, f, indent=2)
