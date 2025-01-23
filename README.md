## FIFA-STAT : Analytics Dashboard for FIFA enthusiasts

### About the Dashboard :
The app is predominantly developed using Dash and Plotly, using FIFA rosters of male players spanning FIFA 18 to FIFA 23. The datasets were sourced from Stefano Leone’s Kaggle page, with FIFA-18 to FIFA-22 data extracted from the [FIFA-22 dataset](https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset), and the specific FIFA-23 player data obtained from the dedicated [FIFA-23 dataset](https://www.kaggle.com/datasets/stefanoleone992/fifa-23-complete-player-dataset). The FIFA-23 roster was acquired from a distinct dataset, introducing some inconsistencies compared to data from previous versions. It’s worth noting that all the data used was originally scraped from the [Sofifa website](https://sofifa.com/?r=230054&set=true), ensuring comprehensive and accurate information for analysis within the app. Along with the main page, an additional about page is added to provide users a guide to work with the application along with a few selected case-studies demonstrating how analysis through the dashboard could be useful.

### Tech-Stack & Requirements :  

- dash == `2.9.2`
- pandas == `2.0.0`
- opencv-python == `4.7.0.68`
- mplsoccer == `1.2.2`

The project tries to encompass the most important aspects of a Dash app ranging from structuring layouts, managing functionality with callbacks, and building interactive graphs. Most parts in the application were built using Dash’s Core components (dcc), HTML components (html), and Bootstrap components (dbc). The visualisations representing the vertical football pitch were plotted using the MPLSoccer and OpenCV libaries. 

### Features & Use-cases :

- Search player function to pick either using player name or by sorting through leagues & teams
- Player profile presented through face, club-logo, general info, and visualized player positions
- Radar plot & 4-tab table highlighting the selected player's stats across primary and secondary attributes
- Analyse player growth on primary attributes with 2 plots from all versions where player represented 1st division
- Compare player stats across various comparison sets and FIFA versions with 6 plots pre-assigned for each position-type
- Visualisations to assess player percentile ranking in selected primary attributes compared to all other players
- All visualisations are interactive with options to hover for more info, zoom in to sub-group, & download plot images

### Added Case-Studies :

In the about section of the project, the users can find two case studies performed using the analysis provided by the application. Manchester City’s treble in the 2022/23 campaign and Real Madrid’s domination in the 2021/22 season was studied. The two most influential players from both the teams were analysed wherein, the player’s stats from the real world were put up against the stats in-game. The player’s strengths and weaknesses in the specific version of the game were compared to their performances for the team in the particular season. The case studies were added as an attempt to provide a template or headstart for users to take on their own approach for using in-game stats in whichever way they wish to.

### Future Work and Final Notes :

In the future, female player data can also be added to the project. The choice to emit the female player data was solely based on the major inconsistencies in the columns and values from the male player data. Speaking of adding more data, only the past 6 versions of FIFA were used in the project ranging from FIFA-18 to FIFA-23, so this is another area where the project can be made bigger in scope.

The datasets used for the projects were filtered to reduce the size of the data used behind the application. But even after such filtering, the numerous dash elements with several behind-the-app functions result in a slow response time. The app takes some seconds to respond to certain user-interactions. While the response time is something that should be rectified in the future, it would be advisable for users to be patient with the clicks. Keep an eye on the ‘Updating’ status on the browser tab that indicates the app trying to work through the changes.
