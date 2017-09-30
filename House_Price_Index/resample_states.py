## This program resamples data from texas HPI from month to annualy.
## It then graphs is an displays it show what resample does to data visually
## ZDI - 9/29

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



tx = pd.DataFrame()                     # Creating Data Frame called tx
tx = data['TX'].resample('A').mean()    # Resampling the texas data for average annually
print(tx.head())                        # Print the head of the Texas resampled annually Data Frame



data['TX'].plot(ax = ax1, label = "Monthly TX HPI") # Plot monthly tx HPI data to ax1 with the label Monthly TX HPI
tx.plot(ax = ax1, label = "Yearly TX HPI")          # Plot the TX on ax1 with the label Yearly TX HPI


plt.legend()    # Display Legend
plt.show()      # Show the figure 

print("\n\nEnd of Program\n\n")
#End of Program
