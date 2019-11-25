#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Here's a quick example

import dash
import dash_core_components as dcc
import dash_html_components as html

# Create an app called dash, put the server online
app = dash.Dash(__name__)
  server = app.server 

# Create html with python
# Layout is the webpage
# The children of the Divs, are the next levels, H1 means a big headline
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
# Create graphs within a dashboard, move them, graph has a dictionary and a layout, similar to seaborn
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)

