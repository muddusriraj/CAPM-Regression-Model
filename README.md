Simple CAPM Regression using the past 9 years of data regarding daily returns.

Data collected from NASDAQ (http://nasdaq.com/) and Federal Reserve Bank of St. Louis (https://fred.stlouisfed.org/).

Parts of the project:
-  Python
    -  Pandas for preprocessing .csv raw data
    -  Format data such that there are consistent dates for the return rates of $SPY, $MSFT, and the T-Bill Return Rate
    -  Format structure of data for usability and merged raw data
-  R
    - Visualize data to verify the usage of linear regression on such a dataset
    - Perform linear regression and create the CAPM model
    - Plotted various graphs to confirm the usability/accuracy of the model
