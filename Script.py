# -*- coding:utf-8 -*-  
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import datetime
import sys
import csv
import nltk # Classic NLP package
import re

#share of voice

reload(sys)
sys.setdefaultencoding("utf-8")
#sys.setdefaultencoding('Cp1252')
os.chdir('/Users/Heisenberg/Data Science/ProyectoBID')

#Cleaning data
#Part 1
#Many tweets weres in two lines, with the below algorith I've fixed this issue
tweets = []
with open('TwitterMentions.csv', 'rU') as f:
    data = f.readlines()
#Tweets 67431
counter = 1
pNext=''
pCurrent=''

for row in range(1,len(data)):
    if(counter == len(data)-1):
        break    
    pCurrent = data[counter]
    if pCurrent[0:5].isdigit():         
        pNext = data[counter+1]                    
        if pNext[0:5].isdigit(): 
            tweets.append(pCurrent)
        else:
            tweets.append(pCurrent + pNext)        
    counter=counter+1 
#after the algorith there are 59299 tweets

#Part 2
#still many tweets were incomplete, with split('::') I will ensure that I get only complete data for every tweet
colNames =[ 
'tweetText',
'tweetId',
'tweetInReplyStatusId',
'tweetFavoriteCount',
'tweetRetweeted',
'tweetCoordinates',
'tweetTimestamp_ms',
'tweetGeo',
'tweetLang',
'tweetDate',
'tweetUserScreen_name',
'tweetUserProfile_image_url_https',
'tweetUserFollowers_count',
'tweetUserListed_count',
'tweetUserFollowing_count',
'tweetUserLocation',
'tweetUserGeo_enabled',
'tweetUserName',
'tweetUserLang',
'tweetUserUrl',
'tweetUserCreated_at',
'tweetUserTime_zone',
'tweetUserIs_translator']

tweetText=[]
tweetId=[]
tweetInReplyStatusId=[]
tweetFavoriteCount=[]
tweetRetweeted=[]
tweetCoordinates=[]
tweetTimestamp_ms=[]
tweetGeo=[]
tweetLang=[]
tweetDate=[]
tweetUserScreen_name=[]
tweetUserProfile_image_url_https=[]
tweetUserFollowers_count=[]
tweetUserListed_count=[]
tweetUserFollowing_count=[]
tweetUserLocation=[]
tweetUserGeo_enabled=[]
tweetUserName=[]
tweetUserLang=[]
tweetUserUrl=[]
tweetUserCreated_at=[]
tweetUserTime_zone=[]
tweetUserIs_translator=[]
tweetBrand=[]


#test = 'RT @CpdlRd: @el BiD: ¿Qué BancO interamericano hacer las #ciudades de LatAm +accesibles? http://t.co/ALJUrrmk2u @BID_Ciudades  @armandogarciap http://t.c…'

#re.findall(r"(?i)Banco Interamericano", test)

#RT @geovannyvicentr: El Barómetro de servicio civil está enfocado al buen gobierno, #GobiernoElectronico y #GobiernoAbierto @armandogarciap… 

#ignore case
for row in tweets:
    if len(row.split('::')) == 24:
        tweetText.append(row.split('::')[1])    
        
        if len(re.findall(r"(?i)@el_BID", row.split('::')[1]))>0:
            tweetBrand.append('BID')
        elif len(re.findall(r'(?i)@el BID', row.split('::')[1]))>0:
            tweetBrand.append('BID')
        elif len(re.findall(r"(?i)Banco Interamericano", row.split('::')[1]))>0:
            tweetBrand.append('BID')
        elif len(re.findall(r"(?i)el bid", row.split('::')[1]))>0:
            tweetBrand.append('BID')
        elif len(re.findall(r"(?i)Banco Mundial", row.split('::')[1]))>0:
            tweetBrand.append('BANCO MUNDIAL')
        elif len(re.findall(r"(?i)@BancoMundial", row.split('::')[1]))>0:
            tweetBrand.append('BANCO MUNDIAL')
        elif len(re.findall(r"(?i)BancoMundial", row.split('::')[1]))>0:
            tweetBrand.append('BANCO MUNDIAL')
        elif len(re.findall(r"(?i)@AgendaCAF", row.split('::')[1]))>0:
            tweetBrand.append('CAF')
        elif len(re.findall(r"(?i)AgendaCAF", row.split('::')[1]))>0:    
            tweetBrand.append('CAF')
        elif len(re.findall(r"(?i)banco de desarrollo de AméricaLatina", row.split('::')[1]))>0:
            tweetBrand.append('CAF')
        elif len(re.findall(r"(?i)CAF-Banco de desarrollo de América Latina", row.split('::')[1]))>0:
            tweetBrand.append('CAF')
        elif len(re.findall(r"(?i)el caf", row.split('::')[1]))>0:
            tweetBrand.append('CAF')

        else: 
            tweetBrand.append('UNDEFINED')
                    
        tweetId.append(row.split('::')[2])
        tweetInReplyStatusId.append(row.split('::')[3])
        tweetFavoriteCount.append(row.split('::')[4])
        tweetRetweeted.append(row.split('::')[5])
        tweetCoordinates.append(row.split('::')[6])
        tweetTimestamp_ms.append(row.split('::')[7])
        tweetGeo.append(row.split('::')[8])
        tweetLang.append(row.split('::')[9])
        tweetDate.append(pd.to_datetime(row.split('::')[10]))
        tweetUserScreen_name.append(row.split('::')[11])
        tweetUserProfile_image_url_https.append(row.split('::')[12])
        tweetUserFollowers_count.append(row.split('::')[13])
        tweetUserListed_count.append(row.split('::')[14])
        tweetUserFollowing_count.append(row.split('::')[15])
        #many countris has accent, I need to remove it
        tweetUserLocation.append(row.split('::')[16].encode("ascii", "ignore"))
        tweetUserGeo_enabled.append(row.split('::')[17])
        tweetUserName.append(row.split('::')[18])
        tweetUserLang.append(row.split('::')[19])
        tweetUserUrl.append(row.split('::')[20])
        tweetUserCreated_at.append(row.split('::')[21])
        tweetUserTime_zone.append(row.split('::')[22])
        tweetUserIs_translator.append(row.split('::')[23])

cleanData = pd.DataFrame({'tweetId':tweetId, 'tweetText':tweetText
, 'tweetBrand':tweetBrand
, 'tweetFavoriteCount':tweetFavoriteCount
, 'tweetCoordinates':tweetCoordinates
, 'tweetGeo':tweetGeo
, 'tweetUserLocation':tweetUserLocation
, 'tweetLang':tweetLang
, 'tweetDate':tweetDate 
, 'tweetUserScreen_name':tweetUserScreen_name
, 'tweetUserLang':tweetUserLang
, 'tweetUserFollowers_count':tweetUserFollowers_count
})
cleanData.to_csv('cleaned.csv')

#after the second algorith there are 57711 tweets
#Part 3
#Reading data with pandas and creating new columns
twData = pd.read_csv('cleaned.csv', parse_dates=True)

twData.describe()
twData.head()
twData.info#57711 rows x 10 columns
#Range april 20th to may 28th
#Many people dont put the country name, they use state name or a kind of variation
twData['isColombia']  = twData.tweetUserLocation.str.strip().map({'Colombia':1, 'Bogot':1
, 'Bogot, Colombia':1, 'Bogot D.C.':1, 'Bogota, Colombia':1, 'Bogota':1
, 'Bogot - Colombia':1, 'Colombia':1, 'Medelln':1, 'Ccuta, Colombia':1
, 'Cali, Colombia':1, 'Santa Marta':1, 'colombia':1, 'COLOMBIA':1
, 'Medelln, Colombia':1, 'bogota':1, 'Medellin':1, 'Bogota y Colombia Humana':1
, 'Barranquilla':1
})
#before to remove the accent #808
twData.isColombia.sum() 
#after to remove the accent 1876
#I have to identify our brand and our competitors
#Part 4
#Drawing some charts to see data behavor
#grouping tweets by brand
twData.tweetBrand.value_counts().plot(kind='bar', title='tweetBrandName')
plt.xlabel('Brand')
plt.ylabel('Tweets')
plt.show()          
#Part 5
#Analizing only one country COLOMBIA                     
#looking for influencers
twData.plot(kind='line', x='tweetDate', y='tweetUserFollowers_count', alpha=0.4)
plt.xlabel('Date')
plt.ylabel('User followers count')
plt.show()                                 

#
twData[twData.isColombia==1].tweetUserFollowers_count.describe()
#mean       38590.124200
#max      5257638
test = twData[(twData.isColombia==1) & (twData.tweetUserFollowers_count == 5257638)]
#https://twitter.com/NoticiasRCN
#Banco Interamericano de Desarrollo eligió los Centros para Drogodependientes en #Bogotá como experiencias exitosas. http://t.co/vYcXzITKlO
#tweet id 597037806331043840
#https://twitter.com/NoticiasRCN/status/597037806331043840
#world bank spanish countries %
#bid spanish countries %
#caf spanish countries
twData[(twData.isColombia==1) & (twData.tweetBrand == 'BID')].info#[937 rows x 14 columns]>
twData[(twData.isColombia==1) & (twData.tweetBrand == 'BANCO MUNDIAL')].info#[569 rows x 14 columns]>
twData[(twData.isColombia==1) & (twData.tweetBrand == 'CAF')].info#[95 rows x 14 columns]>
twData[(twData.isColombia==1) & (twData.tweetBrand == 'UNDEFINED')].info#[275 rows x 14 columns]>
#getting top 10 followers numbers
twData[(twData.isColombia==1) & (twData.tweetBrand == 'BID')].tweetUserFollowers_count.order().tail(10)
twData[(twData.isColombia==1) & (twData.tweetBrand == 'BANCO MUNDIAL')].tweetUserFollowers_count.order().tail(10)
twData[(twData.isColombia==1) & (twData.tweetBrand == 'CAF')].tweetUserFollowers_count.order().tail(10)


