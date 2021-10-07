import networkx as nx
import matplotlib.pyplot as plt

from relation import Relation

r = Relation(set("abcd"), [("a","b"), ("b","c"), ("c","d"),
                           ("a","c"), ("b","d"), ("a","d")])
nxg = nx.DiGraph(r.mapping)
nx.draw_networkx(nxg)
plt.savefig("networkx-test.png")

plt.clf()
pos = nx.bipartite_layout(nxg, ("a", "b"))
nx.draw_networkx(nxg, pos, node_size=1000)
plt.savefig("networkx-test-layout.png")

plt.clf()
pos = nx.nx_pydot.pydot_layout(nxg, prog="dot")
nx.draw_networkx(nxg, pos, node_size=1000)
plt.savefig("networkx-test-pydot-layout.png")

pdg = nx.nx_pydot.to_pydot(nxg)
pdg.set_rankdir("LR")
for node in pdg.get_node_list():
    node.set_shape("circle")
pdg.write_png("nx-test-to-pydot.png")
