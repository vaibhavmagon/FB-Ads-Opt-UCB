# Facebook Ads Optimisation Script Using Real Life Ads 💻

<img src="https://img.shields.io/static/v1?label=Python&message=2.7&color=<COLOR>"> <img src="https://img.shields.io/static/v1?label=Build&message=Passing&color=<COLOR>">

This code analyzes 43 Facebook ad sets and helps find the best ad set using the <a href="http://banditalgs.com/2016/09/18/the-upper-confidence-bound-algorithm/">Upper Confidence Bound</a> machine learning algorithm.

More on UCB here: http://banditalgs.com/2016/09/18/the-upper-confidence-bound-algorithm/


## To Run
1. Export Ad set from Facebook ads directly for Impressions : Signups (Can use it for other data points as well).
2. Replace the data in ads-data.csv with current ads data.
3. Run: sudo python fb-ucb-ads.py


## Data
Folder contains the ads-data.csv file with Ads Impressions : Signups data.


## Ads Histogram for current Data
Clearly Ad: 2 is the winner and should have higher budget allocation.

<img width="641" alt="screen shot 2019-01-31 at 11 46 28 am" src="https://user-images.githubusercontent.com/5276190/52034823-2f6fa200-254f-11e9-93b2-5e309462e942.png">


## Prerequisits
- Python 2.7
- Machine learning libraries
- Anaconda/Spyder


## Contributers
- Vaibhav Magon
