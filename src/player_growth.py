import pandas as pd
import plotly.express as px
pd.options.mode.chained_assignment = None

def update_dtypes(df):
    f_columns = list(df.select_dtypes(include='float64'))
    for col in f_columns:
      df[col] = df[col].astype(int)
    return df

def define_attr():
    columns = ['sofifa_id', 'short_name', 'player_positions', 'overall', 'age',
       'height_cm', 'weight_kg', 'club_name', 'league_name', 'club_position',
       'club_jersey_number', 'nationality_name', 'preferred_foot', 'weak_foot',
       'skill_moves', 'pace', 'shooting', 'passing', 'dribbling', 'defending',
       'physic', 'attacking_crossing', 'attacking_finishing',
       'attacking_heading_accuracy', 'attacking_short_passing',
       'attacking_volleys', 'skill_dribbling', 'skill_curve',
       'skill_fk_accuracy', 'skill_long_passing', 'skill_ball_control',
       'movement_acceleration', 'movement_sprint_speed', 'movement_agility',
       'movement_reactions', 'movement_balance', 'power_shot_power',
       'power_jumping', 'power_stamina', 'power_strength', 'power_long_shots',
       'mentality_aggression', 'mentality_interceptions',
       'mentality_positioning', 'mentality_vision', 'mentality_penalties',
       'mentality_composure', 'defending_marking_awareness',
       'defending_standing_tackle', 'defending_sliding_tackle',
       'goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking',
       'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed',
       'club_logo_url', 'RW', 'ST', 'CF', 'LW', 'CAM', 'CM', 'GK', 'CDM', 'LM',
       'CB', 'RB', 'RM', 'LB', 'RWB', 'LWB']
    return columns

def define_list_df():
    m_23 = pd.read_csv('new_data/m_23.csv', index_col=[0])
    m_22 = pd.read_csv('new_data/growth/m_22.csv', index_col=[0])
    m_21 = pd.read_csv('new_data/growth/m_21.csv', index_col=[0])
    m_20 = pd.read_csv('new_data/growth/m_20.csv', index_col=[0])
    m_19 = pd.read_csv('new_data/growth/m_19.csv', index_col=[0])
    m_18 = pd.read_csv('new_data/growth/m_18.csv', index_col=[0])
    df_l = [m_23, m_22, m_21, m_20, m_19, m_18]
    return df_l

def get_growth(s_name):
    attrs = define_attr()
    df_l = define_list_df()
    years = ['2023', '2022', '2021', '2020', '2019', '2018']
    growth = pd.DataFrame({'Year':years})
    for at in attrs:
        attr_values = []
        for df in df_l:
            sub_df = df[df['short_name']==s_name]
            if sub_df.shape[0] > 0:
              val = list(df[df['short_name']==s_name][at].values)[0]
            else:
              val = None
            attr_values.append(val)
        growth[at] = attr_values
    growth = growth[growth['overall'].notna()]
    growth = update_dtypes(growth)
    growth.sort_values(by=['Year'], inplace=True)
    growth.to_csv('new_data/growth/temp-growth.csv')
    return growth

def define_growth_cat(attr_cat):
  cat_dict = {
    'general' : ['pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic'],
    'attacking' : ['attacking_crossing', 'attacking_finishing', 'attacking_heading_accuracy', 'attacking_short_passing', 'attacking_volleys'],
    'skill': ['skill_dribbling', 'skill_curve', 'skill_fk_accuracy', 'skill_long_passing', 'skill_ball_control'],
    'movement': ['movement_acceleration', 'movement_sprint_speed', 'movement_agility', 'movement_reactions', 'movement_balance'],
    'power' : ['power_shot_power', 'power_jumping', 'power_stamina', 'power_strength', 'power_long_shots'],
    'mentality' : ['mentality_aggression', 'mentality_interceptions', 'mentality_positioning', 'mentality_vision', 'mentality_penalties', 'mentality_composure'],
    'defending' : ['defending_marking_awareness', 'defending_standing_tackle', 'defending_sliding_tackle']
  }
  categories = cat_dict[attr_cat]
  return categories

def rename_attributes(categories):
    x_list = []
    for cat in categories:
        parts = cat.split('_')
        if len(parts) > 1:
          parts = parts[1:]
        x_list.append('_'.join(parts))
    return x_list

def plot_graph(growth, categories):
  import plotly.graph_objects as go
  fig = go.Figure()
  colors = ["#13FFFF", "#00CACB", "#00989A", "#00686B", "#00555D", "#00474D"]
  min_range = min(list(growth[categories].min(axis='columns'))) - 10
  max_range = max(list(growth[categories].max(axis='columns'))) + 15
  if max_range>100: max_range=100
  data = growth[categories].T
  x_list = rename_attributes(categories)
  colors = colors[:len(growth)]
  for i in range(len(growth)):
      fig.add_trace(go.Bar(
          x=x_list,
          y=list(data[len(growth)-i-1]),
          name=str(growth['Year'][len(growth)-i-1]),
          marker_color=colors[-(i+1)],
      ))

  fig.update_layout(
      template='plotly_dark',
      title={
        'text': 'Attribute Growth Over the Years',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
      },
      yaxis_range=[min_range, max_range],
      width=675,
      height=400,
      paper_bgcolor='rgba(0,0,0,0)',
      plot_bgcolor='rgba(0,0,0,0)'
  )
  return fig

def get_growth_plot_1(s_name, attr_cat):
    growth = get_growth(s_name)
    if (list(growth['player_positions'].values)[0]=='GK') and (attr_cat=='general'):
      categories = ['goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking', 'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed']
    else:
      categories = define_growth_cat(attr_cat)
    fig = plot_graph(growth, categories)
    return fig

def get_growth_plot_2(s_name, attr_cat):
    growth = get_growth(s_name)
    if (list(growth['player_positions'].values)[0]=='GK') and (attr_cat=='general'):
      categories = ['goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking', 'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed']
    else:
      categories = define_growth_cat(attr_cat)
    growth_selected = growth[categories]
    growth_selected['Year'] = growth['Year']
    growth_selected.set_index('Year', inplace=True)
    categories = list(growth_selected.columns.values) 
    x_list = rename_attributes(categories)
    col_rename_dict = {i:j for i,j in zip(categories,x_list)}
    growth_selected.rename(columns=col_rename_dict, inplace=True)
    colors = ["#13FFFF", "#00CACB", "#00989A", "#00686B", "#00555D", "#00474D"]
    fig = px.imshow(
        growth_selected.T,
        aspect='auto',
        color_continuous_scale=colors)
    fig.update_layout(
        template='plotly_dark',
        title={
          'text': 'Attribute Growth Over the Years',
          'y':0.9,
          'x':0.5,
          'xanchor': 'center',
          'yanchor': 'top'
        },
        height=400,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )
    return fig
