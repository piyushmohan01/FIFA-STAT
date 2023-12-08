import dash
import pandas as pd
import plotly.express as px
from callbacks import get_dropdown_options
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
import dash_daq as daq
from dash_bootstrap_templates import load_figure_template

# --------------------------------------------------------- #

df = pd.read_csv('new_data/m_23.csv', index_col=[0])
data = get_dropdown_options(df)
league_options = list(data['leagues'].keys())
complete_player_list = df['short_name']
cat_dict = {
    'general' : ['pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic'],
    'attacking' : ['attacking_crossing', 'attacking_finishing', 'attacking_heading_accuracy', 'attacking_short_passing', 'attacking_volleys'],
    'skill': ['skill_dribbling', 'skill_curve', 'skill_fk_accuracy', 'skill_long_passing', 'skill_ball_control'],
    'movement': ['movement_acceleration', 'movement_sprint_speed', 'movement_agility', 'movement_reactions', 'movement_balance'],
    'power' : ['power_shot_power', 'power_jumping', 'power_stamina', 'power_strength', 'power_long_shots'],
    'mentality' : ['mentality_aggression', 'mentality_interceptions', 'mentality_positioning', 'mentality_vision', 'mentality_penalties', 'mentality_composure'],
    'defending' : ['defending_marking_awareness', 'defending_standing_tackle', 'defending_sliding_tackle']
}
attr_cat_list = list(cat_dict.keys())
attr_cat_list = [attr_cat.upper() for attr_cat in attr_cat_list]
year_list = ['2023', '2022', '2021', '2020', '2019', '2018']
comp_set_list = ['nationality','league','club','position']
comp_set_list = [comp_set.upper() for comp_set in comp_set_list]


dash.register_page(__name__, path='/', name='STAT PAGE')
layout = html.Div(
    className='playerPage-content',
    children=[
        html.Div(
        className='playerPage-sidebar-content',
        children=[
            html.Div(
            className='playerPage-sidebar',
            children=[
                
                html.Div(
                className='dropDown', children=[
                    dcc.Dropdown(
                        options=complete_player_list,
                        id='all-player-search',
                        placeholder='ENTER NAME',
                        disabled=False,
                        maxHeight=100,
                        optionHeight=20,
                    )
                ]),
                html.Hr(style={'margin': '0.75rem 0rem'}),
                html.Div(
                className='dropDown', children=[
                    dcc.Dropdown(
                        league_options,
                        id='league-dropdown',
                        placeholder='ENTER LEAGUE',
                        disabled=True,
                        maxHeight=100,
                        optionHeight=20,
                    ),
                ]),
                html.Div(
                className='dropDown', children=[
                    dcc.Dropdown(
                        options=[],
                        id='team-dropdown',
                        placeholder='ENTER TEAM',
                        disabled=True,
                        maxHeight=100,
                        optionHeight=20,
                    ),
                ]),
                html.Div(
                className='dropDown', children=[
                    dcc.Dropdown(
                        options=[],
                        id='player-dropdown',
                        placeholder='ENTER PLAYER',
                        disabled=True,
                        maxHeight=100,
                        optionHeight=20,
                    ),
                ]),
                html.Hr(style={'margin': '0.75rem 0rem'}),
                html.Div(
                className='radioItems',
                children=[
                    html.P('SEARCH : ', style={'width': 'fit-content', 'margin-right': '0.5rem', 'margin-bottom': '0'}),
                    dcc.RadioItems(
                    id='radioOptions',
                    options=['NAME', 'TEAM'], value='NAME', inline=True), 
                ]),
                # html.P(' ')
                
            ]),
        ]),
        html.Div(
        className='playerPage-section-1', id='playerPage-section-1',
        children=[
            html.Div(
            className='nameTag',
            children=[
                html.Div(
                id='playerFace-div',
                children=[
                    html.Img(id='playerFace'),
                ]),
                html.Div(
                id='playerNameTag',
                children=[])
            ]),
            html.Hr(style={
              'margin': '0.5rem',
              'marginTop': '0rem',
              'width': '100%',
            }),
            html.Div(
            className='generalInfo',
            children=[
                html.Div(
                id='generalInfoDiv',
                children=[]),
                html.Div(
                id='pitch-pos',
                children=[
                  html.Img(id='pitch-image', src='assets/temp-pitch.png')
                ]),
            ]),
            html.Hr(style={
              'margin': '0.5rem',
              'marginBottom': '0rem',
              'width': '100%',
            }),
            html.Div(
            id='stats-1',
            children=[
                  
            ])
        ]),
        html.Div(
            id='playerPage-section-2', className='playerPage-section-2',
            children=[
                html.Div(
                    id='plot-type-selector',
                    children=[
                      html.Div(
                      className='radioItems-plot',
                      children=[
                          html.P('SELECT BY: ', style={'margin':"0.5rem 1rem", 'marginRight': '0rem'}),
                          dcc.RadioItems(
                          id='radio-plot-options', style={'margin':"0.5rem 1rem"},
                          options=['GROWTH', 'COMPARE'], value='GROWTH', inline=True),
                      ]),
                      html.Div(
                      className='plot-type-dropdowns',
                      children=[
                          html.Div([dcc.Dropdown(
                              attr_cat_list,
                              id='attr-cat-dropdown-1',
                              placeholder='ATTR CATEGORY',
                              maxHeight=120,
                              optionHeight=20,
                              # value=attr_cat_list[0]
                          )], 
                          id='plot-dropdown-div',
                          style={'width': '37.5%', 'height': 'fit-content'}),
                          html.Div([dcc.Dropdown(
                              comp_set_list,
                              id='attr-cat-dropdown-2',
                              placeholder='COMPARISON SET',
                              maxHeight=120,
                              optionHeight=20,
                          )],
                          id='plot-dropdown-div',
                          style={'width': '40%', 'height': 'fit-content'}),
                          html.Div([dcc.Dropdown(
                              options=[],
                              id='attr-cat-dropdown-3',
                              placeholder='YEAR',
                              maxHeight=120,
                              optionHeight=20,
                          )],
                          id='plot-dropdown-div',
                          style={'width': '25%', 'height': 'fit-content'}),
                      ]),
                ]),
                html.Div(
                id='viz-container-1',
                children=[
                    # html.Div(id='growth-attr-selector')
                    html.Div(
                    className='plot-carousel-div',
                    id='plot-carousel-div',
                    children=[
                        html.Div(
                        id='previous-button-div',
                        children=[
                            html.Img(
                                id='previous-button-svg',
                                src='../assets/svg/arrow-left.svg',
                                n_clicks=0,
                                width='30rem',
                            )
                        ]),
                        html.Div(
                        id='plot-outer-div',
                        children=[
                            html.Div(
                            id='plot-container',
                            children=[
                                # html.P(id='sample-text-1'),
                                # html.P(id='sample-text-2'),
                                # dcc.Loading(id='graph-div', type="default")
                            ]),
                        ]),
                        html.Div(
                        id='next-button-div',
                        children=[
                            html.Img(
                                id='next-button-svg',
                                src='../assets/svg/arrow-right.svg',
                                n_clicks=0,
                                width='30rem',
                            )
                        ]),
                    ]),
                ]),
                html.Div(
                id='viz-container-2',
                children=[
                    html.H6('PERCENTILES', style={
                        'transform':'rotate(-90deg)',
                        'margin': '0rem',
                        'marginRight': '-2rem',
                        'marginLeft': '-2rem',
                        'width': 'fit-content',
                        'height': 'fit-content',
                    }),
                    html.Div(
                    id='top-stats-container',
                    children=[

                    ]),
                    html.Div(
                    id='buttons-container',
                    children=[
                        html.Div(
                        id='percentile-buttons-1',
                        children=[
                            html.Button('TOP-5', id='button-1', n_clicks=0),
                            html.Button('ATTACKING', id='button-2', n_clicks=0),
                            html.Button('SKILL', id='button-3', n_clicks=0),
                            html.Button('MOVEMENT', id='button-4', n_clicks=0),
                        ]),
                        html.Div(
                        id='percentile-buttons-2',
                        children=[
                            html.Button('POWER', id='button-5', n_clicks=0),
                            html.Button('MENTALITY', id='button-6', n_clicks=0),
                            html.Button('DEFENDING', id='button-7', n_clicks=0),
                            html.Button('WORST-5', id='button-8', n_clicks=0),
                        ]),
                    ])
                ])
            ]
        ),
])