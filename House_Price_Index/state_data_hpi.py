## This program uses an API to get HPI data from Quandl.
## After all the HPI data from all 50 states, it then is convereted to a percentage and then serialized to a file.
## ZDI - 9/29


#Libraries
import quandl           # quandl website functions from this lib
import pandas as pd     # Python Data Analysis Library
import pickle           # Python data Serialization Library


#Grab the API given from my quandl account
q_key = open("api_key.txt", "r").read()


# Getting States Abbreviations
def state_list():
    states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states') # Using the read_html pandas functions to parse the website for state Abbreviations
    return states[0][0][1:]

#Creating the main data frame
main_df = pd.DataFrame()

#Grabbing the list of states
states = state_list()

#Going thought all states and getting the HPI data
for abv in states:
    #Creating the query for all states
    query = ("FMAC/HPI_" + str(abv))
    #Getting the data frame from quandl
    df = quandl.get(query, authtoken = q_key)
    #Renaming the columns form Value to the State Abbreviation
    df.rename(columns={'Value':str(abv)}, inplace=True)
    #Converting it to percentage
    df[abv] = (df[abv] - df[abv][0]) / df[abv][0] * 100.0
    #Printing it out to let me know what dataframe were getting
    print(query)

    #Data Frame Joining logic
    if main_df.empty:
        main_df = df
    else:
        main_df = main_df.join(df)


print(main_df.head())


# Write the DataFrame to a Pickle!
pickle_out = open('states_percent.pickle', 'wb') # Create a file called 'states_percent.pickle' and let it know that we plane on writing bytes 'wb'.
pickle.dump(main_df, pickle_out) # Writing our datafram to the pickle file
pickle_out.close() # Close the pickel file

print("\nSuccesfully Grabed Data from Quandle and serialized in a pickle file\n-----------------------\n")

## END of Program
