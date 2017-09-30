## This program grabs the data frame from a serialed pickle file and finds interesting facts about it
## We also get the HPI of the United States to use it as a benchmark/
## ZDI - 9/29

#Libraries
import quandl                    # Quandl website functions from this lib
import pandas as pd              # Python Data Analysis Library
import pickle                    # Python data Serialization Library
import matplotlib.pyplot as plt  # Pythons plotting library
from matplotlib import style     # Customize plots with style
style.use('fivethirtyeight')     # Picking the Five Thirthy Eight plot style

#Getting Quandle api key
q_key = open("api_key.txt", "r").read()


# Setting Up Figure
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))



# Getting Housing Price Index of the United States
def HPI_Benchmark():
    df = pd.DataFrame()                                                     # Creating the Data Frame Variable
    df = quandl.get('FMAC/HPI_USA', authtoken = q_key)                      # Using my own quanndle account key to get the dataset of the HPI of the Unted States
    df.rename(columns={'Value':str('United States HPI')}, inplace=True)     # Rename the Columns from Value to USA
    df['United States HPI'] = (df['United States HPI'] - df['United States HPI'][0]) / df['United States HPI'][0] * 100.0           # Convert to Percentage

    return df                                                               # Return Data Frame


benchmark = pd.DataFrame()      # Creating DataFrame Variable
benchmark = HPI_Benchmark()     # Getting United States HPI data for Data Frame

pickle_in = open('states_percent.pickle', 'rb')   # Open the pickle file, and let the program know that we intend to read bytes
data = pd.DataFrame()                             # Create DataFrame
data = pickle.load(pickle_in)                     # Load the data frame from the pickle to the data frame


print(data.head())

# Plotting the Data
data.plot(ax = ax1)
benchmark.plot(ax = ax1, color = 'k', linewidth=10) # Specify characteristics of the benchmark data for the graph


plt.legend().remove()   # Remove legend
plt.show()              # Show the Graph

HPI_State_Correlation = data.corr()     # Correlate the Data
print(HPI_State_Correlation)            # Print the correlated Data Frame

print("\n\n----------------\n\n")
print( HPI_State_Correlation.describe() )   # Describing Data
print("\n-----------------\n\n")


#END Of Program
