from IPython.display import display
import ipywidgets as wid


def callback(event):
    mywid.description = "you clicked me"


mywid = wid.Button(description='Click me', tooltip='Click me')
mywid.on_click(callback)


# just displays text, only works properly in Jupyter notebook
def test_py():
    display(mywid)


# no dynamic behavior in generated HTML
# not sure what the point of this is
def make_html():
    from ipywidgets.embed import embed_minimal_html
    embed_minimal_html('jupytertest.html', views=[mywid], title='Widgets export')


if __name__ == "__main__":
    display()
