# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 19:42:03 2022

@author: Miles
"""

import pandas as pd

DensityData = []
DensityData = pd.read_csv("DensityData.txt", delimiter = "\t")
pd.set_option('display.max_column', None)
pd.set_option('display.max_rows', None)

LessDense = DensityData.loc[(DensityData["Density"]<15) , ["Municipalities", "Density", "STATION", "LINES/ROUTES"]]
NoBoston = LessDense.loc[(DensityData["Municipalities"]!="Boston") , ["Municipalities", "Density", "STATION", "LINES/ROUTES"]]


Density_Order = NoBoston.sort_values(['Density'], ascending=False)
containBoston = 0
print()
print("  MBTA Community Densities to Research (Less Than 15 Units/Acre,  Excluding Boston)")
print()
print()
print(" "*5 + "MUNICIPALITY:" + " "*20 + "DENSITY:" + " "*8 + "STATION:" + " "*26 + "LINE/ROUTE:")



Names = ["Yuxin", "Ryan", "Gloria", "Chuhan", "Miles"]

#print(Density_Order.iloc[0,0])


for n in range(len(Names)):
        print()
        print(Names[n] + ":")
        print()
        counter = 1
        index = n
        while(index<len(Density_Order)):
            if "Boston" not in Density_Order.iloc[index,0]:
                numInLine = 4-len(str(counter))
                densityInLine = 33-len(str(Density_Order.iloc[index,0]))
                stationInLine = 16-len(str(Density_Order.iloc[index,1]))
                routeInLine = 34-len(str(Density_Order.iloc[index,2]))
                print(str(counter) + "." + " "*numInLine + str(Density_Order.iloc[index,0]) 
                      + " "*densityInLine + str(Density_Order.iloc[index,1]) 
                      + " "*stationInLine + str(Density_Order.iloc[index,2])
                      + " "*routeInLine + str(Density_Order.iloc[index,3]))
                index += 5
                counter += 1
                #print(index)
            else:
                index += 5
           
                
                
                
