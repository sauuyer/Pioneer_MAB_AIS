import pandas as pd
import sidetable

# read in merged file

#ais_data = pd.read_csv("../point_data/merged_AIS_data.csv")
#print(ais_data.head())

sample_point_data_jan = pd.read_csv("../point_data/AIS_2022_01_01.csv")
sample_point_data_feb = pd.read_csv("../point_data/AIS_2022_02_01.csv")
sample_point_data_mar = pd.read_csv("../point_data/AIS_2022_03_01.csv")
sample_point_data_apr = pd.read_csv("../point_data/AIS_2022_04_01.csv")
sample_point_data_may = pd.read_csv("../point_data/AIS_2022_05_01.csv")
sample_point_data_june = pd.read_csv("../point_data/AIS_2022_06_01.csv")
sample_point_data_july = pd.read_csv("../point_data/AIS_2022_07_01.csv")
sample_point_data_aug = pd.read_csv("../point_data/AIS_2022_08_01.csv")
sample_point_data_sep = pd.read_csv("../point_data/AIS_2022_09_01.csv")
sample_point_data_oct = pd.read_csv("../point_data/AIS_2022_10_01.csv")
sample_point_data_nov = pd.read_csv("../point_data/AIS_2022_11_01.csv")
sample_point_data_dec = pd.read_csv("../point_data/AIS_2022_12_01.csv")

all_months_all_cords = [sample_point_data_jan, sample_point_data_feb, sample_point_data_mar, sample_point_data_apr, sample_point_data_may, sample_point_data_june,
                        sample_point_data_july, sample_point_data_aug, sample_point_data_sep, sample_point_data_oct, sample_point_data_nov, sample_point_data_dec]


# include only relevant lat lon information

### mooring box
max_lat_m = 36.25
min_lat_m = 35.63
max_lon_m = -74.6667
min_lon_m = -75.3667

df = sample_point_data[sample_point_data['LAT'] > min_lat_m]
df = df[df['LAT'] < max_lat_m]
df = df[df['LON'] > min_lon_m]
mooring_box_data = df[df['LON'] < max_lon_m]

for df in all_months_all_cords:
    df = sample_point_data[sample_point_data['LAT'] > min_lat_m]
    df = df[df['LAT'] < max_lat_m]
    df = df[df['LON'] > min_lon_m]
    #mooring_box_data = df[df['LON'] < max_lon_m]
    df

#print(mooring_box_data.DatetimeIndex.month)
mooring_box_data['month'] = mooring_box_data.BaseDateTime.str[5:7]

print(len(mooring_box_data.index))
print(mooring_box_data)

### glider box
max_lat_g = 37.1667
min_lat_g = 35.5
max_lon_g = -74.3333
min_lon_g = -75.3667


df = sample_point_data[sample_point_data['LAT'] > min_lat_g]
df = df[df['LAT'] < max_lat_g]
df = df[df['LON'] > min_lon_g]
glider_box_data = df[df['LON'] < max_lon_m]

print(len(glider_box_data.index))





############### Table - per month vessel counts
#   unique vessels ->  unique MMSI   |   unique vessel types ->  unique VesselType   |   AIS transmissions -> total rows

print("unique mmsi::::", mooring_box_data['MMSI'].nunique())
print(mooring_box_data.stb.freq(['MMSI']))
print(mooring_box_data.stb.freq(['VesselType']))
print(mooring_box_data.stb.freq(['month']))


# Table - types of unique ships passing thorugh the full region per month
