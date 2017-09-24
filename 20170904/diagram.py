
import tkz as tikz
import tikz.shapes as sh

nodes = tikz.Path()

f = sh.Node('\\(f(x_1, x_2, x_3)\\)', 'f')

x1 = sh.Node('\\(x_1\\)', 'x1')
x2 = sh.Node('\\(x_2\\)', 'x2')
x3 = sh.Node('\\(x_3\\)', 'x3')

t1 = sh.Node('\\(t_1\\)', 't1')
t2 = sh.Node('\\(t_2\\)', 't2')

nodes.add(tikz.Point2D(0, 0))
nodes.add(f)

nodes.add(tikz.Point2D(-1, -1))
nodes.add(x1)

nodes.add(tikz.Point2D(0, -1))
nodes.add(x2)

nodes.add(tikz.Point2D(1, -1))
nodes.add(x3)

print(nodes)

edges = tikz.Path(style=tikz.Style('draw'))

edges.add(





