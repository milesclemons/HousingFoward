# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 20:36:48 2022

@author: Miles R. Clemons

Data From: https://mhpcenterforhousingdata.shinyapps.io/todex/
           https://maps.massgis.digital.mass.gov/MassMapper/MassMapper.html
"""
import pandas as pd
import matplotlib.pyplot as plt

TopData = []
TopData = pd.read_csv("MBTA-Top25.txt", delimiter = "\t")

StationScores = {
    "Quincy Center": 0,
    "Bellingham Square": 0,
    "Braintree": 0,
    "Swampscott": 0,
    "Montello": 0,
    "Brandeis-Roberts": 0,
    "Worcester": 0,
    "Middleborough-Lakeville": 0,
    "Shirley": 0,
    "Grafton": 0,
    "Wollaston": 0,
    "Needham Height": 0,
    "Newton Centre": 0,
    "Belmont": 0,
    "North Wilmington": 0, 
    "Newtonville": 0,
    "West Newton": 0,
    "Stoughton": 0,
    "Waban": 0,
    "Newton Highlands": 0,
    "Beaconsfield": 0,
    "Eliot": 0,
    "Canton Center": 0,
    "Auburndale": 0,
    "Hersey": 0
}

for i in range(25):
    #Density Evaluation:
    if 0 < TopData.iloc[i,2] <= 4:
        StationScores[TopData.iloc[i,0]] += 5
    elif 4 < TopData.iloc[i,2] <= 10:
        StationScores[TopData.iloc[i,0]] += 10
    else:
        StationScores[TopData.iloc[i,0]] += 5
        
    #Water/Sewar Evaluation:
    if TopData.iloc[i,3] == "WS":
        StationScores[TopData.iloc[i,0]] += 10
    elif TopData.iloc[i,3] == "W":
        StationScores[TopData.iloc[i,0]] += 8
    elif TopData.iloc[i,3] == "S":
        StationScores[TopData.iloc[i,0]] += 8
    else:
        StationScores[TopData.iloc[i,0]] += 5
        
    #Contaminated Land Evaluation:
    if TopData.iloc[i,4] > 0:
        StationScores[TopData.iloc[i,0]] -= 3
    
    #Conservation Area Evaluation:
    StationScores[TopData.iloc[i,0]] -= (TopData.iloc[i,5] // 7)
    
    #Zoning Data Evaluation:
    if "Multi" in TopData.iloc[i,6]:
        StationScores[TopData.iloc[i,0]] += 5
    elif "Single" in TopData.iloc[i,6]:
        StationScores[TopData.iloc[i,0]] += 2
        
    #Water Coverage Evaluation:
    StationScores[TopData.iloc[i,0]] -= (TopData.iloc[i,7] // 5)  
    
    #Rapid Tranist Evaluation:
    StationScores[TopData.iloc[i,0]] += (TopData.iloc[i,8] * 5)
    
    #Developable Areas Evaluation:
    StationScores[TopData.iloc[i,0]] += (TopData.iloc[i,9] // 7)
    
    
    TopData.iloc[i,10] = StationScores[TopData.iloc[i,0]]

TopScoreOrdered = TopData.sort_values(['SCORE'], ascending=False)
print(TopScoreOrdered)
    
Stations = []
Scores = []
for j in range(25):
    Stations += [TopScoreOrdered.iloc[j,0]]  
    Scores += [TopScoreOrdered.iloc[j,10]]
    
#Plotting Bar Chart:    
plt.bar(Stations, Scores, color="red")
plt.title('Scores for MBTA Communities Best Fit for Transit-Oriented Development Soley On: \n MASS GIS Data, TODEX Density Data, and Public Zoning Data')
plt.xlabel('Station')
plt.xticks(rotation=80)
plt.ylabel('Score')
plt.show()    
    