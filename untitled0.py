# -*- coding: utf-8 -*-
"""
Created on Mon May 15 22:03:22 2023

@author: alpar
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

df = pd.read_csv("C:/Users/hp/Desktop/happiness index/2018.csv") 
df_2019 = pd.read_csv("C:/Users/hp/Desktop/happiness index/2019.csv") 

# #   Column                        Non-Null Count  Dtype  
# ---  ------                        --------------  -----  
#  0   Overall rank                  156 non-null    int64  
#  1   Country or region             156 non-null    object 
#  2   Score                         156 non-null    float64
#  3   GDP per capita                156 non-null    float64
#  4   Social support                156 non-null    float64
#  5   Healthy life expectancy       156 non-null    float64
#  6   Freedom to make life choices  156 non-null    float64
#  7   Generosity                    156 non-null    float64
#  8   Perceptions of corruption     156 non-null    float64


africa = (
    'Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde',
    'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Congo (Brazzaville)',
    'Congo (Kinshasa)', "Ivory Coast", 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea',
    'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya',
    'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius',
    'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Sao Tome and Principe',
    'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan',
    'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe'
)

asia = (
    'Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei',
    'Cambodia', 'China', 'Cyprus', 'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel',
    'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia',
    'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan',
    'Palestine', 'Philippines', 'Qatar', 'Russia', 'Saudi Arabia', 'Singapore', 'South Korea',
    'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Timor-Leste', 'Turkey',
    'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen',
    'Hong Kong','Northern Cyprus','Palestinian Territories'
)

europe = (
    'Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria',
    'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany',
    'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein',
    'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands',
    'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino',
    'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine',
    'United Kingdom', 'Vatican City','Macedonia'
)

north_america = (
    'Antigua and Barbuda', 'Bahamas', 'Barbados', 'Belize', 'Canada', 'Costa Rica', 'Cuba',
    'Dominica', 'Dominican Republic', 'El Salvador', 'Grenada', 'Guatemala', 'Haiti',
    'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Saint Kitts and Nevis',
    'Saint Lucia', 'Saint Vincent and the Grenadines', 'Trinidad and Tobago',
    'United States','Trinidad & Tobago'
)

oceania = (
    'Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia', 'Nauru', 'New Zealand',
    'Palau', 'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu'
)

south_america = (
    'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay',
    'Peru', 'Suriname', 'Uruguay', 'Venezuela'
)


def map_country_to_region(country):
    
    if country in europe:
        return 'Europe'
    elif country in asia:
        return 'Asia'
    elif country in africa:
        return "Africa"
    elif country in south_america:
        return "South America"
    elif country in north_america:
        return "North America"
    elif country in oceania:
        return "Oceania"
    else:
        return 'Unknown Region'

def map_region_to_color(region):
    # Define color mappings for each region
    if region == 'Europe':
        return 'blue'
    elif region == 'Asia':
        return 'red'
    elif region == "Africa":
        return 'black'
    elif region == "North America":
        return "green"
    elif region == 'South America':
        return "purple"
    elif region == 'Oceania':
        return 'brown'
    else:
        return 'gray'


df['region'] = df['Country or region'].apply(map_country_to_region)
df['color'] = df['region'].apply(map_region_to_color)
df_2019['region'] = df_2019['Country or region'].apply(map_country_to_region)
df_2019['color'] = df_2019['region'].apply(map_region_to_color)



df = df.drop(columns='Overall rank')
df_2019 = df_2019.drop(columns = 'Overall rank')
corr = df.groupby(["region"]).corr()
corr_2019 = df_2019.groupby(['region']).corr()

for i in df['region'].unique():
    
    plt.figure()
    sb.heatmap(corr.loc[i],annot=True)
    plt.xlabel(i+" year 2018",size=25)
    plt.show()

for i in df_2019['region'].unique():
    
    plt.figure()
    sb.heatmap(corr_2019.loc[i],annot=True)
    plt.xlabel(i+" year 2019",size=25)
    plt.show()




plt.figure()
plt.scatter(df["Score"], df["GDP per capita"],c = df['color'])
plt.xlabel('Score')
plt.ylabel('GDP per capita')
plt.title('Scatter Plot with Colors by Region at 2018')

plt.figure()
plt.scatter(df_2019["Score"], df_2019["GDP per capita"],c= df_2019['color'])
plt.xlabel('Score')
plt.ylabel('GDP per capita')
plt.title('Scatter Plot with Colors by Region at 2019')

plt.show()
