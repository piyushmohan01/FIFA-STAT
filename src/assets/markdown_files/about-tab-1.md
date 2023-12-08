# Guide to FIFA-STAT :

This page is designed to help the users understand the working of the app. Here, you can find how to navigate through the app and make the most of it. We will be discussing all the aspects of the app and how they could be used for stat-analysis of the players. 

---

## Pick your player :

![PlayerSidebar](./assets/images/app-screenshots/player-sidebar.png)

We start by choosing a player from the latest FIFA rooster (FIFA 23) and this can be done in two different ways. Want to look up your favorite player's stats? Or do you want to view all players from your favorite team? The app allows the users to pick players by name but also narrow down the options to players of a specific team in any of the available leagues. You can find the player picker on the sidebar of the stat-page. The radio options on the bottom let you choose the way you would like to pick your player. You can find more about the options below :

#### Pick by Player Name :
- To pick a player by their name, simply select the **NAME** option in the bottom
- The dropdown pertaining to the option gets enabled for selection. The options in the dropdown show player names sorted in the descending order of highest overall in FIFA 23.
- You can also start typing the name of your player and the options in the dropdown get reduced to player names containing the alphabets typed by the user.

#### Pick by Player Team :
- In order to get all players from a particular team, first select the **TEAM** option in the bottom.
- Now all the dropdowns necessary for the selection get enabled. Start by choosing the league (available leagues : Ligue 1, La Liga, Premier League, Bundesliga, Serie A, Indian Super League). 
- Now that the league is selected, you will be able to find all teams in the league in the team dropdown. Go ahead and pick any team from the options.
- Once you select your team, the next dropdown should have all players playing for the team selected.

---

## Player Stat-Page :

This section covers all the parts of the player stat-page. The page is split into four sections: Player Info, Player Stats, Growth/Compare Visualizations, and Player Percentiles. You can find more about the sections below :

### Player Info :

![PlayerInfo](./assets/images/app-screenshots/player-info.png)

This section can be located on the top left part of the page and this contains all the necessary information about the player that the user has picked. Here you can find :

* Player's Face, Jersey number, Name, and Team
* A table showing more info such as Age, Height, Weight, Player and Club Positions, Nationality, Preferred Foot, along with Weak Foot and Skill rating.
* A football pitch with one or more highlighted areas indicating the player's position. This gives a visual idea to the users that are not much familiar with the positioning system followed in football.

---

### Player Stats :

![PlayerSidebar](./assets/images/app-screenshots/player-stats.png)

Here you can find all the stats the player holds in the latest FIFA game (FIFA 23). The section is split into 4 tabs in order to show all the attributes used in the FIFA game franchise.
* A very popular football game chart (Spider Chart) can be found in the first tab. This shows the strength of the player in different aspects of football such as Passing, Physicality, Dribbling, Defending, Pace, and Shooting for outfield players (everyone except keepers) and GK Kicking, Positioning, Reflexes, Speed, Diving, and Handling for keepers.
* Along with the chart, one can find a table containing the numerical rating of the player in all the categories mentioned above along with the overall rating of the player in the game.
* The table continues in the other three tabs showing the numerical ratings of the player corresponding to different attributes.
* The color code on the numerical attributes follow a somewhat-close-to-FIFA colors for ratings. Dark green represents the best attributes of the player and as the rating goes down, the colors change from shades of green to yellow and finally to red which indicate the player's weakest attributes.

---

### Growth/Compare Visualizations :

This section contains almost all of the major visualizations used in the app. The visualizations are split into two categories: Growth and Compare. All visualizations are shown at the same place every time and with navigation buttons provided on both sides, the users can toggle through the various visualizations. The visualizations are made with Plotly which means users can interact with them by zooming, selecting, and even downloading the plots as image files.

#### Choosing visualization category and variables :

We start by choosing on of the options from the radio buttons. Once we have one category selected, we further pick more sorting variables from the enabled dropdowns

#### 1) Growth visualizations :

* Select the attribute category you want to see the player's growth in once you've selected the **GROWTH** option.

![PlayerSidebar](./assets/images/app-screenshots/player-growth-1.png)

* The Bar Graph shows the players growth in the selected category over the years in FIFA (earliest from FIFA-18 and latest till FIFA-23). The number of bars represent the years of player as a FIFA player playing in the first division in the available leagues.

![PlayerSidebar](./assets/images/app-screenshots/player-growth-2.png)

* Upon toggling the visualization using the arrow buttons provided on both sides, the user can view the alternative Heatmap indicating the growth. A color shade reference is provided beside the map to indicate that the darker the shade gets the higher the rating the player holds for the specific attribute.

#### 2) Compare visualizations :
* Once the **COMPARE** option is selected, two other dropdowns get enabled. The first one represents the comparison set that the user wants to compare the player with. The options comprise of same Nationality, League, Club, or Position. For example, if the option Nationality is selected, the visualization would show all players from the selected player's Nationality. Users can find how well the selected player fares in comparison to other players over different comparison sets.
* The second dropdown asks for the year based on which the FIFA rooster is to be considered for comparison. For example, if the year 2020 is selected, then all the comparison sets are set to use the player rooster from the FIFA-20 edition. This can help users compare their players over the different FIFA game editions.
* Once all the parameters are selected, the user can find all the visualizations in the form of Scatterplots. The attributes used for the Scatterplots are chosen based on the selected player's prime position. For example, if the selected player is a striker (ST), then the attributes used over the different Scatterplots represent the top-most important attributes a striker is expected to have. The plots are made using combinations of two attributes with an added third attribute indicated using the size of the scatter points. 

![PlayerSidebar](./assets/images/app-screenshots/player-compare-1.png)

* Users can hover over any of the scatter points to find the numerical rating of the two plus attributes along with the short name of the player. The point representing the selected player is given a red color to help visually differentiate the player from the rest of the comparison set and the player's name is also displayed on top of the scatter point.
* If we continue with the case of the selected player being a striker (ST), then one of the plots would be Finishing vs Shot Power (w Curve). This plot shows how good the player's finish and shot power is while also looking at the curve attribute.

![PlayerSidebar](./assets/images/app-screenshots/player-compare-2.png)

* The players are sorted into position types based on their prime positions. The position types are then used to find the combination of attributes that is to be used for the selected player. The position types are as such: Midfielder, Forward, Winger, Full-back/Wing-back, Center-back, and Keeper.
* The plots can be toggled using the arrow buttons provided on both sides of the plot area. There are five different plots for all the different position types.
* Users can interact with the plots by cropping a section of the plot and viewing the comparisons with players having attributes closer to the selected player. This can be useful to find cheaper or alternative prospects to sign for your team while having similar attributes of another expensive or older player.

---

### Player Percentiles :

![PlayerSidebar](./assets/images/app-screenshots/player-percentiles-1.png)

This section allows users to compare the select player's attributes as a form of percentiles in comparison to other players.
* The user picks one of the many category options from the buttons provided on the right side. The options represent different attribute categories each having different attributes under them.
* Along with the attribute categories, the users can also pick the option to find the top-5 or worst-5 attribute percentiles of the player in comparison to other players.
* The percentiles are found on the basis of player position but this time a lot simpler, the players are sorted into outfield players (everyone except keepers) and keepers.
* The percentage bars appear once an option is selected. The bars have the percentile displayed over them and the shades of the color are used to help visually differentiate between the various attributes.

---

### Conclusion :

The page covered all the aspects of the application along with screenshots to demonstrate the usage better. The scatterplots and growth charts shown in the images above vary for every player depending on the position and availability in top-flight leagues in FIFA games over the years. In order to find out how the app can be used for personal case studies, visit the 'Case Studies' page. Hope you have fun with the app! Cheers!
