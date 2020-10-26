import pandas as pd
import matplotlib.pyplot as plt

def compute_daily(series):
    return series.sub(series.shift(fill_value = 0)) 

state_data = pd.read_csv('us-states.csv', parse_dates=['date'], index_col='date')
state_data[['daily_cases', 'daily_deaths']] = (
    state_data.groupby('state')[['cases', 'deaths']]
    .transform( compute_daily )
)

state_data[state_data['state']=='New York']['daily_cases'].plot(kind='bar')



