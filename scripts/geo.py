import json
from random import random
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

    inds = []
    j = 1
    while j <= num_sides - 2:
        inds.extend([0, j, j + 1])
        j += 1
    
    return verts, inds


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


player_radius = 0.5
small_asteroid_radius = 2
basic_shot_radius = 0.1
basic_shot_verts, basic_shot_inds = get_eq_poly_verts(basic_shot_radius, 10)
player_verts, player_inds = get_eq_poly_verts(player_radius, 10)
small_asteroid_verts, small_asteroid_inds = get_eq_poly_verts(small_asteroid_radius, 10)

out = {
    "player": {
        "position": [55.0, 50.0],
        "radius": player_radius,
        "vertices": player_verts,
        "indices": player_inds,
        "rotation": 0, 
        "velocity": [0, 0],
    },
    "objects": [
        {
            "id": 0,
            "name": "small asteroids",
            "radius": small_asteroid_radius,
            "vertices": small_asteroid_verts,
            "indices": small_asteroid_inds,
            "health": 3,
            "damage": 1
        }
    ],
    "projectiles": [
        {
            "id": 0,
            "name": "basic shot",
            "radius": basic_shot_radius,
            "vertices": basic_shot_verts,
            "indices": basic_shot_inds,
            "health": 1,
            "damage": 1
        }
    ],
    "hud": [
        {
            # TODO
            "vertices": basic_shot_verts,
            "indices": basic_shot_inds,
        }
    ]
}

instances = []

for i in range(10, 100, 10):
    x = i
    for j in range(10, 100, 10):
        y = j
        instances.append({
            "position": [x, y],
            "rotation": random() * 360,
            "velocity": [random() * 10, random() * 10]
        })

out["objects"][0]["instances"] = instances

with open("../models/objects.json", "w") as f:
    json.dump(out, f, indent=2)
