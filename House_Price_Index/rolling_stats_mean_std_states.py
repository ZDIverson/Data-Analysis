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


# Applying Rolling functions
data['TX12MA'] = data['TX'].rolling(window=12,center=False).mean()      # Rolling statistics for 12 windows of Texas with mean function
data['TX12STD'] = data['TX'].rolling(window=12,center=False).std()      # Rolling statistics for 12 windows of Texas with standard deviation function


# Assigning data for specific axis on the graph
data['TX'].plot(ax=ax1)
data['TX12MA'].plot(ax=ax1)
data['TX12STD'].plot(ax=ax2, label ='TX12STD STD', color = '#696969')


# Showing graph as figure
handles,labels = [],[]
for ax in fig.axes:
    for h,l in zip(*ax.get_legend_handles_labels()):
        handles.append(h)
        labels.append(l)

plt.legend(handles,labels,loc='upper center', bbox_to_anchor=(0.5, 2.35), ncol=3, fancybox=True, shadow=True)
plt.show()



print('\n\n End of Program \n\n')
## END OF PROGRAM
