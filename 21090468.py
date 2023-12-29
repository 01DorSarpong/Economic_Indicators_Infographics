import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def read_data(file):
    
    """
    This function takes in a csv file as a parameter and returns two
     dataframes, one with columns as years and the other transposed with 
     countries as years. 
    
    Parameter: 
        file: this is a CSV file read into the function
    """
   
    #Reading the CSV file and setting index as country name and series name
    df1 = pd.read_csv(file, index_col=['Series Name', 'Country Name'])
    
    #Removing the country code and series code in df1
    df1 = df1.drop(['Country Code', 'Series Code'], axis = 1)

    #Applying .to_numeric to change all values in the dataframe to floats
    df1 = df1.apply(pd.to_numeric, errors = 'coerce')
    
    #Transposing the dataframe 1 and assigning to new dataframe 2
    df2 = df1.T
         
    #Renaming the index to remove years in [] 
    df2.rename(index = {'1991 [YR1991]': '1991', '1992 [YR1992]':'1992', 
    '1993 [YR1993]': '1993', '1994 [YR1994]':'1994', '1995 [YR1995]': '1995', 
    '1996 [YR1996]': '1996', '1997 [YR1997]':'1997', '1998 [YR1998]': '1998', 
    '1999 [YR1999]': '1999', '2000 [YR2000]':'2000'}, inplace = True)           
        
    #The function returns the two dataframes df1 and df2
    return df1, df2
  
    
#Calling the function with the economic_data csv file
df1, df2 = read_data('project_data.csv')


# Defining variables for my graphs 
years = df2.index
countries = ['United States', 'China', 'Germany', 'Canada', 'United Kingdom', 'South Africa']


# Creating dataframes for all the indicators
pop = df2.xs('Population, total', level=0, axis=1)
labor_force = df2.xs('Labor force, total', level=0, axis=1)
gdp = df2.xs('GDP growth (annual %)', level=0, axis=1)
imports = df2.xs('Imports of goods and services (% of GDP)', level=0, axis=1)
exports = df2.xs('Exports of goods and services (% of GDP)', level=0, axis=1)
inflation = df2.xs('Inflation, consumer prices (annual %)', level=0, axis=1)

avg_inflation = inflation.mean()
avg_gdp = gdp.mean()

# Creating subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10), 
                         gridspec_kw={'hspace': 0.4}, facecolor='lightyellow')
plt.subplots_adjust(wspace=0.4)
plt.subplots_adjust(hspace=0.2) 
fig.suptitle('Economic Performances Based on World Development Indicators',
             fontsize=30, fontweight='bold', color='purple', fontstyle='italic')

# Subplot 1: Bar and Line plot for Imports and Exports of China
sns.barplot(y=imports['China'], x=years, ax=axes[0, 0])
axes[0, 0].set_ylabel('Imports')
axes2 = axes[0, 0].twinx()
#axes2 = axes[0, 0].twiny()
sns.lineplot(y=exports['China'], x=years, ax=axes2, marker='o', color='black')
axes2.set_ylabel('Exports')
axes[0, 0].set_title('Imports and Exports of Goods & Services for China', 
                     fontsize=15, fontweight='bold', color='indigo')
axes[0,0].set(facecolor='lightyellow')


# Subplot 2: Line plot showing Total Labor Force for all countries
axes[0, 1].set_title('Total Labor Force per Country',fontsize=15, fontweight='bold', color='indigo')
for country in countries:
    sns.lineplot(x=years, y=df2['Labor force, total'][country], ax=axes[0, 1],label=country)
axes[0, 1].legend(facecolor='lightyellow')
axes[0, 1].set_ylabel('Total labor force')
axes[0,1].set(facecolor='lightyellow')

# Subplot 3: Bar plot for Average Annual GDP Growth
sns.barplot(x=avg_gdp, y=countries, ax=axes[1, 0], alpha=0.7, palette='colorblind')
axes[1, 0].set_title('Average Annual GDP % Growth from 1991 to 2000', 
                     fontsize=15, fontweight='bold', color='indigo')
axes[1, 0].set_ylabel('Countries')
axes[1, 0].set_xlabel('Annual % Growth')

# Displaying values on the bar plot
for idx, value in enumerate(avg_gdp):
    axes[1, 0].text(value, idx, f'{value:.2f}%', va='center', ha='left', fontsize=10)
axes[1,0].set(facecolor='lightyellow')

# Subplot 4: Pie chart for Average Annual Inflation Growth
axes[1, 1].set_title('Average Annual Inflation % Growth from 1991 to 2000',
                     fontsize=15, fontweight='bold', color='indigo')
explode = [0.15 if country == 'China' else 0.05 for country in countries]
axes[1, 1].pie(avg_inflation, labels=countries, autopct='%1.1f%%', startangle=90, shadow=True, explode=explode)

# Adjust layout
plt.tight_layout(rect=[0,0,1,0.96])
plt.text(12,-8, 
'Student ID: 21090468 \nName: Dorothy Sarpong Kumankoma', horizontalalignment='center', fontsize=20, fontweight='bold')

plt.text(-4,-10, 
'The infographics displayed above shows the economic performance of some selected ' 
         'countries between 1991 and 2000.', fontsize=19, fontstyle='italic')


plt.text(11,-15, 
'Economic indicators help us to assess the performances of countries in comparison with'
'other countries. The above charts \nshow the performance as measured by GDP, Inflation, Imports and Exports'
' of some select countries namely China, Canada,\nGermany, United States, United Kingdom and South Africa.'
'China having a high population and being named in the top 5 \nhighly populated countries in the world reflects this'
' in their high volumes of labour force. The high labour force however \npositively correlates '
'with their economic performances.', horizontalalignment='center', fontsize=19, fontstyle='italic')

plt.text(11,-20,
'A deep dive into the economic performance of China as expressed in the Immports and Exports of Goods and Services\n'
'shows that China had very high imports in year 1994 and 2000 and recorded the highest exports in 1997 and 2000.\n'
'Although United States shows the highest average GDP growth over the period, China also demonstrates'
'a high GDP growth. \n With the lowest inflation amongst all the counries displayed, we can observe a good economic\n'
'performance for China over the period of 1991 to 2000.',horizontalalignment='center',fontsize=19, fontstyle='italic')


plt.savefig("21090468.png", dpi=300)
