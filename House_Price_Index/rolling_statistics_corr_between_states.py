## This program applies rolling statistics on the HPI data frame.
## Specifically rolling mean and standard deviation
## ZDI - 9/30

#Libraries
import pandas as pd              # Python Data Analysis Library
import pickle                    # Python data Serialization Library
import matplotlib.pyplot as plt  # Pythons plotting library
from matplotlib import style     # Customize plots with style
style.use('fivethirtyeight')     # Picking the Five Thirthy Eight plot style


# Setting Up Figure
fig = plt.figure()
ax1 = plt.subplot2grid((2,1), (0,0))
ax2 = plt.subplot2grid((2,1), (1,0), sharex=ax1)


pickle_in = open('states_percent.pickle', 'rb')   # Open the pickle file, and let the program know that we intend to read bytes
data = pd.DataFrame()                             # Create DataFrame
data = pickle.load(pickle_in)                     # Load the data frame from the pickle to the data frame


TX_AK_12corr = pd.rolling_corr(data['TX'], data['AK'], 12)



data['TX'].plot(ax=ax1, label="TX HPI")
data['AK'].plot(ax=ax1, label="AK HPI")
ax1.legend(loc=4)

TX_AK_12corr.plot(ax=ax2)

plt.show()



print('\n\n  End of Program \n\n')
## END of Program
