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
hud_obj_verts, hud_obj_inds = get_eq_poly_verts(5, 4)
font_verts = []
for i in range(11):
    for j in range(11):
        font_verts.append((j, i))

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
    "font": {
        "vertices": font_verts,
        "characters": [
            {
                "char": "A",
                "indices": [
                    5, 112, 110,
                    5, 49, 112,
                    5, 120, 118,
                    5, 118, 49,
                    70, 72, 95,
                    70, 95, 91
                ]
            },
            {
                "char": "B",
                "indices": [
                    0, 90, 110,
                    0, 24, 90,
                    0, 8, 24,
                    8, 29, 24,
                    8, 32, 29,
                    32, 43, 29,
                    43, 51, 29,
                    43, 63, 51,
                    63, 73, 51,
                    73, 68, 51,
                    51, 68, 46,
                    63, 87, 73,
                    87, 95, 73,
                    87, 98, 95,
                    98, 118, 95,
                    95, 118, 90,
                    118, 110, 90
                ],
            },
            {
                "char": "C",
                "indices": [
                    2, 26, 22,
                    2, 8, 26,
                    26, 8, 28,
                    8, 32, 28,
                    28, 32, 52,
                    52, 32, 54,
                    22, 26, 46,
                    22, 46, 88,
                    46, 68, 88,
                    68, 92, 88,
                    92, 112, 88,
                    92, 94, 112,
                    94, 118, 112,
                    94, 98, 118,
                    74, 98, 94,
                    74, 76, 98
                ]
            },
            {
                "char": "D",
                "indices": [
                    0, 7, 24,
                    24, 7, 28,
                    7, 43, 28,
                    28, 43, 52,
                    43, 87, 74,
                    52, 43, 74,
                    74, 87, 117,
                    74, 117, 94,
                    94, 117, 90,
                    90, 117, 110,
                    90, 110, 24,
                    24, 110, 0
                ]
            },
            {
                "char": "E",
                "indices": [
                    0, 24, 110,
                    0, 10, 24,
                    10, 32, 24,
                    110, 24, 90,
                    46, 54, 76,
                    46, 76, 68,
                    90, 120, 110,
                    90, 98, 120
                ]
            },
            {
                "char": "F",
                "indices": [
                    0, 24, 110,
                    0, 10, 24,
                    10, 32, 24,
                    110, 24, 112,
                    46, 54, 76,
                    46, 76, 68
                ]
            },
            {
                "char": "G",
                "indices": [
                    0, 10, 24,
                    24, 10, 32,
                    0, 24, 110,
                    24, 90, 110,
                    110, 90, 118,
                    90, 96, 118,
                    118, 96, 120,
                    120, 96, 74,
                    74, 54, 120,
                    74, 70, 48,
                    74, 48, 54
                ]
            },
            {
                "char": "H",
                "indices": [
                    0, 2, 112,
                    0, 112, 110,
                    46, 74, 68,
                    46, 52, 74,
                    8, 10, 118,
                    118, 10, 120
                ]
            }, 
            {
                "char": "I",
                "indices": [
                    0, 32, 22,
                    0, 10, 32,
                    26, 28, 92,
                    92, 28, 94,
                    88, 98, 120,
                    88, 120, 110
                ]
            }, 
            {
                "char": "J",
                "indices": [
                    8, 120, 96,
                    8, 10, 120,
                    96, 120, 110,
                    110, 90, 96,
                    110, 68, 90,
                    110, 66, 68
                ]
            }, 
            {
                "char": "K",
                "indices": [
                    0, 112, 110,
                    0, 2, 112,
                    90, 7, 10,
                    90, 57, 7,
                    70, 50, 120,
                    70, 120, 117
                ]
            }, 
            {
                "char": "L",
                "indices": [
                    0, 90, 110,
                    0, 2, 90,
                    110, 90, 98,
                    110, 98, 120
                ]
            }, 
            {
                "char": "M",
                "indices": [
                    0, 24, 110,
                    110, 24, 112,
                    0, 3, 71,
                    3, 38, 71,
                    71, 38, 7,
                    71, 7, 10,
                    30, 10, 120,
                    30, 120, 118
                ]
            },
            {
                "char": "N",
                "indices": [
                    0, 24, 110,
                    110, 24, 112,
                    0, 120, 117,
                    0, 3, 120,
                    96, 8, 120,
                    120, 8, 10
                ]
            },
            {
                "char": "O",
                "indices": [
                    3, 28, 26,
                    3, 7, 28,
                    28, 7, 52,
                    7, 43, 52,
                    52, 43, 74,
                    74, 43, 87,
                    87, 94, 74,
                    94, 87, 117,
                    94, 117, 92,
                    92, 117, 113,
                    92, 113, 68,
                    68, 113, 77,
                    68, 77, 46,
                    46, 77, 33,
                    46, 33, 26,
                    26, 33, 3
                ]
            },
            {
                "char": "P",
                "indices": [
                    0, 24, 110,
                    110, 24, 112,
                    0, 8, 24,
                    24, 8, 32,
                    30, 32, 52,
                    52, 32, 54,
                    46, 54, 74,
                    68, 46, 74
                ]
            },
            {
                "char": "Q",
                "indices": [
                    3, 28, 26,
                    3, 7, 28,
                    28, 7, 52,
                    7, 43, 52,
                    52, 43, 74,
                    74, 43, 87,
                    87, 94, 74,
                    94, 87, 117,
                    94, 117, 92,
                    92, 117, 113,
                    92, 113, 68,
                    68, 113, 77,
                    68, 77, 46,
                    46, 77, 33,
                    46, 33, 26,
                    26, 33, 3,
                    117, 97, 98,
                    117, 98, 120
                ]
            },
            {
                "char": "R",
                "indices": [
                    0, 24, 110,
                    110, 24, 112,
                    0, 8, 24,
                    24, 8, 30,
                    8, 32, 30,
                    30, 32, 54,
                    30, 54, 73,
                    68, 30, 73,
                    68, 73, 82,
                    68, 82, 90,
                    82, 73, 117,
                    117, 73, 120
                ]
            },
            {
                "char": "S",
                "indices": [
                    0, 10, 24,
                    24, 10, 32,
                    0, 24, 46,
                    0, 46, 66,
                    66, 46, 54,
                    66, 54, 74,
                    74, 54, 96,
                    96, 54, 120,
                    96, 120, 110,
                    110, 88, 96
                ]
            },
            {
                "char": "T",
                "indices": [
                    0, 10, 22,
                    22, 10, 32,
                    26, 116, 114,
                    26, 28, 116
                ]
            },
            {
                "char": "U",
                "indices": [
                    0, 2, 90,
                    0, 90, 110,
                    110, 90, 120,
                    90, 96, 120,
                    96, 10, 120,
                    8, 10, 96
                ]
            },
            {
                "char": "V",
                "indices": [
                    0, 82, 115,
                    0, 2, 82,
                    8, 10, 82,
                    82, 10, 115
                ]
            },
            {
                "char": "W",
                "indices": [
                    0, 2, 90,
                    0, 90, 110,
                    110, 90, 113,
                    90, 49, 113,
                    113, 49, 82,
                    82, 49, 117,
                    117, 49, 96,
                    117, 96, 120,
                    96, 10, 120,
                    96, 8, 10
                ]
            },
            {
                "char": "X",
                "indices": [
                    0, 2, 59,
                    2, 49, 59,
                    110, 49, 71,
                    110, 71, 112,
                    71, 49, 10,
                    49, 8, 10,
                    71, 61, 118,
                    118, 61, 120
                ]
            },
            {
                "char": "Y",
                "indices": [
                    0, 2, 59,
                    59, 2, 61,
                    49, 8, 61,
                    61, 8, 10,
                    59, 61, 114,
                    114, 61, 116
                ]
            },
            {
                "char": "Z",
                "indices": [
                    0, 30, 22,
                    0, 10, 30,
                    30, 10, 43,
                    30, 43, 90,
                    30, 90, 77,
                    77, 90, 110,
                    110, 90, 120,
                    120, 90, 98
                ]
            },
            {
                "char": "1",
                "indices": [
                    0, 4, 22,
                    22, 4, 26,
                    4, 6, 92,
                    92, 6, 94,
                    88, 98, 110,
                    110, 98, 120
                ]
            },
            {
                "char": "2",
                "indices": [
                    0, 30, 22, 
                    0, 10, 30,
                    30, 10, 76, 
                    30, 76, 52,
                    52, 76, 68,
                    68, 44, 52,
                    68, 110, 44,
                    110, 68, 90,
                    90, 120, 110,
                    90, 98, 120

                ]
            },
            {
                "char": "3",
                "indices": [
                    0, 30, 22,
                    0, 10, 30,
                    30, 10, 120,
                    30, 120, 96,
                    52, 74, 66,
                    52, 66, 44,
                    96, 120, 110,
                    96, 110, 88
                ]
            },
            {
                "char": "4",
                "indices": [
                    0, 2, 46,
                    0, 46, 66,
                    66, 46, 52,
                    66, 52, 74,
                    8, 10, 118,
                    118, 10, 120
                ]
            },
            {
                "char": "5",
                "indices": [
                    0, 10, 24,
                    24, 10, 32,
                    0, 24, 66,
                    66, 24, 46,
                    66, 46, 74,
                    74, 46, 54,
                    74, 54, 120,
                    74, 120, 96,
                    96, 120, 110,
                    96, 110, 88
                ]
            },
            {
                "char": "6",
                "indices": [
                    0, 10, 32,
                    0, 32, 24,
                    0, 24, 110,
                    110, 24, 90,
                    110, 90, 96,
                    110, 96, 120,
                    120, 96, 54,
                    54, 96, 74,
                    54, 74, 46,
                    46, 74, 68
                ]
            },
            {
                "char": "7",
                "indices": [
                    0, 30, 22,
                    0, 10, 30,
                    30, 10, 43,
                    30, 43, 112,
                    30, 112, 110
                ]
            },
            {
                "char": "8",
                "indices": [
                    0, 10, 24,
                    24, 10, 30,
                    30, 10, 120,
                    30, 120, 96,
                    96, 120, 90,
                    90, 120, 110,
                    90, 110, 24,
                    24, 110, 0,
                    46, 52, 68,
                    68, 52, 74
                ]
            },
            {
                "char": "9",
                "indices": [
                    0, 10, 24,
                    24, 10, 30,
                    30, 10, 120,
                    30, 120, 96,
                    96, 120, 110,
                    96, 110, 88,
                    0, 24, 46,
                    0, 46, 66,
                    66, 46, 52,
                    66, 52, 74
                ]
            },
            {
                "char": "0",
                "indices": [
                    0, 10, 24,
                    24, 10, 30,
                    30, 10, 120,
                    30, 120, 96,
                    96, 120, 90,
                    90, 120, 110,
                    90, 110, 24,
                    24, 110, 0
                ]
            },
            {
                "char": ".",
                "indices": [
                    88, 90, 110,
                    110, 90, 112
                ]
            },
            {
                "char": ",",
                "indices": [
                    66, 68, 88,
                    88, 68, 90,
                    89, 90, 110
                ]
            },
            {
                "char": "!",
                "indices": [
                    0, 2, 66,
                    66, 2, 68,
                    88, 90, 110,
                    110, 90, 112
                ]
            },
        ]
    },
    "hud": { 
        "objects": [
            {
                "vertices": hud_obj_verts,
                "indices": hud_obj_inds
            }
        ],
        "text": [
            {
                "text": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "position": [10, 20],
                "scale": [0.3, 0.3]
            },
            {
                "text": "1234567890.,!",
                "position": [10, 31],
                "scale": [0.3, 0.3]
            },
        ]
    }
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
out["hud"]["objects"][0]["instances"] = [{
    "position": [10, 10]
}]

with open("./models/objects.json", "w") as f:
    json.dump(out, f, indent=2)
