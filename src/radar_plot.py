import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('new_data/m_23.csv', index_col='Unnamed: 0')

def get_radar_plot(r_values, categories):
    values = [20, 20, 20, 20, 20]
    bgcolors = [
      'rgba(37,37,37, 0.95)',
      'rgba(28,25,25, 0.95)',
      'rgba(17,17,17, 0.95)',
      'rgba(13,13,13, 0.95)',
      'rgba(0,0,0, 0.95)',
    ]

    slices=len(r_values)
    fields=[100]*slices
    circle_split = [360/slices]*(slices)
    theta= 0
    thetas=[0]
    for t in circle_split:
        theta=theta+t
        thetas.append(theta)
    thetas

    fig = go.Figure()

    for t in range(0, len(bgcolors)):
        fig.add_trace(go.Barpolar(
            r=[values[t]],
            width=360,
            hoverinfo='skip',
            marker_color=[bgcolors[t]],
            opacity=1,
            name = 'Range ' + str(t+1),
            showlegend=False,
        ))
        t=t+1

    fig.add_trace(go.Scatterpolar(
          text = categories,
            r = r_values,
            showlegend=False,
            mode='lines+markers+text',
            textposition='top center',
            hoverinfo='skip',
            fill='toself',
            fillcolor='rgba(19, 255, 255, 0.6)',
            marker = dict(
              color = 'rgba(19, 255, 255, 1)',
              size = 6,
            ),
          ))

    fig.update_layout(
        template=None,
        paper_bgcolor = 'rgba(255, 255, 255, 0)',
        autosize=False,
        width=240,
        height=240,
        margin = dict(
          l=0, r=20, t=0, b=0,
        ),
        hoverlabel = dict(
          bgcolor = 'white',
          font_size=16,
          font = dict(color='black')
        ),
        polar = dict(
            radialaxis = dict(
              color = 'black',
              gridwidth=5,
              range=[0, 100],
              visible=False,
              showticklabels=False,
              ticks='', gridcolor = "black"
            ),
          angularaxis = dict(
            gridwidth=1,
            showticklabels=False, ticks='',
            rotation=210,
            direction = "clockwise",
            gridcolor = "black"
          )
        )
      )

    fig.update_yaxes(showline=True, linewidth=2, linecolor='white')
    return fig

def radar_plot(name):
    df_ = df[df['short_name']==name]
    pos = list(df_['player_positions'].values)[0]
    keeper = False
    if 'GK' in pos: keeper=True
    if keeper == False:
      pace = list(df_['pace'].values)[0]
      shooting = list(df_['shooting'].values)[0]
      passing = list(df_['passing'].values)[0]
      physic = list(df_['physic'].values)[0]
      dribbling = list(df_['dribbling'].values)[0]
      defending = list(df_['defending'].values)[0]
      r_values = [pace, shooting, passing, physic, dribbling, defending]
      categories = ['Pace', 'Shooting', 'Passing', 'Physic', 'Dribbling', 'Defending']
    else:
      diving = list(df_['goalkeeping_diving'].values)[0]
      handling = list(df_['goalkeeping_handling'].values)[0]
      kicking = list(df_['goalkeeping_kicking'].values)[0]
      positioning = list(df_['goalkeeping_positioning'].values)[0]
      reflexes = list(df_['goalkeeping_reflexes'].values)[0]
      speed = list(df_['goalkeeping_speed'].values)[0]
      r_values = [diving, handling, kicking, positioning, reflexes, speed]
      categories = ['GK Diving', 'GK Handling', 'GK Kicking', 'GK Positioning', 'GK Reflexes', 'GK Speed']
    fig = get_radar_plot(r_values, categories)
    return fig
