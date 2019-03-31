from vpython import *

dt = 0.1

hyperspace = canvas(title='Hypersphere intersecting flattened 3D hyperplane', width=600, height=400)
space = canvas(title='3D slice of hypersphere in 3D space', width=600, height=400)
quartalspace = canvas(title='Tetrahedral coordinate system to model 4 dimensions')

hypersphere = sphere(pos=vector(0, 12, 0), radius=12, color=color.red, opacity=0.8, canvas=hyperspace)
hyperroom = box(size=vector(30, 1, 30), color=color.green, opacaity=0.3, canvas=hyperspace)
hyperplane = box(size=vector(60, 1, 60), color=color.blue, opacity=0.3, canvas=hyperspace)
hypersphere.velocity = vector(0, -1, 0)

room_x = arrow(pos=vector(0, 0, 0), axis=vector(30, 0, 0), shaftwidth=1, color=color.green, canvas=space)
room_y = arrow(pos=vector(0, 0, 0), axis=vector(0, 30, 0), shaftwidth=1, color=color.green, canvas=space)
room_z = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 30), shaftwidth=1, color=color.green, canvas=space)

slice_sphere = sphere(pos=vector(15, 15, 15), radius=0, color=color.red, canvas=space, visible=False)

slice_radius = 0
while(1):
    rate(100)
    hypersphere.pos = hypersphere.pos + (hypersphere.velocity * dt)
    if abs(hypersphere.pos.y) >= hypersphere.radius:
        slice_sphere.visible = False
    if abs(hypersphere.pos.y) > 1.2 * hypersphere.radius:
        hypersphere.velocity.y *= -1
    if abs(hypersphere.pos.y) < hypersphere.radius:
        slice_radius = sqrt(pow(hypersphere.radius, 2) - pow(hypersphere.pos.y, 2))
        slice_sphere.visible = True
        slice_sphere.radius = slice_radius








