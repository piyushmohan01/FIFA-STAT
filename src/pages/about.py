import dash
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
from dash_bootstrap_templates import load_figure_template

# --------------------------------------------------------- #

dash.register_page(__name__, name='ABOUT THE PROJECT')
layout = html.Div(
    className='aboutPage-content',
    children=[
      html.Div(
        className='aboutPage-sidebar-content',
        children=[
            html.Div(
              className='option_area', 
              children=[
                html.Div(className='about-sidebar-intro', children=[
                  html.P('Hey! This page is a collection of all the things I thought were interesting enough to share with you. Have fun!')
                ]),
                dcc.RadioItems(
                  className='about-radio-options',
                  id='about-radio-options',
                  options=[
                    {'label': 'GUIDE TO FIFA-STAT', 'value': 'About-Tab-1',},
                    {'label': 'USING FOR CASE STUDIES', 'value': 'About-Tab-2',}
                  ],
                   value='About-Tab-1'
                ),
                html.Div(className='about-sidebar-intro', children=[
                  html.P('Find more about the project through the buttons below!')
                ]),
                html.Div(className='about-buttons-div', children=[
                  html.Div(className='buttons-about', children=[
                    html.A(
                    href='https://github.com/piyushmohan01/FIFA-STAT.git',
                      children=[
                        html.Button(children=[
                          html.Img(src='../assets/images/icons/github-mark-white.png')
                      ])],
                      target='_blank',
                    )
                  ]),
                  html.Div(className='buttons-about', children=[
                    html.A(
                    href='https://medium.com/@piyushmohan01/fifa-stat-bb3560543400',
                      children=[
                        html.Button(children=[
                          html.Img(src='../assets/images/icons/medium-icon.png')
                      ])],
                      target='_blank',
                    )
                  ]),                           
                  html.Div(className='buttons-about', children=[
                    html.A(
                    href='https://www.kaggle.com/stefanoleone992/datasets',
                      children=[
                        html.Button(children=[
                          html.Img(src='../assets/images/icons/kaggle-icon.png')
                      ])],
                      target='_blank',
                    )
                  ]),                           
                ])
            ])
        ]),
        html.Div(className='about-page-content', children=[
          html.Div(className='section-content', children=[
            dcc.Markdown(
              className='tab-markdown',
              id='tab-markdown', children=[]
            )
          ])
        ])
    ]
)
