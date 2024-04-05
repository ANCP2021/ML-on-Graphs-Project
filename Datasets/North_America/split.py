import numpy as np
import pandas as pd

# Read CSV
biotime_df = pd.read_csv('BioTIMEQuery_24_06_2021.csv')

# Drop columns
biotime_df_columns_dropped = biotime_df.drop(
    ['Unnamed: 0', 
    'SAMPLE_DESC', 
    'PLOT', 
    'ID_SPECIES', 
    'sum.allrawdata.BIOMASS', 
    'DAY', 
    'MONTH'], 
    axis=1
)

# Define longitude and latitude ranges for area
latitude_range = (-44, -10) 
longitude_range = (113, 153) 

# Filter dataframe by longitude and latitude ranges
subset_biotime_df = biotime_df_columns_dropped[
    (biotime_df_columns_dropped['LATITUDE'] >= latitude_range[0]) & 
    (biotime_df_columns_dropped['LATITUDE'] <= latitude_range[1]) &
    (biotime_df_columns_dropped['LONGITUDE'] >= longitude_range[0]) & 
    (biotime_df_columns_dropped['LONGITUDE'] <= longitude_range[1])
]

# Drop rows where there are 0.0 abundance of species
filter_subset_biotime_df = subset_biotime_df[subset_biotime_df['sum.allrawdata.ABUNDANCE'] != 0.0]

# Combines 'YEAR' and 'GENUS_SPECIES' 
# Aggregates column 'sum.allrawdata.ABUNDANCE' to sum
# Takes the first occurance of the remaining columns (LATITUDE, LONGITUDE, GENUS, SPECIES)
combined_subset_biotime_df = filter_subset_biotime_df.groupby(['YEAR', 'GENUS_SPECIES']).agg({
    'sum.allrawdata.ABUNDANCE': 'sum',  # Sum the abundance
    'LATITUDE': 'first',  # Take the first occurrence for the remaining columns
    'LONGITUDE': 'first',
    'GENUS': 'first',
    'SPECIES': 'first',
    'STUDY_ID': 'first'
}).reset_index()


# combined_subset_biotime_df.to_csv('Filtered_Biotime.csv', sep=',')
print(combined_subset_biotime_df)