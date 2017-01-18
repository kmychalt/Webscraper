# Demo file for Spyder Tutorial
# Hans Fangohr, University of Southampton, UK
from graphviz import Digraph
dot = Digraph(comment = 'RoundTable')

dot.node('A', 'King A')
dot.node('B', 'Sir B')
dot.node('L', 'Sir L')
dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint = 'false')
#print(dot.source)

dot.render('round-table.gv', view=True)