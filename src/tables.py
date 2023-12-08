import pandas as pd

df = pd.read_csv('new_data/m_23.csv')

def get_info_table(s_name):
    df_ = df[df['short_name']==s_name]
    info_cat = ['age', 'height_cm', 'weight_kg', 'player_positions', 'club_position', 'nationality_name', 'preferred_foot']
    info_values = []
    final_cat = []
    for cat in info_cat:
        info_values.append(list(df_[cat].values)[0])
        split_list = cat.split('_')
        if len(split_list)>1:
          target = split_list[0:]
          target_join = " ".join(target)
          final_cat.append(target_join.title())
        else:
          target = split_list[0]
          final_cat.append(target.title())
    df_info = pd.DataFrame({'Category':final_cat, 'Value':info_values})
    df_info.loc[len(df_info.index)] = ['Weak Foot', str(list(df_['weak_foot'].values)[0])+'⭐']
    df_info.loc[len(df_info.index)] = ['Skill Moves', str(list(df_['skill_moves'].values)[0])+'⭐']
    return df_info

def get_top_5_table(s_name):
    df_ = df[df['short_name']==s_name]
    top_5_outfield = ['overall', 'pace', 'shooting', 'passing', 'physic', 'dribbling', 'defending']
    top_5_gk = ['overall', 'goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking', 'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed']
    categories = []
    if 'GK' in str(df_['club_position'].values): categories = top_5_gk
    else: categories = top_5_outfield
    final_cat = []
    top_5_skill_stats = []
    for skill in categories:
        top_5_skill_stats.append(list(df_[skill].values)[0])
        split_list = skill.split('_')
        if len(split_list)>1:
          target = split_list[1:]
          target_join = " ".join(target)
          final_cat.append(target_join.title())
        else:
          target = split_list[0]
          final_cat.append(target.title())
    df_top_5_stat = pd.DataFrame({'Skill': final_cat, 'Stat': top_5_skill_stats})
    return df_top_5_stat

def get_stats_table(s_name):
    df_ = df[df['short_name']==s_name]
    p_skill = ['attacking_crossing', 'attacking_finishing',
       'attacking_heading_accuracy', 'attacking_short_passing',
       'attacking_volleys', 'skill_dribbling', 'skill_curve',
       'skill_fk_accuracy', 'skill_long_passing', 'skill_ball_control',
       'movement_acceleration', 'movement_sprint_speed', 'movement_agility',
       'movement_reactions', 'movement_balance', 'power_shot_power',
       'power_jumping', 'power_stamina', 'power_strength', 'power_long_shots',
       'mentality_aggression', 'mentality_interceptions',
       'mentality_positioning', 'mentality_vision', 'mentality_penalties',
       'mentality_composure', 'defending_marking_awareness',
       'defending_standing_tackle', 'defending_sliding_tackle']
    final_cat = []
    skill_stats = []
    for skill in p_skill:
        skill_stats.append(list(df_[skill].values)[0])
        split_list = skill.split('_')
        if len(split_list)>1:
          target = split_list[1:]
          target_join = " ".join(target)
          final_cat.append(target_join.title())
        else:
          target = split_list[0]
          final_cat.append(target.title())
    df_stat = pd.DataFrame({'Skill': final_cat, 'Stat': skill_stats})
    return df_stat
