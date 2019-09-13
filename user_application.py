import pandas as pd
import numpy as np
from datetime import date

interest_rate = 0.04
years = 30
payments_year = 12
addl_principle = 50
start_date = (date(2016,1,1))

# algoirthum trading
# apple - import data source
# Assign `Adj Close` to `daily_close`
daily_close = aapl[['___________']]

# Daily returns
daily_pct_change = daily_close.__________()

# Replace NA values with 0
daily_pct_change.fillna(0, inplace=True)

# Inspect daily returns
print(______________)

# Daily log returns
daily_log_returns = np.log(daily_close.pct_change()+1)

# Print daily log returns
print(daily_log_returns)

# smallest_so_far = -1
# for the_num in [9, 41, 12, 3, 74, 15] :
#    if the_num < smallest_so_far :
#       smallest_so_far = the_num
# print(smallest_so_far)