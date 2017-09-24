import tkz as tikz
import tikz.shapes as sh
import math

def fn(r, theta):
    return math.sin(r) * math.sin(theta)

def polar(r, theta):
    return r * tikz.Point2D(math.cos(theta), math.sin(theta))

def cyl(r, theta, z):
    return tikz.Point3D(r*math.cos(theta), r*math.sin(theta), z)

def cyl_fn(r, theta):
    return cyl(r, theta, fn(r, theta))

def cut_fn(r):
    return fn(r, theta_cut)

def cut_cyl(r):
    return cyl_fn(r, theta_cut)

def color(r, theta):
    return 1-(fn(r, theta)+1)/2

theta_n = 30
r_n = 50

i_cut = 20

theta_max = math.pi/2
r_max = 5

theta_cut = i_cut/theta_n * theta_max

x_axis = tikz.Path(style=tikz.Style('thick', 'draw', '->'))
z_axis = tikz.Path(style=tikz.Style('thick', 'draw', '->'))

x_axis.add(tikz.Point2D(0, 0))
z_axis.add(tikz.Point2D(0, 0))

x_axis.add(sh.Line())
z_axis.add(sh.Line())

x_axis.add(tikz.Point2D(5, 0))
z_axis.add(tikz.Point2D(0, 3))

x_axis.add(sh.Node('\\(\\vec l = \\vec p + t \\uvec v\\)', style=tikz.Style('right')))
z_axis.add(sh.Node('\\(z\\)', style=tikz.Style('above')))

print(x_axis)
print(z_axis)

plot = tikz.Path(style=tikz.Style('draw'))

plot.add(tikz.Point2D(0, cut_fn(0)))

for j in range(r_n):
    r_next = (j+1)/r_n * r_max
    plot.add(sh.Line())
    plot.add(tikz.Point2D(r_next, cut_fn(r_next)))

vec = tikz.Path(style=tikz.Style('draw', 'ultra thick', '->'))

r_grad = 2

vec.add(tikz.Point2D(r_grad, cut_fn(r_grad)))
vec.add(sh.Coordinate(style=tikz.Style('circle', fill='black', **{'inner sep': '1pt'})))

r_deriv = math.cos(r_grad) * math.sin(theta_cut)

grad = tikz.Point2D(1, r_deriv)
grad /= grad.mag()

vec.add(sh.Line())
vec.add(tikz.Point2D(r_grad, cut_fn(r_grad)) + grad)





print(plot)
print(vec)
