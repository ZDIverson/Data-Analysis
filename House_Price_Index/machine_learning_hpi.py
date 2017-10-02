import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from statistics import mean
from sklearn import svm, preprocessing, cross_validation


style.use('fivethirtyeight')


def create_labels(cur_hpi, fut_hpi):
    if fut_hpi > cur_hpi:
        return 1
    else:
        return 0



housing_data = pd.read_pickle('HPI2.pickle')
housing_data = housing_data.pct_change()

housing_data.replace([np.inf, -np.inf], np.nan, inplace=True)
housing_data['US_HPI_future'] = housing_data['United States HPI'].shift(-1)

housing_data.dropna(inplace=True)

housing_data['label'] = list(map(create_labels,housing_data['United States HPI'], housing_data['US_HPI_future']))


X = np.array(housing_data.drop(['label','US_HPI_future'], 1))
X = preprocessing.scale(X)

y = np.array(housing_data['label'])


X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)


clf = svm.SVC(kernel='linear')

clf.fit(X_train, y_train)
print('\n\nScore: ')
print(clf.score(X_test, y_test))

print('\n\nEnd Program\n\n')
