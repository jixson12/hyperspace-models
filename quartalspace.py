from vpython import *

w_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), length=100, shaftwidth=1, color=color.cyan)
x_axis = arrow(pos=vector(0, 0, 0), axis=vector(sqrt(8/9), 0, -1/3), length=100, shaftwidth=1, color=color.blue)
y_axis = arrow(
    pos=vector(0, 0, 0),
    axis=vector(-sqrt(2/9), sqrt(2/3), -1/3),
    length=100,
    shaftwidth=1,
    color=color.green
)
z_axis = arrow(
    pos=vector(0, 0, 0),
    axis=vector(-sqrt(2/9), -sqrt(2/3), -1/3),
    length=100,
    shaftwidth=1,
    color=color.red
)
tetrotation = [[sqrt(8/9), 0, -1/3],
 [-sqrt(2/9), sqrt(2/3), -1/3],
 [sqrt(2/9), -sqrt(2/3), -1/3]]

