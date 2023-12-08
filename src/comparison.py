import os
import pandas as pd
from player_growth import define_list_df

def define_player_type(player_pos):
    midfielder = ['CM', 'CAM', 'CDM']
    forward = ['ST', 'CF']
    winger = ['LW', 'LM', 'RW', 'RM']
    fullwingback = ['LWB', 'LB', 'RWB', 'RB']
    centerback = ['CB']
    keeper = ['GK']
    if player_pos in midfielder: player_type = 'midfielder'
    if player_pos in forward: player_type = 'forward'
    if player_pos in winger: player_type = 'winger'
    if player_pos in fullwingback: player_type = 'fullwingback'
    if player_pos in centerback: player_type = 'centerback'
    if player_pos in keeper: player_type = 'keeper'
    return player_type

def define_plot_combinations():
    plot_combination = {
        'midfielder': {
            0: {
                'x_attr': 'skill_long_passing',
                'y_attr': 'mentality_vision',
                'size_attr': 'attacking_short_passing',
                'title': 'Long Passing vs Vision (w Short Passing)'
            },
            1: {
                'x_attr': 'skill_ball_control',
                'y_attr': 'skill_dribbling',
                'size_attr': 'mentality_composure',
                'title': 'Ball Control vs Dribbling (w Composure)'
            },
            2: {
                'x_attr': 'physic',
                'y_attr': 'power_strength',
                'size_attr': 'movement_balance',
                'title': 'Physicality vs Strength (w Balance)'
            },
            3: {
                'x_attr': 'mentality_interceptions',
                'y_attr': 'defending_marking_awareness',
                'size_attr': 'mentality_positioning',
                'title': 'Interceptions vs Marking Awareness (w Positioning)'
            },
            4: {
                'x_attr': 'power_long_shots',
                'y_attr': 'power_shot_power',
                'size_attr': 'attacking_volleys',
                'title': 'Long Shots vs Shot Power (w Volleys)'
            },
        },
        'forward': {
            0: {
                'x_attr': 'attacking_finishing',
                'y_attr': 'power_shot_power',
                'size_attr': 'skill_curve',
                'title': 'Finishing vs Shot Power (w Curve)'
            },
            1: {
                'x_attr': 'mentality_positioning',
                'y_attr': 'mentality_composure',
                'size_attr': 'movement_reactions',
                'title': 'Positioning vs Composure (w Reactions)'
            },
            2: {
                'x_attr': 'skill_dribbling',
                'y_attr': 'movement_agility',
                'size_attr': 'movement_balance',
                'title': 'Dribbling vs Agility (w Balance)'
            },
            3: {
                'x_attr': 'attacking_heading_accuracy',
                'y_attr': 'power_jumping',
                'size_attr': 'power_strength',
                'title': 'Heading Accuracy vs Jumping (w Strength)'
            },
            4: {
                'x_attr': 'movement_acceleration',
                'y_attr': 'movement_sprint_speed',
                'size_attr': 'mentality_positioning',
                'title': 'Acceleration vs Sprint Speed (w Positioning)'
            },
        },
        'winger': {
            0: {
                'x_attr': 'skill_dribbling',
                'y_attr': 'skill_ball_control',
                'size_attr': 'movement_reactions',
                'title': 'Dribbling vs Ball Control (w Reactions)'
            },
            1: {
                'x_attr': 'movement_sprint_speed',
                'y_attr': 'movement_acceleration',
                'size_attr': 'movement_agility',
                'title': 'Sprint Speed vs Acceleration (w Agility)'
            },
            2: {
                'x_attr': 'attacking_crossing',
                'y_attr': 'skill_curve',
                'size_attr': 'mentality_vision',
                'title': 'Crossing vs Curve (w Vision)'
            },
            3: {
                'x_attr': 'attacking_finishing',
                'y_attr': 'mentality_positioning',
                'size_attr': 'mentality_composure',
                'title': 'Finishing vs Positioning (w Composure)'
            },
            4: {
                'x_attr': 'power_stamina',
                'y_attr': 'movement_sprint_speed',
                'size_attr': 'mentality_positioning',
                'title': 'Stamina vs Sprint Speed (w Positioning)'
            },
        },
        'fullwingback': {
            0: {
                'x_attr': 'movement_sprint_speed',
                'y_attr': 'movement_acceleration',
                'size_attr': 'movement_agility',
                'title': 'Sprint Speed vs Acceleration (w Agility)'
            },
            1: {
                'x_attr': 'defending_marking_awareness',
                'y_attr': 'mentality_interceptions',
                'size_attr': 'movement_reactions',
                'title': 'Marking Awareness vs Interceptions (w Reactions)'
            },
            2: {
                'x_attr': 'attacking_crossing',
                'y_attr': 'power_stamina',
                'size_attr': 'mentality_vision',
                'title': 'Crossing vs Stamina (w Vision)'
            },
            3: {
                'x_attr': 'defending_standing_tackle',
                'y_attr': 'defending_sliding_tackle',
                'size_attr': 'movement_balance',
                'title': 'Standing Tackle vs Sliding Tackle (w Balance)'
            },
            4: {
                'x_attr': 'power_strength',
                'y_attr': 'mentality_aggression',
                'size_attr': 'mentality_composure',
                'title': 'Strength vs Aggression (w Composure)'
            },
        },
        'centerback': {
            0: {
                'x_attr': 'defending_marking_awareness',
                'y_attr': 'defending_standing_tackle',
                'size_attr': 'mentality_aggression',
                'title': 'Marking Awareness vs Standing Tackle (w Aggression)'
            },
            1: {
                'x_attr': 'attacking_heading_accuracy',
                'y_attr': 'power_jumping',
                'size_attr': 'power_strength',
                'title': 'Heading Accuracy vs Jumping (w Strength)'
            },
            2: {
                'x_attr': 'power_strength',
                'y_attr': 'mentality_aggression',
                'size_attr': 'mentality_composure',
                'title': 'Strength vs Aggression (w Composure)'
            },
            3: {
                'x_attr': 'mentality_interceptions',
                'y_attr': 'movement_reactions',
                'size_attr': 'mentality_vision',
                'title': 'Interceptions vs Reactions (w Visions)'
            },
            4: {
                'x_attr': 'mentality_composure',
                'y_attr': 'movement_reactions',
                'size_attr': 'mentality_positioning',
                'title': 'Composure vs Reactions (w Positioning)'
            },
        },
        'keeper': {
            0: {
                'x_attr': 'goalkeeping_diving',
                'y_attr': 'goalkeeping_reflexes',
                'size_attr': 'movement_reactions',
                'title': 'GK Diving vs GK Reflexes (w Reactions)'
            },
            1: {
                'x_attr': 'goalkeeping_handling',
                'y_attr': 'goalkeeping_positioning',
                'size_attr': 'mentality_composure',
                'title': 'GK Handling vs GK Positioning (w Composure)'
            },
            2: {
                'x_attr': 'goalkeeping_kicking',
                'y_attr': 'mentality_vision',
                'size_attr': 'mentality_composure',
                'title': 'GK Kicking vs Vision (w Composure)'
            },
            3: {
                'x_attr': 'goalkeeping_reflexes',
                'y_attr': 'movement_reactions',
                'size_attr': 'goalkeeping_speed',
                'title': 'GK Reflexes vs Reactions (w GK Speed)'
            },
            4: {
                'x_attr': 'power_jumping',
                'y_attr': 'height_cm',
                'size_attr': 'mentality_aggression',
                'title': 'Jumping vs Height (w Aggression)'
            },
        },
    }
    return plot_combination

def get_plots(x_attr, y_attr, size_attr, comparison_set, title, player):
    import plotly.express as px
    import plotly.graph_objects as go
    p_id = player['sofifa_id'].values[0]
    other_players = comparison_set[comparison_set['sofifa_id']!=p_id]
    fig = px.scatter(
        other_players, x=x_attr, y=y_attr,
        hover_data=['short_name'], 
        size=size_attr, size_max=15,
        template='plotly_dark',
        color_discrete_sequence=['#00e5e6'],
    )

    fig.add_trace(
        go.Scatter(
            x=player[x_attr], 
            y=player[y_attr], 
            customdata=[dict(
                x_attr=player[x_attr].name,
                y_attr=player[y_attr].name,
                size_attr=player[size_attr].name
            )],
            text=player['short_name'],
            textposition='top center',
            textfont=dict(color='white'),
            mode='lines+markers+text',
            name='',
            hovertemplate='%{customdata.x_attr}=%{x}<br>'+
                          '%{customdata.y_attr}=%{y}<br>'+
                          '%{customdata.size_attr}=%{marker.size}<br>'+
                          'short_name=%{text}',
            marker_size=player[size_attr],
            marker_sizeref=4,
            marker_color='#FF1313',
        )
    )

    fig.update_traces(showlegend=False)
    fig.update_layout(
      width=675,
      height=400,
      paper_bgcolor='rgba(0,0,0,0)',
      plot_bgcolor='rgba(0,0,0,0)',
      margin=go.layout.Margin(r=20, t=90),
      title={
      'text': title,
      'x': 0.5,
      'y': 0.9,
      'xanchor': 'center',
      'yanchor': 'top',
    })
    return fig

def get_comp_set(player, set_type, total):
    nationality = player['nationality_name'].values[0]
    league = player['league_name'].values[0]
    club = player['club_name'].values[0]
    position = player['player_positions'].values[0].split(',')[0]
    prime_pos = []
    [prime_pos.append(item.split(',')[0]) for item in list(total['player_positions'])]
    total['prime_pos'] = prime_pos
    same_nationality = total[total['nationality_name'] == nationality]
    same_league = total[total['league_name'] == league]
    same_club = total[total['club_name'] == club]
    same_pos = total[total['prime_pos']==position]
    comp_set = {
        'nationality': same_nationality,
        'league': same_league,
        'club': same_club,
        'position': same_pos,
    }
    return comp_set[set_type]

def get_comparisons(s_name, set_type, year):
    df_l = define_list_df()
    year_csv = {
        '2023': df_l[0],
        '2022': df_l[1],
        '2021': df_l[2],
        '2020': df_l[3],
        '2019': df_l[4],
        '2018': df_l[5],
    }
    total = year_csv[year]
    p_id = list(total[total['short_name']==s_name]['sofifa_id'].values)[0]
    player_df = total[total['sofifa_id']==p_id]
    player_pos = player_df['player_positions'].values[0].split(',')[0]
    player_type = define_player_type(player_pos)
    plot_combination = define_plot_combinations()
    comp_set = get_comp_set(player_df, set_type, total)
    plot_list = []
    for i in range(5):
      x_attr = plot_combination[player_type][i]['x_attr']
      y_attr = plot_combination[player_type][i]['y_attr']
      size_attr = plot_combination[player_type][i]['size_attr']
      title = plot_combination[player_type][i]['title']
      fig = get_plots(x_attr, y_attr, size_attr, comp_set, title, player_df)
      plot_list.append(fig)
    if not os.path.exists("assets/images/comparison/"):
      os.mkdir("assets/images/comparison/")
    else:
      filelist = [ f for f in os.listdir("assets/images/comparison/") if f.endswith(".png") ]
      for f in filelist:
          os.remove(os.path.join("assets/images/comparison/", f))
    [plot_list[i].write_image(f"assets/images/comparison/{set_type}-{i+1}.png") for i in range(len(plot_list))]
    return plot_list
