# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 13:04:05 2022

@author: Miles

"""
import pandas as pd


MainData = []
MainData = pd.read_csv("MainData.txt", delimiter = "\t")

Scores = {
    "Ayer" : 0,
    "Abington" : 0,
    "Andover" : 0,
    "Belmont" : 0,
    "Beverly" : 0,
    "Dedham" : 0,
    "Concord" : 0,
    "Canton" : 0,
    "Brockton" : 0,
    "Braintree" : 0,
    "Chelsea" : 0,
    "Hingham" : 0,
    "Franklin" : 0,
    "Kingston" : 0,
    "Plymouth" : 0,
    "Norwood" : 0,
    "Needham" : 0,
    "Newton" : 0,
    "Mansfield" : 0,
    "Rockport" : 0,
    "Quincy" : 0,
    "Wakefield" : 0,
    "Waltham" : 0,
    "Weston" : 0,
    "Winchester" : 0,
    "Wellesley" : 0,
    "Weymouth" : 0,
    "Westwood" : 0,
    "Whitman" : 0,
}

MainData['Score'] = 0

for i in range(29):
    #Water 
    if MainData.iloc[i,1] == 1:
        Scores[MainData.iloc[i,0]] += 3
    
    #Sewage
    if MainData.iloc[i,2] == 1:
        Scores[MainData.iloc[i,0]] += 3
    
    #Electricity
    if MainData.iloc[i,3] == 1:
        Scores[MainData.iloc[i,0]] += 1
        
    #Natural Gas
    if MainData.iloc[i,4] == 1:
        Scores[MainData.iloc[i,0]] += 1
    
    #Cable
    if MainData.iloc[i,5] == 1:
        Scores[MainData.iloc[i,0]] += 1
        
    #School Score
    if "A" in MainData.iloc[i,9]:
        Scores[MainData.iloc[i,0]] += 3
    elif "B" in MainData.iloc[i,9]:
        Scores[MainData.iloc[i,0]] += 1
        
    #Graduation Rate
    if MainData.iloc[i,10] > 95:
        Scores[MainData.iloc[i,0]] += 3
    elif 95 >= MainData.iloc[i,10] and MainData.iloc[i,10] > 90:
        Scores[MainData.iloc[i,0]] += 2
    elif 90 >= MainData.iloc[i,10] and MainData.iloc[i,10] > 85:
        Scores[MainData.iloc[i,0]] += 1
        
    #Near Hospital
    if MainData.iloc[i,13] == 1:
        Scores[MainData.iloc[i,0]] += 2
        
    #Subsidized Housing Inventory %
    if MainData.iloc[i,12] > 10:
        Scores[MainData.iloc[i,0]] -= 5
        
    MainData.iloc[i,14] = Scores[MainData.iloc[i,0]]
        

#print(MainData)   

ScoresOrdered = MainData.sort_values(['Score'], ascending=False)
#print(ScoresOrdered)
#print(ScoresOrdered['Municipality'])

Rank1 = []

for k in range(29):
    Rank1 += [ScoresOrdered.iloc[k,0]]
    
#print(Rank1)

Rank1.remove('Weston')

#print(Rank1)


Rank2 = [
    'Chelsea',
    'Waltham',
    'Brockton',
    'Needham',
    'Newton',
    'Norwood',
    'Andover',
    'Belmont',
    'Concord',
    'Braintree',
    'Ayer',
    'Westwood',
    'Abington',
    'Rockport',
    'Wakefield',
    'Weymouth',
    'Quincy',
    'Mansfield',
    'Winchester',
    'Franklin',
    'Canton',
    'Dedham',
    'Beverly',
    'Wellesley',
    'Whitman',
    'Plymouth',
    'Hingham',
    'Kingston',
]

#print(Rank2)

FinalRanks = {
    "Ayer" : 0,
    "Abington" : 0,
    "Andover" : 0,
    "Belmont" : 0,
    "Beverly" : 0,
    "Dedham" : 0,
    "Concord" : 0,
    "Canton" : 0,
    "Brockton" : 0,
    "Braintree" : 0,
    "Chelsea" : 0,
    "Hingham" : 0,
    "Franklin" : 0,
    "Kingston" : 0,
    "Plymouth" : 0,
    "Norwood" : 0,
    "Needham" : 0,
    "Newton" : 0,
    "Mansfield" : 0,
    "Rockport" : 0,
    "Quincy" : 0,
    "Wakefield" : 0,
    "Waltham" : 0,
    "Winchester" : 0,
    "Wellesley" : 0,
    "Weymouth" : 0,
    "Westwood" : 0,
    "Whitman" : 0,
}

for count1, element1 in enumerate(Rank1):
    #print(str(count) + " AND " + ele)
    FinalRanks[element1] += count1
    
for count2, element2 in enumerate(Rank2):
    #print(str(count) + " AND " + ele)
    FinalRanks[element2] += count2
    
#print(FinalRanks)    

#{k: v for k, v in sorted(FinalRanks.items(), key=lambda item: item[1])}

#print(k)

OrderedDic = sorted(FinalRanks.items(), key=lambda x: x[1])

#print(OrderedDic)

print()
print()
print("Here is the final order ranking for municipalities best for Housing Foward MA to move foward with:")
print() 

count = 1    
for mun in OrderedDic:
   print(str(count) + ": " + mun[0])
   count += 1   
    
    
    
    
    
    