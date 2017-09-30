## This program applies rolling statistics on the HPI data frame.
## ZDI - 9/30

#Libraries
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



data['TX12MA'] = pd.rolling_mean(data['TX'], 12)  # Moving Window mean on the Texas hpi data for 12 windows


print(data[['TX','TX12MA']])




data[['TX','TX12MA']].plot(ax = ax1)



plt.legend()
plt.show()


print('\n\n END OF PROGRAM \n\n')


## END OF PROGRAM
