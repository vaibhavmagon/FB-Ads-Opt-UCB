# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# Importing the dataset
table_1 = pd.read_csv('ads-data.csv')

#Building the data from facebook according to the algorithm requirement.
def convert(row):
    rewards = row[2]
    array_len = row[1]
    ad = np.zeros(array_len)
    ad[:rewards] = 1
    np.random.shuffle(ad) # Insert rewards in-between misses
    return ad

ads = table_1.apply(convert, axis=1) # Make all the ads as array of 0 & 1's randomly put.
series_list = [pd.Series(ad) for ad in ads] # Making them series i.e in a tabular format.
table_2 = pd.DataFrame(series_list).T # Transposing the Data frame and making Ad centric Table.
dataset = table_2.add_prefix('Ad_')

# Using UCB to find best predictability of Ads.
N = len(dataset)  # Total number of Test
d = len(table_1)  # Number of ads
Selected_Ad = [0]
no_of_selections = [0] * d
Sum_rewards = [0] * d
Total_rewards = 0

for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if (no_of_selections[i] > 0):
            average_reward = Sum_rewards[i] / no_of_selections[i]
            delta_i = math.sqrt(3 / 2 * math.log(n + 1) / no_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    Selected_Ad.append(ad)
    no_of_selections[ad] = no_of_selections[ad] + 1
    reward = dataset.values[n, ad]
    Sum_rewards[ad] = Sum_rewards[ad] + reward

Total_rewards = Total_rewards + reward

print(pd.Series(Selected_Ad).head(N).value_counts(normalize = True))

# Seeing the results
plt.hist(Selected_Ad, bins=d, rwidth=0.5)
plt.title('Histogram of ' + str(d) + ' Ads selected')
plt.xlabel('Ads')
plt.ylabel(str(N) + ' Number of times Ad was selected')
plt.show()