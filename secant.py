from vpython import *

# x^2 + y^2 = 12
UNIT_RADIUS = 12

unit_circle = extrusion(
    path=paths.circle(radius=UNIT_RADIUS, up=vector(0, 0, 1)),
    shape=shapes.circle(radius=0.25)
)
ticks = {}
for i in range(2*UNIT_RADIUS):
    theta_rad = pi * i / UNIT_RADIUS
    theta_deg = degrees(theta_rad)
    x = cos(theta_rad)
    y = sin(theta_rad)
    tick = box(
        pos=vector(x * UNIT_RADIUS, y * UNIT_RADIUS, 0),
        axis=vector(x, y, 0)
    )
    tick_label = label(pos=tick.pos, text=str(round(theta_deg)))
    ticks[theta_deg] = tick


