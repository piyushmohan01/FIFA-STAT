import pandas as pd
from player_growth import define_growth_cat, rename_attributes

df = pd.DataFrame()

def get_percentile(s_name, attr_cat):
    global df
    df = pd.read_csv('new_data/m_23.csv', index_col=[0])
    p_id = df[df['short_name']==s_name]['sofifa_id'].values[0]
    player_df = df[df['sofifa_id']==p_id]
    p_skill = ['attacking_crossing','attacking_finishing','attacking_heading_accuracy','attacking_short_passing','attacking_volleys',
           'skill_dribbling','skill_curve','skill_fk_accuracy','skill_long_passing','skill_ball_control',
           'movement_acceleration','movement_sprint_speed','movement_agility','movement_reactions','movement_balance',
           'power_shot_power','power_jumping','power_stamina','power_strength','power_long_shots',
           'mentality_aggression','mentality_interceptions','mentality_positioning','mentality_vision','mentality_penalties','mentality_composure',
           'defending_marking_awareness','defending_standing_tackle','defending_sliding_tackle']
    if list(player_df['player_positions'].values)[0] == 'GK':
      p_skill = ['attacking_crossing','attacking_finishing', 'attacking_heading_accuracy','attacking_short_passing','attacking_volleys',
           'skill_dribbling','skill_curve','skill_fk_accuracy','skill_long_passing','skill_ball_control',
           'movement_acceleration','movement_sprint_speed','movement_agility','movement_reactions','movement_balance',
           'power_shot_power','power_jumping','power_stamina','power_strength','power_long_shots',
           'mentality_aggression','mentality_interceptions','mentality_positioning','mentality_vision','mentality_penalties','mentality_composure',
           'defending_marking_awareness','defending_standing_tackle','defending_sliding_tackle',
           'goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking', 'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed']
      df = df[df['club_position'] == 'GK']
    else:
      df = df[df['club_position'] != 'GK']
    top_worst_5 = False
    if (attr_cat != 'top-5') and (attr_cat != 'worst-5'):
      skills_list = define_growth_cat(attr_cat)
    else:
      skills_list = p_skill
      top_worst_5 = True
    attr = player_df[skills_list].T
    attr.sort_values(by=[attr.columns[0]], inplace=True, ascending=False)
    attributes = list(attr.index.values)
    if top_worst_5 == True:
      if attr_cat == 'top-5': attributes = attributes[:5]
      elif attr_cat == 'worst-5': attributes = attributes[-5:]
    percentiles = []
    for attr in attributes:
      less_count = 0
      for x in list(df[attr].values):
        if x < player_df[attr].values[0]: less_count += 1
      total_count = len(list(df[attr].values))
      percentile = round((less_count/total_count)*100, 2)
      percentiles.append(percentile)
    attributes = rename_attributes(attributes)
    df_perc = pd.DataFrame({'Attribute': attributes, 'Percentile': percentiles})
    return df_perc
