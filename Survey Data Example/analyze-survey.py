import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Read in data
data = pd.read_csv('./Survey Data Example/DigitalCamera_030413.csv', parse_dates=[1, 2])
print(data.head())
print(data.columns)
print(data.dtypes)

# Code Data
# Documentation on Categorical Variables https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html
data["Gender"] = data["D1"].astype('category')
data["Gender"] = data["Gender"].cat.rename_categories(['Male', 'Female'])

data["Age"] = 2020 - data["D2"]

min(data["Age"])
max(data["Age"])

# 25 - 80 What groups do we want?
labels = ["18 - 35", "36 - 50", "51 - 65", "65+"]
data["AgeGroups"] = pd.cut(data["Age"], bins=[18, 35, 50, 65, 100], labels=labels)

# We have 6 education categories - We only want 3 - No College (1-2), Undergraduate (3-4), Advanced Degree (5-6)
data["Education"] = data["D6"]
data.loc[data["Education"] == 2, "Education"] = 1
data.loc[data["Education"] == 3, "Education"] = 2
data.loc[data["Education"] == 4, "Education"] = 2
data.loc[data["Education"] == 5, "Education"] = 3
data.loc[data["Education"] == 6, "Education"] = 3
data["Education"] = data["Education"].astype('category').cat.rename_categories(['No College',
                                                                                'Undergraduate',
                                                                                'Advanced Degree'])

data["Education"].value_counts().plot()


# Continue for other quesitons.

# Clean Data

# Check for missing data
# Remove respondents who say that they don't have an electronic device, but do have a camera???
data = data[data["T1_7"] == 0]

# Check for straight lining
# This looks across multiple questions to see if the variance is 0.0.  It the variance is 0.0 then the respondents
# answered the same for 16 straight questions
data = data[data.loc[:, ["DC_{col}".format(col=i) for i in range(1, 17)]].var(axis=1) != 0.0]

# Check for speeding
data = data[data["ILength"] > data["ILength"].quantile(0.05)]

# Demonstrate running cross tabs
data["Gender"].value_counts()
pd.crosstab(data["Education"], data["Gender"])


# Plot stuff
data["Gender"].value_counts().plot()
