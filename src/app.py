import dash
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
from dash_bootstrap_templates import load_figure_template
from callbacks import get_callbacks

# --------------------------------------------------------- #

font_link_1 = "https://fonts.googleapis.com/css2?family=Roboto+Condensed&display=swap"  
font_link_2 = "https://fonts.googleapis.com/css2?family=Chakra+Petch&display=swap"  
app = Dash(__name__, use_pages=True, assets_url_path='assets',
           external_stylesheets=[font_link_1, font_link_2, dbc.themes.DARKLY],
           suppress_callback_exceptions=True)
server = app.server

# --------------------------------------------------------- #

sidebar = html.Div(
    children=[
    html.Div(
      className='sideBar',
      children=
      [
          html.Div(
              className='appTitle-Div',
              children=[
              html.H5("FIFA STAT", className='appTitle'),
              html.H6("VISUALIZER", className='appTitle'),  
          ]),
      ],
    ),
    html.Div(
        className='navBar',
        children=[
          html.Div(
            className='page-nav',
            children=[
              dbc.Nav(
              className='NavButton',
              children=[
                  dbc.NavLink(
                      [
                          html.Div(page['name'], className='navButton')
                      ],
                      href=page['path'],
                      active='exact',
                  )
                  for page in dash.page_registry.values()
              ],
              vertical=True,
              pills=True,
          ),
          ])
      ])
    ]
)

content = html.Div(children=[dash.page_container],id="page-content")

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content,
])

get_callbacks(app)
    
if __name__ == "__main__":
    app.run(debug=True, dev_tools_hot_reload=False)