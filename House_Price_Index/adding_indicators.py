## This program adds indicators to the existing dataset.
## Formats the data to apply a simple machine learning algorithm to it.
## Then applies a simple machine learning algorithm to the data to give us a score.
## ZDI - 10/1

#Libraries
import pandas as pd              # Python Data Analysis Library
import pickle                    # Python data Serialization Library
import quandl
import matplotlib.pyplot as plt  # Pythons plotting library
from matplotlib import style     # Customize plots with style

style.use('fivethirtyeight')     # Picking the Five Thirthy Eight plot style


q_key = open("api_key.txt", "r").read()




def mortgage_30y():
    m30 = pd.DataFrame()
    m30 = quandl.get("FMAC/MORTG", trim_start="1975-01-01", authtoken=q_key)
    m30["Value"] = (m30["Value"]-m30["Value"][0]) / m30["Value"][0] * 100.0
    m30=m30.resample('1D').mean()
    m30=m30.resample('M').mean()
    m30.columns = ['M30']
    return m30


def sp500_data():
    df = quandl.get("MULTPL/SP500_REAL_PRICE_MONTH", trim_start="1975-01-01", authtoken=q_key)
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    df=df.resample('M').mean()
    df.rename(columns={'Value':'sp500'}, inplace=True)
    df = df['sp500']
    return df


def gdp_data():
    df = quandl.get("BCB/4385", trim_start="1975-01-01", authtoken=q_key)
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    df=df.resample('M').mean()
    df.rename(columns={'Value':'GDP'}, inplace=True)
    df = df['GDP']
    return df


def us_unemployment():
    df = quandl.get("FRED/UNRATE", trim_start="1975-01-01", authtoken=q_key)
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    df=df.resample('1D').mean()
    df=df.resample('M').mean()
    df.columns = ['Unemployment Rate']
    return df


# Getting Housing Price Index of the United States
def HPI_Benchmark():
    df = pd.DataFrame()                                                     # Creating the Data Frame Variable
    df = quandl.get('FMAC/HPI_USA', authtoken = q_key)                      # Using my own quanndle account key to get the dataset of the HPI of the Unted States
    df.rename(columns={'Value':str('United States HPI')}, inplace=True)     # Rename the Columns from Value to USA
    df['United States HPI'] = (df['United States HPI'] - df['United States HPI'][0]) / df['United States HPI'][0] * 100.0           # Convert to Percentage

    return df                                                               # Return Data Frame



benchmark = pd.DataFrame()
benchmark = HPI_Benchmark()
#print (benchmark.head())
pickle_in = open('fifty_states_percent.pickle', 'rb')
states = pd.DataFrame()
states = pickle.load(pickle_in)

sp500 = sp500_data()
m30 = mortgage_30y()
gdp = gdp_data()
unemployment = us_unemployment()

HPI = pd.DataFrame()
HPI = states.join([benchmark,m30,sp500,gdp,unemployment])
HPI.dropna(inplace = True)
print(HPI.head())

HPI.to_pickle('HPI2.pickle')
