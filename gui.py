# Python Chapter 16 - Part 187 ff

import ipywidgets as widgets
from IPython.display import display

widgets.Button(description="Push me")
widgets.Text(description="My text", value"123")
widgets.Checkbox(description"Description" value=False)

widgets.RadioButtons(
    options=['A','B','C'],
    description='Which letter?',
    disabled=False
)

widgets.Dropdown(
    options=['A','B','C']
    description='Which letter?',
    disabled=False
)