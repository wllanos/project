# -*- coding:utf-8 -*-  
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import sys
import csv
import nltk
import re


#share of voice

reload(sys)
sys.setdefaultencoding("utf-8")
#sys.setdefaultencoding('Cp1252')
os.chdir('/Users/Heisenberg/Data Science/ProyectoBID')

#Cleaning data
#Part 1
#Many tweets weres in two lines, with the below algorith I've fixed this issue
with open('TwitterMentions.csv', 'r') as f:
        dirty = [row for row in csv.reader(f.read().splitlines())]
len(dirty)
tweets=[]

for row in dirty:
    tweet=''
    for i in row:
        tweet = tweet + i
    if len(tweet.split('::')) == 24:
        tweets.append(tweet)
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
tweetisColombia=[]


#test = 'RT @CpdlRd: @el BiD: ¿Qué BancO interamericano hacer las #ciudades de LatAm +accesibles? http://t.co/ALJUrrmk2u @BID_Ciudades  @armandogarciap http://t.c…'

#re.findall(r"(?i)Banco Interamericano", test)

#RT @geovannyvicentr: El Barómetro de servicio civil está enfocado al buen gobierno, #GobiernoElectronico y #GobiernoAbierto @armandogarciap… 

#ignore case
op1 = '''\\b'''
op2 = '''\\b'''


for row in tweets:
        tweetText.append(row.split('::')[1].encode('ascii','ignore'))        
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
        tweetUserLocation.append(row.split('::')[16].encode("ascii", "ignore").upper())
        tweetUserGeo_enabled.append(row.split('::')[17])
        tweetUserName.append(row.split('::')[18])
        tweetUserLang.append(row.split('::')[19])
        tweetUserUrl.append(row.split('::')[20])
        tweetUserCreated_at.append(row.split('::')[21])
        tweetUserTime_zone.append(row.split('::')[22])
        tweetUserIs_translator.append(row.split('::')[23])

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#I've made a Colombia list with every city, statate, county etc
terms = pd.read_csv('Terms.csv', parse_dates=True)
#accent removed
termsCleaned = []
for term in terms['TERM']:
    termsCleaned.append(term.encode("ascii", "ignore").strip())

#removing common places in other countris(the following list is irrelevant for our study)
#FLORENCIA, CÓRDOBA, AMAZONAS,LA PLATA,MADRID
termsCleaned.remove('FLORENCIA')
termsCleaned.remove('CRDOBA')
termsCleaned.remove('AMAZONAS')
termsCleaned.remove('LA PLATA')
termsCleaned.remove('FLORIDA')
termsCleaned.remove('MADRID')

#mapping twData.tweetUserLocation with terms cleaned

for location in tweetUserLocation:
    flag = 0
    op1 = '''\\b'''
    op2 = '''\\b'''

    for place in termsCleaned:
        if not (re.search(r""+op1+place+op2,location,flags=re.IGNORECASE)) is None: 
            tweetisColombia.append("1")
            flag = 1
            break
    if flag == 0:
        tweetisColombia.append("0")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
, 'tweetIsColombia':tweetisColombia
})
cleanData.to_csv('cleaned.csv')

#after the second algorith there are 57711 tweets
#Part 3
#Reading data with pandas and creating new columns
twData = pd.read_csv('cleaned.csv', parse_dates=True)

twData.describe()
twData.head()
twData.info#[53987 rows x 13 columns]>

'''
#Range april 20th to may 28th
#Many people dont put the country name, they use state name or a kind of variation
twData['isColombia']  = twData.tweetUserLocation.str.strip().map({
  'BARRANQUILLA':1, 'BARRANQUILLA - COLOMBIA':1
, 'BARRANQUILLA COLOMBIA':1, 'BOGOT':1, 'BOGOT - COLOMBIA':1, 'BOGOT COLOMBIA':1
, 'BOGOT COLOMBIA.':1, 'BOGOT D.C':1, 'BOGOT D.C - COLOMBIA':1, 'BOGOT D.C.':1
, 'BOGOT D.C. COLOMBIA':1, 'BOGOT-COLOMBIA':1, 'BOGOTA':1, 'BOGOTA - COLOMBIA':1
, 'BOGOTA COLOMBIA':1, 'BOGOTA D.C.':1, 'BOGOTA Y COLOMBIA HUMANA':1, 'BUCARAMANGA':1
, 'CALI':1, 'CALI - COLOMBIA':1
, 'CALI COLOMBIA':1, 'CALI- COLOMBIA':1
, 'CALI-COLOMBIA':1, 'CARTAGENA':1
, 'CCUTA COLOMBIA':1, 'COLOMBIA':1
, 'COLOMBIA | MXICO | ESPAA':1, 'MANIZALES':1
, 'MEDELLIN':1, 'MEDELLIN - COLOMBIA':1
, 'MEDELLIN COLOMBIA':1, 'MEDELLN':1
, 'MEDELLN - COLOMBIA':1, 'MEDELLN COLOMBIA':1
, 'PASTO':1, 'PASTO - NARIO - COLOMBIA':1
, 'PASTO COLOMBIA!!':1, 'PEREIRA':1
, 'SANTA MARTA - COLOMBIA':1, 'SANTA MARTA COLOMBIA':1
, 'VALLEDUPAR':1, 'VALLEDUPAR COLOMBIA':1
})
'''


cities = twData[twData.tweetIsColombia == 1].tweetUserLocation

#twData['tweetIsColombia'] = np.where(twData.tweetIsColombia == 1, 1, 0)
#before to remove the accent #808
#manual mapping copying and pasting 2185
#after to remove the accent 1876
#afeter to apply a csv mapping 3268
twData.tweetIsColombia.sum()
#I have to identify our brand and our competitors
#Part 4
#Drawing some charts to see data behavor
#grouping tweets by brand
twData.tweetBrand.value_counts().plot(kind='bar', title='')
plt.xlabel('Brand')
plt.ylabel('Tweets')
plt.show()   

twData[(twData.tweetBrand == 'BID')].info
twData[(twData.tweetBrand == 'BANCO MUNDIAL')].info
twData[(twData.tweetBrand == 'CAF')].info
twData[(twData.tweetBrand == 'UNDEFINED')].info
       
#Part 5
#Analizing only one country COLOMBIA                     
#looking for influencers
twData.plot(kind='line', x='tweetDate', y='tweetUserFollowers_count', alpha=0.4)
plt.xlabel('Date')
plt.ylabel('User followers count')
plt.show()                                 

#

twData[twData.tweetIsColombia==1].tweetUserFollowers_count.describe()
#mean       38590.124200
#max      5257638
test = twData[(twData.tweetIsColombia==1) & (twData.tweetUserFollowers_count == 5257638)]
#https://twitter.com/NoticiasRCN
#Banco Interamericano de Desarrollo eligió los Centros para Drogodependientes en #Bogotá como experiencias exitosas. http://t.co/vYcXzITKlO
#tweet id 597037806331043840
#https://twitter.com/NoticiasRCN/status/597037806331043840
#world bank spanish countries %
#bid spanish countries %
#caf spanish countries
twData[(twData.tweetIsColombia==1) & (twData.tweetBrand == 'BID')].info#[1572 rows x 14 columns]>
twData[(twData.tweetIsColombia==1) & (twData.tweetBrand == 'BANCO MUNDIAL')].info#[1045 rows x 14 columns]>
twData[(twData.tweetIsColombia==1) & (twData.tweetBrand == 'CAF')].info#[131 rows x 14 columns]>
twData[(twData.tweetIsColombia==1) & (twData.tweetBrand == 'UNDEFINED')].info#[520 rows x 14 columns]>
#getting top 10 followers numbers
twData[(twData.tweetIsColombia==1) & (twData.tweetBrand == 'BID')].tweetUserFollowers_count.order().tail(10)
twData[(twData.tweetIsColombia==1) & (twData.tweetBrand == 'BANCO MUNDIAL')].tweetUserFollowers_count.order().tail(10)
twData[(twData.tweetIsColombia==1) & (twData.tweetBrand == 'CAF')].tweetUserFollowers_count.order().tail(10)

twData.groupby('tweetBrand')['tweetIsColombia'].sum().plot(kind='bar')

