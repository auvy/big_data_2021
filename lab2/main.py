import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium
import os

from matplotlib import colors


#PART2
#step1
folder_path = os.path.dirname(os.path.abspath(__file__))

dataset_path = folder_path + '\\res\Map-Crime_Incidents-Previous_Three_Months.csv'

SF = pd.read_csv(dataset_path)

#step2

pd.set_option('display.max_rows', 10)
# print(SF)
# print('VARIABLES:', SF.columns)
# print('AMOUNT OF COLUMNS:', len(SF.columns))
# print('AMOUNT OF ROWS:', len(SF))


#PART3
#step1

SF['Month'] = SF['Date'].apply(lambda row: int(row[0:2]))
SF['Day'] = SF['Date'].apply(lambda row: int(row[3:5]))

# print(SF['Month'][0:2])
# print(SF['Day'][0:2])

# print(type(SF['Month'][0]))

#step2
del SF['IncidntNum']

SF.drop('Location', axis=1, inplace=True )
# print('DATABASE: ', SF)
# print('COLUMNS:', SF.columns)
# print('AMOUNT OF COLUMNS:', len(SF.columns))

#PART4
#step1
# print('Most frequent offence:', SF['Category'].value_counts()[0:1])
# print('Most dangerous district:', SF['PdDistrict'].value_counts()[0:1])

#step2
AugustCrimes = SF[SF['Month'] == 8]
# print('Crimes in August:', len(AugustCrimes))
BurglaryAugust = SF[SF['Category'] == 'BURGLARY']
# print('Burglaries of August:', len(BurglaryAugust))
Crime0704 = SF.query('Month == 7 and Day == 4')
# print('Crimes as of July 4th:', len(Crime0704))


#PART5
#step1
# plt.plot(SF['X'],SF['Y'], 'ro')
# plt.show()

pd_districts = np.unique(SF['PdDistrict'])
pd_districts_levels = dict(zip(pd_districts, range(len(pd_districts))))

SF['PdDistrictCode'] = SF['PdDistrict'].apply(lambda row: pd_districts_levels[row])
# print(pd_districts_levels)


# plt.scatter(SF['X'], SF['Y'], c=SF['PdDistrictCode'])
# plt.show()

#step2
districts = np.unique(SF['PdDistrict'])
# print('Colors:', list(colors.cnames.values())[0:len(districts)])
color_dict = dict(zip(districts, list(colors.cnames.values())[0:-1:len(districts)]
))
# print(color_dict)

map_osm = folium.Map(location=[SF['Y'].mean(), SF['X'].mean()], zoom_start = 12)
plotEvery = 50
obs = list(zip( SF['Y'], SF['X'], SF['PdDistrict']))
for el in obs[0:-1:plotEvery]:
    folium.CircleMarker(el[0:2], color=color_dict[el[2]], fill_color=el[2],radius=10).add_to(map_osm)

map_osm.save("map.html")
