import pandas as pd
from dash import Dash, dcc, html, Input, Output, dash_table, ctx
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output
from pitch_plot import player_pos_map
from radar_plot import radar_plot
from tables import get_info_table, get_top_5_table, get_stats_table
from player_growth import get_growth_plot_1, get_growth_plot_2, get_growth
from get_top_percentile import get_percentile
from comparison import get_comparisons
import dash_bootstrap_components as dbc

markdown_tab_1 = open('assets/markdown_files/about-tab-1.txt', 'r').read()
markdown_tab_2 = open('assets/markdown_files/case-study.txt', 'r').read()

df = pd.read_csv('new_data/m_23.csv')
s_name = ''
first_plot = True
comp_plot_number = 0

def get_sname(name1, name1_):
  global s_name
  if name1 is None and name1_ is None:
    return None
  else:
    if name1 is not None: s_name = name1
    elif name1_ is not None: s_name = name1_
    return s_name

def get_dropdown_options(df):
  all_ = {}
  league_ = {}
  league_list = list(df['league_name'].unique())
  for league in league_list:
    league_df = df[df['league_name']==league]
    team_list = list(league_df['club_name'].unique())
    team_ = {}
    for team in team_list:
      team_df = league_df[league_df['club_name']==team]
      player_list = list(team_df['short_name'])
      team_[team] = player_list
      league_[league] = team_
      all_['leagues'] = league_
  return all_

def get_dataframe(name):
    df_player = df[df['short_name']==name].head(1)
    p_id = df_player['sofifa_id'].values[0]
    player = df[df['sofifa_id']==p_id]
    return player

data = get_dropdown_options(df)

def get_callbacks(app):

    # player-sidebar
    # --------------------------------------------------------------- #
    
    @app.callback(
            Output('all-player-search', 'disabled'),
            Output('league-dropdown', 'disabled'),
            Output('team-dropdown', 'disabled'),
            Output('player-dropdown', 'disabled'),
            Input('radioOptions', 'value')
    )
    def set_search_type(val):
        if val=='NAME':
            return False, True, True, True
        else:
            return True, False, False, False

    @app.callback(
        Output('all-player-search', 'value'),
        Input('all-player-search', 'disabled'),
    )
    def remove_disabled_values(is_disabled):
      if is_disabled is True: return None
      raise PreventUpdate
    
    @app.callback(
        Output('league-dropdown', 'value'),
        Output('team-dropdown', 'value'),
        Output('player-dropdown', 'value'),
        Input('all-player-search', 'disabled'),
    )
    def remove_disabled_values(is_disabled):
      if is_disabled is False: return None, None, None
      raise PreventUpdate
    
    @app.callback(
        Output('team-dropdown', 'options'),
        Input('league-dropdown', 'value')
    )
    def set_team_options(selected_league):
        league_df = df[df['league_name']==selected_league]
        team_list = league_df['club_name'].unique()
        return [{'label': i, 'value': i} for i in team_list]
    
    @app.callback(
        Output('player-dropdown', 'options'),
        Input('team-dropdown', 'value'),
    )
    def set_player_options(selected_team):
        team_df = df[df['club_name']==selected_team]
        player_list = team_df['short_name'].unique()
        return [{'label': i, 'value': i} for i in player_list]
    
    # about-sidebar
    # --------------------------------------------------------------- #
    @app.callback(
        Output('tab-markdown', 'children'),
        Input('about-radio-options', 'value')
    )
    def display_about_tab_content(tab_option):
      if tab_option == 'About-Tab-1':
        return markdown_tab_1
      if tab_option == 'About-Tab-2':
        return markdown_tab_2
      if tab_option == 'About-Tab-3':
        return '''## About TAB3'''

    # player-section-1
    # --------------------------------------------------------------- #

    @app.callback(
        Output('playerPage-section-1', 'style'),
        Input('player-dropdown', 'value'),
        Input('all-player-search', 'value')
    )
    def display_section_1(drpdown, search):
        if drpdown is None and search is None:
          return {'display': 'None'}
        
    @app.callback(
        Output('playerPage-section-2', 'style'),
        Input('player-dropdown', 'value'),
        Input('all-player-search', 'value')
    )
    def display_section_2(drpdown, search):
        if drpdown is None and search is None:
          return {'display': 'None'}
    
    @app.callback(
        Output('playerFace', 'src'),
        Input('player-dropdown', 'value'),
        Input('all-player-search', 'value')
    )
    def update_club_logo(drpdown, search):
        get_sname(drpdown, search)
        if len(s_name) > 0:
          player_df = df[df['short_name']==s_name]
          face_url = str((player_df['player_face_url'].values)[0])
          return face_url
        else:
          return 'https://cdn.sofifa.net/teams/111575/60.png'
    
    @app.callback(
        Output('clubLogo', 'src'),
        Input('player-dropdown', 'value'),
        Input('all-player-search', 'value')
    )
    def update_club_logo(drpdown, search):
        get_sname(drpdown, search)
        if len(s_name) > 0:
          player_df = df[df['short_name']==s_name]
          logo_url = str((player_df['club_logo_url'].values)[0])
          return logo_url
        else:
          return 'https://cdn.sofifa.net/teams/111575/60.png'
            
    @app.callback(
        Output('playerNameTag', 'children'),
        Input('all-player-search', 'value'),
        Input('player-dropdown', 'value')
    )
    def display_player_name(name1, name1_):
      get_sname(name1, name1_)
      if len(s_name) > 0:
        df_ = get_dataframe(s_name)
        name = str((df_['short_name'].values)[0])
        num = int((df_['club_jersey_number'].values)[0])
        num = str(num).zfill(2)
        team = str((df_['club_name'].values)[0])
        return html.Div(
            id='playerNameBox',
            children=[
            html.Div(
            className='numAndName',
            children=[
                html.P(num+' |', style={'paddingRight': '0.5rem', 'width': 'fit-content'}),
                html.P(name.upper(), id='playerNameP'),
            ]),
            html.Hr(style={'margin': '0'}),
            html.Div(
            className='clubLogoName',
            children=[
              html.Div(
                id='clubLogo-div',
                children=[
                    html.Img(id='clubLogo'),
              ]),
              html.P(team.upper(), style={'fontSize': '1.5rem','margin':'0.25rem', 'marginTop': '0.25rem'}),
            ]),
        ])
        
    @app.callback(
        Output('generalInfoDiv', 'children'),
        Input('all-player-search', 'value'),
        Input('player-dropdown', 'value')
    )
    def display_player_name(name1, name1_):
        get_sname(name1, name1_)
        if len(s_name) > 0:
          df_ = get_dataframe(s_name)
          df_info = get_info_table(s_name)
          return html.Div(
          className='generalInfoCall',
          children=[
              dash_table.DataTable(
                id='info-table',
                data = df_info.to_dict('records'),
                columns=[{'id': c, 'name': c} for c in df_info.columns],
                style_header={
                  'display': 'None',
                  'height': '0px',
                },
                style_cell={
                  'textAlign': 'left',
                  'padding': '0px 0.5rem',
                },
                style_data={
                  'backgroundColor': '#000',
                  'height': 'auto',
                },
                style_as_list_view=False,
              ),
          ])
    
    @app.callback(
        Output('pitch-image', 'src'),
        Input('all-player-search', 'value'),
        Input('player-dropdown', 'value')
    )
    def display_pitch(name1, name1_):
        get_sname(name1, name1_)
        if len(s_name) > 0:
          df_ = get_dataframe(s_name)
          player_positions = str(list(df_['player_positions'].values)[0])
          src = player_pos_map(player_positions)
          return src
      
    @app.callback(
        Output('attr-cat-dropdown-1', 'disabled'),
        Output('attr-cat-dropdown-2', 'disabled'),
        Output('attr-cat-dropdown-3', 'disabled'),
        Input('radio-plot-options', 'value')
    )
    def disable_plot_dropdowns(value):
       if value=='GROWTH': 
          return False, True, True
       elif value=='COMPARE': 
          return True, False, False
       
    @app.callback(
        Output('attr-cat-dropdown-1', 'value'),
        Input('attr-cat-dropdown-1', 'disabled'),
    )
    def remove_disabled_values(is_disabled):
      if is_disabled is True: return None
      raise PreventUpdate
    
    @app.callback(
        Output('attr-cat-dropdown-2', 'value'),
        Output('attr-cat-dropdown-3', 'value'),
        Input('attr-cat-dropdown-1', 'disabled'),
    )
    def remove_disabled_values(is_disabled):
      if is_disabled is False: return None, None
      raise PreventUpdate
      
    @app.callback(
          Output('attr-cat-dropdown-3', 'options'),
          Input('all-player-search', 'value'),
          Input('player-dropdown', 'value')
    )
    def update_year_list(name1, name1_):
      s_name = get_sname(name1, name1_)
      year_list = list(get_growth(s_name)['Year'].values)
      return year_list[::-1]
    
    @app.callback(
          Output('plot-container', 'children'),
          Input('radio-plot-options', 'value'),
          Input('attr-cat-dropdown-1', 'value'),
          Input('attr-cat-dropdown-2', 'value'),
          Input('attr-cat-dropdown-3', 'value'),
          Input('previous-button-svg', 'n_clicks'),
          Input('next-button-svg', 'n_clicks'),    
    )
    def update_plot_div(plot_type, attr_cat, set_type, year, n1, n2):
      global first_plot
      global comp_plot_number
      if plot_type == 'GROWTH':
        if attr_cat is not None:
          attr_cat = attr_cat.lower()
          button_id = ctx.triggered_id
          if button_id == 'next-button-svg':
            if first_plot == True: first_plot = False
            elif first_plot == False: first_plot = True
          elif button_id == 'previous-button-svg':
            if first_plot == True: first_plot = False
            elif first_plot == False: first_plot = True
          if first_plot == True: 
            fig = get_growth_plot_1(s_name, attr_cat)
          elif first_plot == False: 
            fig = get_growth_plot_2(s_name, attr_cat)
          return dcc.Graph(figure=fig)
        else:
          return html.Div(
            id='placeholder-plot-div',
            children=[html.P('SELECT ATTRIBUTE CATEGORY ABOVE')]
          )
      elif plot_type == 'COMPARE':
        if (set_type is not None) and (year is not None):
          set_type = set_type.lower()
          button_id = ctx.triggered_id
          if button_id == 'next-button-svg':
            if comp_plot_number == 4:
              comp_plot_number = 0
            else: 
              comp_plot_number += 1
          elif button_id == 'previous-button-svg':
            if comp_plot_number == 0:
              comp_plot_number = 4
            else: 
              comp_plot_number -= 1
          plot_list = get_comparisons(s_name, set_type, year)
          fig = plot_list[comp_plot_number]
          return dcc.Graph(figure=fig)
        else:
          return html.Div(
            id='placeholder-plot-div',
            children=[html.P('SELECT COMPARISON SET AND YEAR ABOVE')]
          )
        
    def get_value_color(val):
      col = ''
      colors = ['#03aeae', '#019598', '#00686c', '#004a51', '#013e43']
      if val >= 90: col = colors[0]
      elif val >= 80 and val < 90: col = colors[1]
      elif val >= 70 and val < 80: col = colors[2]
      elif val >= 50 and val < 70: col = colors[3]
      elif val < 50: col = colors[4]
      # elif val > 0 and val <= 30: col = colors[5]
      return col
      
    def createProgressbar(perc_dict):
      if perc_dict is not None:
        return  dbc.Container([
                    dbc.Row([
                        dbc.Col([
                            dbc.Progress(
                              value=v,
                              label=str(v)+'%',
                              className='dbc-progress-bar',
                              color=get_value_color(v),
                            ),
                            html.P(k, id='dbc-progress-text')
                        ]),
                    ]) for k, v in perc_dict.items()
                ]) 

    def get_attribute_cat(button_id):
      if button_id == 'button-1': return 'top-5'
      elif button_id == 'button-2': return 'attacking'
      elif button_id == 'button-3': return 'skill'
      elif button_id == 'button-4': return 'movement'
      elif button_id == 'button-5': return 'power'
      elif button_id == 'button-6': return 'mentality'
      elif button_id == 'button-7': return 'defending'
      elif button_id == 'button-8': return 'worst-5'
      else: return None
    
    @app.callback(
        Output('top-stats-container', 'children'),
        Input('all-player-search', 'value'),
        Input('player-dropdown', 'value'),
        Input('button-1', 'n_clicks'),
        Input('button-2', 'n_clicks'),
        Input('button-3', 'n_clicks'),
        Input('button-4', 'n_clicks'),
        Input('button-5', 'n_clicks'),
        Input('button-6', 'n_clicks'),
        Input('button-7', 'n_clicks'),
        Input('button-8', 'n_clicks'),
    )
    def p(name1, name1_, n1, n2, n3, n4, n5, n6, n7, n8):
        s_name = get_sname(name1, name1_)
        if s_name is not None:
          button_id = ctx.triggered_id
          attr_type = get_attribute_cat(button_id)
          if attr_type is not None:
            df_perc = get_percentile(s_name, attr_type)
            attributes = list(df_perc['Attribute'].values)
            percentiles = list(df_perc['Percentile'].values)
            # print(attributes)
            # print(percentiles)
            perc_dict = {}
            for i in range(len(attributes)):
              perc_dict[attributes[i]] = percentiles[i]
            return createProgressbar(perc_dict)
          else:
            return html.Div(
              id='placeholder-percentile',
              children=[
                html.H6('SELECT ATTRIBUTE CATEGORY')
            ])
      
    @app.callback(
        Output('button-1', 'style'),
        Output('button-2', 'style'),
        Output('button-3', 'style'),
        Output('button-4', 'style'),
        Output('button-5', 'style'),
        Output('button-6', 'style'),
        Output('button-7', 'style'),
        Output('button-8', 'style'),
        Input('all-player-search', 'value'),
        Input('player-dropdown', 'value'),
        Input('button-1', 'n_clicks'),
        Input('button-2', 'n_clicks'),
        Input('button-3', 'n_clicks'),
        Input('button-4', 'n_clicks'),
        Input('button-5', 'n_clicks'),
        Input('button-6', 'n_clicks'),
        Input('button-7', 'n_clicks'),
        Input('button-8', 'n_clicks'),
    )
    def update_button_style(name1, name1_, n1, n2, n3, n4, n5, n6, n7, n8):
        s_name = get_sname(name1, name1_)
        res = [{'background-color': '#232323'}]*8
        if s_name is not None:
          button_id = ctx.triggered_id
          attr_type = get_attribute_cat(button_id)
          if attr_type is not None:
            if button_id is not None:
              button_num = int(str(button_id).split('-')[1])
              res[button_num-1] = {
                'background-color': 'black',
                'color': '#13FFFF'
              }
        return res

    @app.callback(
        Output('stats-1', 'children'),
        Input('all-player-search', 'value'),
        Input('player-dropdown', 'value')
    )
    def display_player_name(name1, name1_):
        s_name = get_sname(name1, name1_)
        if s_name is not None:
          fig = radar_plot(s_name)
          df_top_5 = get_top_5_table(s_name)
          df_stats = get_stats_table(s_name)
          df_stats_1 = df_stats[:5]
          df_stats_2 = df_stats[5:10]
          df_stats_3 = df_stats[10:15]
          df_stats_4 = df_stats[15:20]
          df_stats_5 = df_stats[20:25]
          df_stats_6 = df_stats[25:]
          return html.Div(
             children=[
              html.Div(id='stats-box-1', children=[
                dcc.Tabs(id='tabs-1', value='tab-1', children=[
                  dcc.Tab(label='Tab-1', value='tab-1', children=[
                    html.Div(id='tab-1-content', children=[
                      dcc.Graph(
                        id='radar-plot',
                        figure=fig,
                        config={
                          'displayModeBar': False,
                          'displaylogo': False,
                        }
                      ),
                      dash_table.DataTable(
                        id='info-table',
                        data = df_top_5.to_dict('records'),
                        columns=[{'id': c, 'name': c} for c in df_top_5.columns],
                        style_header={
                          'display': 'None',
                          'height': '0px',
                        },
                        style_cell={
                          'textAlign': 'left',
                          'padding': '0px 1rem',
                        },
                        style_data={
                          'backgroundColor': '#000',
                          'height': 'auto',
                        },
                        style_data_conditional=[
                        {
                          'if': {
                            'filter_query': '{Stat} >= 90',
                            'column_id': 'Stat',
                          },
                          'color': 'white',
                          'backgroundColor': '#105902',
                        },
                        {
                          'if': {
                            'filter_query': '{Stat} >= 80 && {Stat} < 90',
                            'column_id': 'Stat',
                          },
                          'color': 'white',
                          'backgroundColor': '#0ba11a',
                        },
                        {
                          'if': {
                            'filter_query': '{Stat} >= 70 && {Stat} < 80',
                            'column_id': 'Stat',
                          },
                          'color': 'white',
                          'backgroundColor': '#64ad23',
                        },
                        {
                          'if': {
                            'filter_query': '{Stat} >= 50 && {Stat} < 70',
                            'column_id': 'Stat',
                          },
                          'color': 'white',
                          'backgroundColor': '#baa30f',
                        },
                        {
                          'if': {
                            'filter_query': '{Stat} < 50',
                            'column_id': 'Stat',
                          },
                          'color': 'white',
                          'backgroundColor': '#c73214',
                        },
                        ],
                        style_as_list_view=False,
                      ),
                    ])
                  ], className='custom-Tab', selected_className='custom-Tab--selected'),
                  dcc.Tab(label='Tab-2', value='tab-2', children=[
                    html.Div(id='tab-2-content',children=[
                      dash_table.DataTable(
                        id='info-table',
                        data = df_stats_1.to_dict('records'),
                        columns=[{'id': c, 'name': c} for c in df_stats_1.columns],
                        style_header={
                          'display': 'None',
                          'height': '0px',
                        },
                        style_cell={
                          'textAlign': 'left',
                          'padding': '0px 1rem',
                        },
                        style_data={
                          'backgroundColor': '#000',
                          'height': 'auto',
                        },
                        style_data_conditional=[
                        {
                          'if': {
                            'filter_query': '{Stat} >= 90',
                            'column_id': 'Stat',
                          },
                          'color': 'white',
                          'backgroundColor': '#105902',
                        },
                        {
                          'if': {
                            'filter_query': '{Stat} >= 80 && {Stat} < 90',
                            'column_id': 'Stat',
                          },
                          'color': 'white',
                          'backgroundColor': '#0ba11a',
                        },
                        {
                          'if': {
                            'filter_query': '{Stat} >= 70 && {Stat} < 80',
                            'column_id': 'Stat',
                          },
                          'color': 'white',
                          'backgroundColor': '#64ad23',
                        },
                        {
                          'if': {
                            'filter_query': '{Stat} >= 50 && {Stat} < 70',
                            'column_id': 'Stat',
                          },
                          'color': 'white',
                          'backgroundColor': '#baa30f',
                        },
                        {
                          'if': {
                            'filter_query': '{Stat} < 50',
                            'column_id': 'Stat',
                          },
                          'color': 'white',
                          'backgroundColor': '#c73214',
                        },
                        ],
                        style_as_list_view=False,
                      ),
                      dash_table.DataTable(
                        id='info-table',
                        data = df_stats_2.to_dict('records'),
                        columns=[{'id': c, 'name': c} for c in df_stats_2.columns],
                        style_header={
                          'display': 'None',
                          'height': '0px',
                        },
                        style_cell={
                          'textAlign': 'left',
                          'padding': '0px 1rem',
                        },
                        style_data={
                          'backgroundColor': '#000',
                          'height': 'auto',
                        },
                        style_data_conditional=[
                        {
                          'if': {
                            'filter_query': '{Stat} >= 90',
                            'column_id': 'Stat',
                          },
                          'color': 'white',
                          'backgroundColor': '#105902',
                        },
                        {
                          'if': {
                            'filter_query': '{Stat} >= 80 && {Stat} < 90',
                            'column_id': 'Stat',
                          },
                          'color': 'white',
                          'backgroundColor': '#0ba11a',
                        },
                        {
                          'if': {
                            'filter_query': '{Stat} >= 70 && {Stat} < 80',
                            'column_id': 'Stat',
                          },
                          'color': 'white',
                          'backgroundColor': '#64ad23',
                        },
                        {
                          'if': {
                            'filter_query': '{Stat} >= 50 && {Stat} < 70',
                            'column_id': 'Stat',
                          },
                          'color': 'white',
                          'backgroundColor': '#baa30f',
                        },
                        {
                          'if': {
                            'filter_query': '{Stat} < 50',
                            'column_id': 'Stat',
                          },
                          'color': 'white',
                          'backgroundColor': '#c73214',
                        },
                        ],
                        style_as_list_view=False,
                      ),
                    ])
                  ], className='custom-Tab', selected_className='custom-Tab--selected'),
                  dcc.Tab(label='Tab-3', value='tab-3', children=[
                    html.Div(id='tab-3-content', children=[
                    dash_table.DataTable(
                      id='info-table',
                      data = df_stats_3.to_dict('records'),
                      columns=[{'id': c, 'name': c} for c in df_stats_3.columns],
                      style_header={
                        'display': 'None',
                        'height': '0px',
                      },
                      style_cell={
                        'textAlign': 'left',
                        'padding': '0px 1rem',
                      },
                      style_data={
                        'backgroundColor': '#000',
                        'height': 'auto',
                      },
                      style_data_conditional=[
                      {
                        'if': {
                          'filter_query': '{Stat} >= 90',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#105902',
                      },
                      {
                        'if': {
                          'filter_query': '{Stat} >= 80 && {Stat} < 90',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#0ba11a',
                      },
                      {
                        'if': {
                          'filter_query': '{Stat} >= 70 && {Stat} < 80',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#64ad23',
                      },
                      {
                        'if': {
                          'filter_query': '{Stat} >= 50 && {Stat} < 70',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#baa30f',
                      },
                      {
                        'if': {
                          'filter_query': '{Stat} < 50',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#c73214',
                      },
                      ],
                      style_as_list_view=False,
                    ),
                    dash_table.DataTable(
                      id='info-table',
                      data = df_stats_4.to_dict('records'),
                      columns=[{'id': c, 'name': c} for c in df_stats_4.columns],
                      style_header={
                        'display': 'None',
                        'height': '0px',
                      },
                      style_cell={
                        'textAlign': 'left',
                        'padding': '0px 1rem',
                      },
                      style_data={
                        'backgroundColor': '#000',
                        'height': 'auto',
                      },
                      style_data_conditional=[
                      {
                        'if': {
                          'filter_query': '{Stat} >= 90',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#105902',
                      },
                      {
                        'if': {
                          'filter_query': '{Stat} >= 80 && {Stat} < 90',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#0ba11a',
                      },
                      {
                        'if': {
                          'filter_query': '{Stat} >= 70 && {Stat} < 80',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#64ad23',
                      },
                      {
                        'if': {
                          'filter_query': '{Stat} >= 50 && {Stat} < 70',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#baa30f',
                      },
                      {
                        'if': {
                          'filter_query': '{Stat} < 50',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#c73214',
                      },
                      ],
                      style_as_list_view=False,
                    )
                  ])
                  ], className='custom-Tab', selected_className='custom-Tab--selected'),
                  dcc.Tab(label='Tab-4', value='tab-4', children=[
                    html.Div(id='tab-4-content', children=[
                    dash_table.DataTable(
                      id='info-table',
                      data = df_stats_5.to_dict('records'),
                      columns=[{'id': c, 'name': c} for c in df_stats_5.columns],
                      style_header={
                        'display': 'None',
                        'height': '0px',
                      },
                      style_cell={
                        'textAlign': 'left',
                        'padding': '0px 1rem',
                      },
                      style_data={
                        'backgroundColor': '#000',
                        'height': 'auto',
                      },
                      style_data_conditional=[
                      {
                        'if': {
                          'filter_query': '{Stat} >= 90',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#105902',
                      },
                      {
                        'if': {
                          'filter_query': '{Stat} >= 80 && {Stat} < 90',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#0ba11a',
                      },
                      {
                        'if': {
                          'filter_query': '{Stat} >= 70 && {Stat} < 80',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#64ad23',
                      },
                      {
                        'if': {
                          'filter_query': '{Stat} >= 50 && {Stat} < 70',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#baa30f',
                      },
                      {
                        'if': {
                          'filter_query': '{Stat} < 50',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#c73214',
                      },
                      ],
                      style_as_list_view=False,
                    ),
                    dash_table.DataTable(
                      id='info-table',
                      data = df_stats_6.to_dict('records'),
                      columns=[{'id': c, 'name': c} for c in df_stats_6.columns],
                      style_header={
                        'display': 'None',
                        'height': '0px',
                      },
                      style_cell={
                        'textAlign': 'left',
                        'padding': '0px 1rem',
                      },
                      style_data={
                        'backgroundColor': '#000',
                        'height': 'auto',
                      },
                      style_data_conditional=[
                      {
                        'if': {
                          'filter_query': '{Stat} >= 90',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#105902',
                      },
                      {
                        'if': {
                          'filter_query': '{Stat} >= 80 && {Stat} < 90',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#0ba11a',
                      },
                      {
                        'if': {
                          'filter_query': '{Stat} >= 70 && {Stat} < 80',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#64ad23',
                      },
                      {
                        'if': {
                          'filter_query': '{Stat} >= 50 && {Stat} < 70',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#baa30f',
                      },
                      {
                        'if': {
                          'filter_query': '{Stat} < 50',
                          'column_id': 'Stat',
                        },
                        'color': 'white',
                        'backgroundColor': '#c73214',
                      },
                      ],
                      style_as_list_view=False,
                    ),])
                  ], className='custom-Tab', selected_className='custom-Tab--selected'),
                ], parent_className='custom-tabs', className='custom-tabs-container',),
              ]),
             ]
          )
