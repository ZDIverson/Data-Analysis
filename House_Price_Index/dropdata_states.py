## This program drops rows/data from the dataframe that is missing data.
## ZDI - 9/30

#Libraries
import quandl                    # Quandl website functions from this lib
import pandas as pd              # Python Data Analysis Library
import pickle                    # Python data Serialization Library
import matplotlib.pyplot as plt  # Pythons plotting library
from matplotlib import style     # Customize plots with style
style.use('fivethirtyeight')     # Picking the Five Thirthy Eight plot style


# Setting Up Figure
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))


pickle_in = open('states_percent.pickle', 'rb')   # Open the pickle file, and let the program know that we intend to read bytes
data = pd.DataFrame()                             # Create DataFrame
data = pickle.load(pickle_in)                     # Load the data frame from the pickle to the data frame

# Creating data frames to use later
DF2 = pd.DataFrame()
tx = pd.DataFrame()


data['TX1yr']= data['TX'].resample('A').mean() # Creating Column named 'TX1yr' which is the mean of the tx hpi data of each year


print(data[['TX','TX1yr']].head()) # Print to show that TX1yr Column has nan data for some rows


DF2 = data.dropna() # Drops all rows that have nan in it

print('\n---------------\n')
print(DF2[['TX','TX1yr']].head()) # See there is no more rows that have nan in it


# Graph data
DF2[['TX','TX1yr']].plot(ax = ax1)



plt.legend()
plt.show()



print('\n\n End of Program \n\n')
