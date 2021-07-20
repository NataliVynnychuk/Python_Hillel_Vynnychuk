import random

MIN_LIMIT = -1
MAX_LIMIT = 1


def create_point(min_limit=MIN_LIMIT, max_limit=MAX_LIMIT):
    point = {"x": random.randint(min_limit, max_limit),
             "y": random.randint(min_limit, max_limit)}
    return point

def create_triangle(points_name_str: str) -> dict:
    return {key: create_point() for key in points_name_str}

def print_triangles_list(triangles_list):
    print("---------------------------------------------")
    for triangle in triangles_list:
        print(triangle)
    print("---------------------------------------------")


triangles_list = []
names = ["ABC", "MNK", "QWE", "ASD"]
for name in names:
    triangle = create_triangle(name)
    triangles_list.append(triangle)
print_triangles_list(triangles_list)
# print(triangles_list)


# triangle_ABC = create_triangle("ABC", -100, 100)
# triangle_MNK = create_triangle("MNK", -10, 10)
# triangle_QWE = create_triangle("QWE", -5, 23)

# triangle_ABC = {key: create_point() for key in "ABC"}

# triangle_ABC = {"A": create_point(),
#                 "B": create_point(),
#                 "C": create_point()}
# print(triangle_ABC)
# print(triangle_MNK)
# print(triangle_QWE)

