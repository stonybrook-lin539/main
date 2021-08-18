import pydot

nodes = set("abcd")
edges = [("a","b"), ("b","c"), ("c","d"),
         ("a","c"), ("b","d"), ("a","d")]

g = pydot.Dot("relation", graph_type="digraph", rankdir="LR")
# g.set_graph_defaults(dpi=96)
g.set_node_defaults(shape="circle", height=0.1, fontsize=16, margin="0.0,0.0")
for node in nodes:
    g.add_node(pydot.Node(node))
for edge in edges:
    g.add_edge(pydot.Edge(*edge))


def test_write_png():
    g.write_png("pydot-test.png")


def test_view_tk():
    import PIL.ImageTk
    import tkinter as tk
    root = tk.Tk()
    img = PIL.ImageTk.PhotoImage(data=g.create_png())
    label = tk.Label(root, image=img)
    label.pack()
    root.mainloop()


if __name__ == "__main__":
    test_view_tk()
