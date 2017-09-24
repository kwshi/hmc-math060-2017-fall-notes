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

x_axis = tikz.Path(style=tikz.Style('draw', 'thick', '->'))
y_axis = tikz.Path(style=tikz.Style('draw', 'thick', '->'))
z_axis = tikz.Path(style=tikz.Style('draw', 'thick', '->'))

x_axis.add(tikz.Point3D(0, 0, 0))
y_axis.add(tikz.Point3D(0, 0, 0))
z_axis.add(tikz.Point3D(0, 0, 0))

x_axis.add(sh.Line())
x_axis.add(tikz.Point3D(r_max+1, 0, 0))
x_axis.add(sh.Node('\\(x\\)', style=tikz.Style('below left')))

y_axis.add(sh.Line())
y_axis.add(tikz.Point3D(0, r_max+1, 0))
y_axis.add(sh.Node('\\(y\\)', style=tikz.Style('below right')))

z_axis.add(sh.Line())
z_axis.add(tikz.Point3D(0, 0, 3))
z_axis.add(sh.Node('\\(z\\)', style=tikz.Style('above')))

print(x_axis)
print(y_axis)
print(z_axis)


line = tikz.Path(style=tikz.Style('draw', 'ultra thick'))
cut = tikz.Path(style=tikz.Style(fill='gray', opacity=.5))
below = tikz.Path(style=tikz.Style(fill='gray', opacity=.5))
below_outline = tikz.Path(style=tikz.Style('draw'))

line.add(cyl_fn(0, theta_cut))
cut.add(cyl_fn(0, theta_cut))
below.add(cyl_fn(0, theta_cut))

for j in range(r_n):
    r = j/r_n * r_max
    r_next = (j+1)/r_n * r_max

    line.add(sh.Line())
    line.add(cut_cyl(r_next))

    cut.add(sh.Line())
    cut.add(cut_cyl(r_next))

    below.add(sh.Line())
    below.add(cut_cyl(r_next))

below.add(sh.Line())
below.add(cyl(r_max, theta_cut, -2))
below.add(sh.Line())
below.add(cyl(0, 0, -2))

#below_outline.add(cyl_fn(0, 0))
#below_outline.add(sh.Line())
#below_outline.add(cyl(0, 0, -2))
#below_outline.add(sh.Line())
#below_outline.add(cyl(r_max, theta_cut, -2))
#below_outline.add(sh.Line())
#below_outline.add(cyl_fn(r_max, theta_cut))


print(below)
#print(below_outline)


for i in range(theta_n):
    theta = i/theta_n * theta_max
    theta_next = (i+1)/theta_n * theta_max

    for j in range(r_n):
        r = j/r_n * r_max
        r_next = (j+1)/r_n * r_max

        style = tikz.Style(
            fill='black!{}'.format(100 * color(r, theta))
            #'draw',
            #fill='white'
        )

        poly = tikz.Path(style=style)

        poly.add(cyl_fn(r, theta))
        poly.add(sh.Line())
        poly.add(cyl_fn(r, theta_next))
        poly.add(sh.Line())
        poly.add(cyl_fn(r_next, theta_next))
        poly.add(sh.Line())
        poly.add(cyl_fn(r_next, theta))

        print(poly)

#outline = tikz.Path(style=tikz.Style('draw'))
#
#outline.add(cyl(0, 0, -2))
#outline.add(cyl(0, 0, 2))
#outline.add(cyl(r_max, theta_cut, 2))
#outline.add(cyl(r_max, theta_cut, -2))
#
#print(outline)

cut.add(sh.Line())
cut.add(cyl(r_max, theta_cut, 2))
cut.add(sh.Line())
cut.add(cyl(0, 0, 2))

print(cut)
print(line)

vec = tikz.Path(style=tikz.Style('draw', 'ultra thick', '->'))

r_grad = 2

vec.add(cut_cyl(r_grad))
vec.add(sh.Coordinate(style=tikz.Style('circle', fill='black', **{'inner sep': '1pt'})))

r_deriv = math.cos(r_grad) * math.sin(theta_cut)

grad = cyl(1, theta_cut, r_deriv)
grad /= grad.mag()

vec.add(sh.Line())
vec.add(cut_cyl(r_grad) + grad)


print(vec)


top = tikz.Path(style=tikz.Style('draw', 'ultra thick'))
top.add(tikz.Point3D(0, 0, 2))
top.add(sh.Line())
top.add(sh.Node('\\(\\vec l = \\vec p + t \\uvec v\\)', style=tikz.Style('above right')))
top.add(cyl(r_max, theta_cut, 2))

print(top)


